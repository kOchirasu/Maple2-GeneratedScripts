""" trigger/02010039_bf/checkbridge06.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[5002], questIds=[40002110], questStates=[1]):
            return 업적발생()


class 업적발생(state.State):
    def on_enter(self):
        set_achievement(triggerId=5002, type='trigger', achieve='checkBridge')

    def on_tick(self) -> state.State:
        if true():
            return 초기화준비()


class 초기화준비(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


