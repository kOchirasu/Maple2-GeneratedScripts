""" trigger/52000120_qd/10_pcdeplacement.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='DefencePhase', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='DefencePhase', value=1):
            return DefencePhase01(self.ctx)


class DefencePhase01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9000, boxId=1):
            return MoveToTheWall(self.ctx)
        if self.user_value(key='DefencePhase', value=2):
            return DefencePhase02(self.ctx)


class MoveToTheWall(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000120, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefencePhase01(self.ctx)
        if self.user_value(key='DefencePhase', value=2):
            return DefencePhase02(self.ctx)


class DefencePhase02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9000, boxId=1):
            return OutsideOfTheWall(self.ctx)
        if self.user_value(key='DefencePhase', value=3):
            return Quit(self.ctx)


class OutsideOfTheWall(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000120, portalId=40)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefencePhase02(self.ctx)
        if self.user_value(key='DefencePhase', value=3):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
