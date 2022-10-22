""" trigger/80000007_bonus/trigger_15.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[302]):
            return 막힘()


class 막힘(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[410,411,412,413,414,415,416,417,418], visible=False)


