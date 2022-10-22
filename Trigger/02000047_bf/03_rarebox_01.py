""" trigger/02000047_bf/03_rarebox_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 발판01()


class 발판01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 발판01끝()


class 발판01끝(state.State):
    def on_enter(self):
        set_timer(timerId='401', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='401'):
            return 대기()


