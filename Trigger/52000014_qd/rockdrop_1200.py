""" trigger/52000014_qd/rockdrop_1200.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1200], isEnable=False)
        set_effect(triggerIds=[1201], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 낙하01준비()


class 낙하01준비(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 낙하01시작()


class 낙하01시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1201], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 낙하01완료()


class 낙하01완료(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=1)
        set_skill(triggerIds=[1200], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=1)
        set_skill(triggerIds=[1200], isEnable=False)
        set_effect(triggerIds=[1201], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 낙하01준비()


