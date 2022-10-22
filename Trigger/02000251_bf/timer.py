""" trigger/02000251_bf/timer.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3001], visible=False)
        set_effect(triggerIds=[3002], visible=False)
        set_effect(triggerIds=[3003], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[202]):
            return 초재기1()


class 초재기1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 초재기2()
        if count_users(boxId=202, boxId=4):
            return 초재기2()


class 초재기2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=5)
        set_event_ui(type=1, arg2='$02000251_BF__TIMER__0$', arg3='3000', arg4='0')
        set_effect(triggerIds=[3001], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=5)
        set_event_ui(type=1, arg2='$02000251_BF__TIMER__1$', arg3='3000', arg4='0')
        set_effect(triggerIds=[3002], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 초재기3()


class 초재기3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000251_BF__TIMER__2$', arg3='5000', arg4='0')

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


