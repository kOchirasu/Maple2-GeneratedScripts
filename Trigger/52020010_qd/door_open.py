""" trigger/52020010_qd/door_open.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5016], visible=False) # 우르르 쾅쾅
        set_effect(triggerIds=[5017], visible=False) # 먼지
        set_breakable(triggerIds=[10001], enabled=False)
        set_breakable(triggerIds=[10002], enabled=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[2]):
            return Check()
        if quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[3]):
            return Check()


class Check(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001275], arg2=0):
            return DoorOpen()


class DoorOpen(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5016], visible=True) # 우르르 쾅쾅
        set_effect(triggerIds=[5017], visible=True) # 먼지
        set_breakable(triggerIds=[10001], enabled=True)
        set_breakable(triggerIds=[10002], enabled=True)


