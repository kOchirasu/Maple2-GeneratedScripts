""" trigger/02010029_bf/triggercube_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 발판()


class 발판(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 발판숨김()


class 발판숨김(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


