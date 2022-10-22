""" trigger/61000004_me/notice.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 어나운스0()


class 어나운스0(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=15, clearAtZero=False) # action name="이벤트UI를설정한다" arg1="1" arg2="$61000004_ME__NOTICE__0$" arg3="4000" arg4="102" /

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 대기()


