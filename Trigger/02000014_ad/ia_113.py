""" trigger/02000014_ad/ia_113.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000113], state=1)
        self.set_actor(triggerId=113, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000113], stateValue=0):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=113, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[91], animationEffect=False)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=91, patrolName='MS2PatrolData401')
        self.set_conversation(type=1, spawnId=91, script='$02000014_AD__IA_113__0$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=291, spawnIds=[91]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[91])
        self.set_timer(timerId='301', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='301'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
