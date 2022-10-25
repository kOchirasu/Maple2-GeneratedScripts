""" trigger/52100041_qd/event_03.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[171], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[704]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=171, patrolName='MS2PatrolData_2139')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ready_02(self.ctx)


class Ready_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[171])


initial_state = idle
