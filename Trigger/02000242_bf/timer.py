""" trigger/02000242_bf/timer.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2001], visible=False)
        set_effect(triggerIds=[2002], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[205]):
            return 초재기1()


class 초재기1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 초재기2()


class 초재기2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2001], visible=True)
        set_event_ui(type=1, arg2='$02000242_BF__TIMER__0$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 유저이동음성()


class 유저이동음성(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 유저이동()


class 유저이동(state.State):
    pass


