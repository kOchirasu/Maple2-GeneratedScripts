""" trigger/02000486_bf/107_text.xml """
from common import *
import state


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9901]):
            return 알림()


class 알림(state.State):
    def on_tick(self) -> state.State:
        if any_one():
            return 텍스트()


class 텍스트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000486_BF__107_TEXT__0$', arg3='4000')

    def on_tick(self) -> state.State:
        if true():
            return None


