""" trigger/02000047_bf/04_rarebox_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[401], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[201]):
            return 발판01()


class 발판01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[401], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[201]):
            return 발판01끝()


class 발판01끝(state.State):
    def on_enter(self):
        set_timer(timerId='501', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='501'):
            return 대기()

