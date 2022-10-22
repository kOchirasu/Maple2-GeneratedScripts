""" trigger/52000014_qd/rockdrop_1000.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1000], isEnable=False)
        set_skill(triggerIds=[1002], isEnable=False)
        set_skill(triggerIds=[1004], isEnable=False)
        set_effect(triggerIds=[1001], visible=False) # RockDrop
        set_effect(triggerIds=[1003], visible=False) # RockDrop
        set_effect(triggerIds=[1005], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 낙하01시작()


class 낙하01시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1001], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 낙하01완료()


class 낙하01완료(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1000], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 낙하02시작()


class 낙하02시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1003], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 낙하02완료()


class 낙하02완료(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=2)
        set_skill(triggerIds=[1002], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 낙하03시작()


class 낙하03시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1005], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 낙하03완료()


class 낙하03완료(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=1)
        set_skill(triggerIds=[1004], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=2)
        set_skill(triggerIds=[1000], isEnable=False)
        set_skill(triggerIds=[1002], isEnable=False)
        set_skill(triggerIds=[1004], isEnable=False)
        set_effect(triggerIds=[1001], visible=False) # RockDrop
        set_effect(triggerIds=[1003], visible=False) # RockDrop
        set_effect(triggerIds=[1005], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 낙하01시작()


