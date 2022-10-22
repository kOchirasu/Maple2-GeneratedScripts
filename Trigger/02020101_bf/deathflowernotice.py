""" trigger/02020101_bf/deathflowernotice.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='notice', value=1):
            return 경고()
        if monster_dead(boxIds=[101]):
            return 종료()


class 경고(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020101_BF__DEATHFLOWERNOTICE__0$', arg3='3000')
        set_user_value(triggerId=900005, key='notice', value=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='notice', value=0):
            return 대기()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=900005, key='notice', value=0)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


