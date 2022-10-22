""" trigger/02000047_bf/04_rarebox_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[404], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[204]):
            return 발판04()


class 발판04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[404], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[204]):
            return 발판04끝()


class 발판04끝(state.State):
    def on_enter(self):
        set_timer(timerId='504', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='504'):
            return 대기()


