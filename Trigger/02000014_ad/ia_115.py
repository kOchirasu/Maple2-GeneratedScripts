""" trigger/02000014_ad/ia_115.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000115], state=1)
        self.set_actor(triggerId=115, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000115], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=115, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[93], animationEffect=False)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=93, patrolName='MS2PatrolData403')
        self.set_conversation(type=1, spawnId=93, script='$02000014_AD__IA_115__0$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=293, spawnIds=[93]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[93])
        self.set_timer(timerId='303', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='303'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
