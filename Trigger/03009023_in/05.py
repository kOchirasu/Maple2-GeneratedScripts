""" trigger/03009023_in/05.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000237], state=1)
        self.create_monster(spawnIds=[105], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000237], stateValue=0):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=8)
        self.destroy_monster(spawnIds=[105])
        self.create_monster(spawnIds=[205], animationEffect=True)
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        self.set_conversation(type=1, spawnId=205, script='$03009023_IN__05__0$', arg4=4, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[205])
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
