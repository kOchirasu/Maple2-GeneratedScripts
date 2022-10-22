""" trigger/02000133_ad/board.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000346], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000346], arg2=0):
            return 어나운스()


class 어나운스(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000133_AD__BOARD__0$', arg3='4000', arg4='101')
        set_timer(timerId='5', seconds=5, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 대기()


