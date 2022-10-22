""" trigger/02000175_bf/triggercube_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[304], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 발판()


class 발판(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[304], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[104]):
            return 발판숨김()


class 발판숨김(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


