""" trigger/99999840/boss_hpcheck.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='210', value=1):
            return 메시지1()


class 메시지1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='B팀의 보스 체력이 70% 이하입니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='220', value=1):
            return 메시지2()


class 메시지2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='B팀의 보스 체력이 50% 이하입니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='230', value=1):
            return 메시지3()


class 메시지3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='B팀의 보스 체력이 30% 이하입니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='240', value=1):
            return 메시지4()


class 메시지4(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='B팀의 보스 체력이 10% 이하입니다.', arg3='5000')

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


