""" trigger/63000006_cs/shake03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5070], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5070], visible=True)

    def on_tick(self) -> state.State:
        if true():
            return 간격랜덤()


class 간격랜덤(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return 초간격4()
        if random_condition(rate=25):
            return 초간격5()
        if random_condition(rate=25):
            return 초간격6()
        if random_condition(rate=25):
            return 초간격7()


class 초간격4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 초기화()
        if user_detected(boxIds=[9002]):
            return 종료()


class 초간격5(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 초기화()
        if user_detected(boxIds=[9002]):
            return 종료()


class 초간격6(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 초기화()
        if user_detected(boxIds=[9002]):
            return 종료()


class 초간격7(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 초기화()
        if user_detected(boxIds=[9002]):
            return 종료()


class 초기화(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5070], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 시작()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5070], visible=False)


