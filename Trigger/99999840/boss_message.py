""" trigger/99999840/boss_message.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if dungeon_variable(varID='200', value=1):
            return 메시지1()


class 메시지1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='B팀의 보스가 등장했습니다!', arg3='4000')

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


