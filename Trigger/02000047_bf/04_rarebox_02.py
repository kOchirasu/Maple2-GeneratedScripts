""" trigger/02000047_bf/04_rarebox_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[402], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[202]):
            return 발판02()


class 발판02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[402], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[202]):
            return 발판02끝()


class 발판02끝(state.State):
    def on_enter(self):
        set_timer(timerId='502', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='502'):
            return 대기()


