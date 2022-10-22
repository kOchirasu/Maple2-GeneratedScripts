""" trigger/52020001_qd/main_3_2.xml """
from common import *
import state


class 경고텍스트발생(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=1):
            return 경고텍스트()


class 경고텍스트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='더이상 상대할 수 없습니다.\n포탑을 이용해 다른 곳으로 이동하세요.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 경고텍스트_2()
        if user_value(key='respawn_end', value=2):
            return 끝()


class 경고텍스트_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='더이상 상대할 수 없습니다.\n포탑을 이용해 다른 곳으로 이동하세요.', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 경고텍스트()
        if user_value(key='respawn_end', value=2):
            return 끝()


class 끝(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return None


