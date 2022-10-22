""" trigger/02000047_bf/04_rarebox_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[403], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[203]):
            return 발판03()


class 발판03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[403], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[203]):
            return 발판03끝()


class 발판03끝(state.State):
    def on_enter(self):
        set_timer(timerId='503', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='503'):
            return 대기()


