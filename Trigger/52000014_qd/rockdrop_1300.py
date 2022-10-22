""" trigger/52000014_qd/rockdrop_1300.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1300], isEnable=False)
        set_skill(triggerIds=[1302], isEnable=False)
        set_skill(triggerIds=[1304], isEnable=False)
        set_effect(triggerIds=[1301], visible=False) # RockDrop
        set_effect(triggerIds=[1303], visible=False) # RockDrop
        set_effect(triggerIds=[1305], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 낙하01시작()


class 낙하01시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1301], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 낙하01완료()


class 낙하01완료(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1300], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 낙하02시작()


class 낙하02시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1303], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 낙하02완료()


class 낙하02완료(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=2)
        set_skill(triggerIds=[1302], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 낙하03시작()


class 낙하03시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[1305], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return 낙하03완료()


class 낙하03완료(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=1)
        set_skill(triggerIds=[1304], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=2)
        set_skill(triggerIds=[1300], isEnable=False)
        set_skill(triggerIds=[1302], isEnable=False)
        set_skill(triggerIds=[1304], isEnable=False)
        set_effect(triggerIds=[1301], visible=False) # RockDrop
        set_effect(triggerIds=[1303], visible=False) # RockDrop
        set_effect(triggerIds=[1305], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 낙하01시작()


