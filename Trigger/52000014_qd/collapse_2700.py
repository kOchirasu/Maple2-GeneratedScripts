""" trigger/52000014_qd/collapse_2700.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2700,2701,2702,2703,2704,2705,2706], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[12700], visible=False) # Vibrate Short
        set_effect(triggerIds=[22700], visible=False) # Vibrate Sound

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[92700]):
            return 무너짐01()


class 무너짐01(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=10)
        set_effect(triggerIds=[12700], visible=True) # Vibrate Short
        set_effect(triggerIds=[22700], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2700,2701,2702,2703,2704,2705,2706], visible=False, meshCount=7, arg4=300, delay=300)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12700], visible=False) # Vibrate Short
        set_effect(triggerIds=[22700], visible=False) # Vibrate Sound


