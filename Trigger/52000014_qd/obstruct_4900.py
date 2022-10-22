""" trigger/52000014_qd/obstruct_4900.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[4900], isEnable=False)
        set_effect(triggerIds=[490], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 발동준비()


class 발동준비(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발동()


class 발동(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=3)
        set_skill(triggerIds=[4900], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=1)
        set_skill(triggerIds=[4900], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 발동준비()


