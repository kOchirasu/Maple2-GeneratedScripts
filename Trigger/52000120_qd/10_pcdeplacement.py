""" trigger/52000120_qd/10_pcdeplacement.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='DefencePhase', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='DefencePhase', value=1):
            return DefencePhase01()


class DefencePhase01(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=1):
            return MoveToTheWall()
        if user_value(key='DefencePhase', value=2):
            return DefencePhase02()


class MoveToTheWall(state.State):
    def on_enter(self):
        move_user(mapId=52000120, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefencePhase01()
        if user_value(key='DefencePhase', value=2):
            return DefencePhase02()


class DefencePhase02(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=1):
            return OutsideOfTheWall()
        if user_value(key='DefencePhase', value=3):
            return Quit()


class OutsideOfTheWall(state.State):
    def on_enter(self):
        move_user(mapId=52000120, portalId=40)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefencePhase02()
        if user_value(key='DefencePhase', value=3):
            return Quit()


class Quit(state.State):
    pass


