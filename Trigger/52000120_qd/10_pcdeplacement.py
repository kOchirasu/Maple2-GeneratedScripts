""" trigger/52000120_qd/10_pcdeplacement.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='DefencePhase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DefencePhase', value=1):
            return DefencePhase01(self.ctx)


class DefencePhase01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, minUsers='1'):
            return MoveToTheWall(self.ctx)
        if self.user_value(key='DefencePhase', value=2):
            return DefencePhase02(self.ctx)


class MoveToTheWall(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000120, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefencePhase01(self.ctx)
        if self.user_value(key='DefencePhase', value=2):
            return DefencePhase02(self.ctx)


class DefencePhase02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, minUsers='1'):
            return OutsideOfTheWall(self.ctx)
        if self.user_value(key='DefencePhase', value=3):
            return Quit(self.ctx)


class OutsideOfTheWall(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000120, portalId=40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefencePhase02(self.ctx)
        if self.user_value(key='DefencePhase', value=3):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
