""" trigger/52000014_qd/actor_8000.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8100], visible=False) # Rage
        self.destroy_monster(spawnIds=[800,801])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 약화01(self.ctx)


class 약화01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[800], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 교체01(self.ctx)


class 교체01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.destroy_monster(spawnIds=[800])
        self.create_monster(spawnIds=[801], animationEffect=False)
        self.move_npc(spawnId=801, patrolName='MS2PatrolData_801')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 일어남01(self.ctx)


class 일어남01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 포효01(self.ctx)


class 포효01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=5)
        self.set_effect(triggerIds=[8100], visible=True) # Rage

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 종료01(self.ctx)


class 종료01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8100], visible=False) # Rage


initial_state = 대기
