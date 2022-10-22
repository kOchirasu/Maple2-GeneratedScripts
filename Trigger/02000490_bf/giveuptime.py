""" trigger/02000490_bf/giveuptime.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 타이머()


class 타이머(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            set_event_ui(type=1, arg2='$DUNGEON__GIVEUP__TIME__0$', arg3='3000')
            dungeon_enable_give_up(isEnable='1')
            return 종료()


class 종료(state.State):
    pass


