""" trigger/02000047_bf/04_rarebox_06.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[406], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[206]):
            return 발판06()


class 발판06(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[406], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[206]):
            return 발판06끝()


class 발판06끝(state.State):
    def on_enter(self):
        set_timer(timerId='506', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='506'):
            return 대기()


