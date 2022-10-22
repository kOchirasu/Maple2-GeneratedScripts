""" trigger/02020065_bf/message.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__0$', arg3='5000')

    def on_tick(self) -> state.State:
        if user_value(key='FieldGameStart', value=1):
            return 체력공지_1()
        if user_value(key='FieldGameStart', value=2):
            return 체력공지_1()
        if wait_tick(waitTick=5000):
            return 대기()


class 체력공지_1(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=801, isRelative=True):
            set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__1$', arg3='5000')
            return 체력공지_2()


class 체력공지_2(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=30, spawnId=801, isRelative=True):
            set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__2$', arg3='5000')
            return 체력공지_3()


class 체력공지_3(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=10, spawnId=801, isRelative=True):
            set_event_ui(type=1, arg2='$02020065_BF__MESSAGE__3$', arg3='5000')
            return 종료()


class 종료(state.State):
    pass


