""" trigger/02000403_bf/event_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[171], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=704, type='trigger', achieve='Hauntedmansion')
        self.move_npc(spawnId=171, patrolName='MS2PatrolData_2139')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ready_02(self.ctx)


class Ready_02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[171])


initial_state = idle
