""" trigger/02000471_bf/event_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000471_BF__EVENT_01__0$', arg3='3000')


