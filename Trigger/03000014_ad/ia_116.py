""" trigger/03000014_ad/ia_116.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000116], state=1)
        self.set_actor(triggerId=116, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000116], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=116, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[94], animationEffect=False)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=94, patrolName='MS2PatrolData404')
        self.set_conversation(type=1, spawnId=94, script='$03000014_AD__IA_116__0$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=294, spawnIds=[94]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[94])
        self.set_timer(timerId='304', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='304'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
