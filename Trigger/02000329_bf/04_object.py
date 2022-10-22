""" trigger/02000329_bf/04_object.xml """
from common import *
import state


class 오브젝트_04(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1105,1106,1107,1108]):
            return 오브젝트_04_작동()


class 오브젝트_04_작동(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10001], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 오브젝트_04_작동_메세지()


class 오브젝트_04_작동_메세지(state.State):
    pass


