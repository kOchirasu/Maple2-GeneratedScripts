""" trigger/02000329_bf/02_object.xml """
from common import *
import state


class 오브젝트_01(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[10001], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 오브젝트_01_작동()


class 오브젝트_01_작동(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[10001], enabled=True)


