""" trigger/80000003_bonus/t1_congratulation.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 축하대기1()


class 축하대기1(state.State):
    def on_tick(self) -> state.State:
        if bonus_game_reward_detected(boxId=100, arg2=True):
            return 축하1()


class 축하1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200], visible=True)

    def on_tick(self) -> state.State:
        if true():
            return 축하2()


class 축하2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=100, script='$80000003_bonus__T1_CONGRATULATION__0$')
        set_conversation(type=1, spawnId=101, script='$80000003_bonus__T1_CONGRATULATION__1$')
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 완료()


class 완료(state.State):
    pass


