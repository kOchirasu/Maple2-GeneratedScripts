""" trigger/03009023_in/07.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000239], state=1)
        self.create_monster(spawnIds=[107], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000239], stateValue=0):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=12)
        self.destroy_monster(spawnIds=[107])
        self.create_monster(spawnIds=[207], animationEffect=True)
        self.move_npc(spawnId=207, patrolName='MS2PatrolData_207')
        self.set_conversation(type=1, spawnId=207, script='$03009023_IN__07__0$', arg4=4, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[207])
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
