""" trigger/02000047_bf/03_rarebox_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[305], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 발판05()


class 발판05(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[305], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[105]):
            return 발판05끝()


class 발판05끝(state.State):
    def on_enter(self):
        set_timer(timerId='405', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='405'):
            return 대기()


