""" trigger/99999841/pc_move.xml """
from common import *
import state


class 대기(state.State):
    pass


class 애디셔널체크(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if check_any_user_additional_effect(boxId=9001, additionalEffectId=70002541, level=1):
            return 유저이동확률()


class 유저이동확률(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if random_condition(rate=33):
            return 유저이동1()
        if random_condition(rate=34):
            return 유저이동2()
        if random_condition(rate=33):
            return 유저이동3()


class 유저이동1(state.State):
    def on_enter(self):
        move_user(mapId=99999840, portalId=2, boxId=9102)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if true():
            return 대기()


class 유저이동2(state.State):
    def on_enter(self):
        move_user(mapId=99999840, portalId=3, boxId=9102)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if true():
            return 대기()


class 유저이동3(state.State):
    def on_enter(self):
        move_user(mapId=99999840, portalId=4, boxId=9102)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='2', value=1):
            return 종료()
        if true():
            return 대기()


class 종료(state.State):
    pass


