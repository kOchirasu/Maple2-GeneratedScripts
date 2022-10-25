""" trigger/03009023_in/04.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000222], state=1)
        self.create_monster(spawnIds=[104], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000222], stateValue=0):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=8)
        self.destroy_monster(spawnIds=[104])
        self.create_monster(spawnIds=[204], animationEffect=True)
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204')
        self.set_conversation(type=1, spawnId=204, script='$03009023_IN__04__0$', arg4=4, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[204])
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
