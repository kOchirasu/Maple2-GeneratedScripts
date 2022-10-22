""" trigger/61000005_me/wait.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        set_timer(timerId='90', seconds=90, clearAtZero=True, display=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[196]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000005_ME__WAIT__0$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if count_users(boxId=196, boxId=20):
            return 시작()
        if wait_tick(waitTick=10000):
            return 대기()
        if time_expired(timerId='90'):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000005_ME__WAIT__1$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 종료()


class 종료(state.State):
    pass


