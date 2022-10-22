""" trigger/02000252_bf/water_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108], visible=False, arg3=0, arg4=100)
        set_interact_object(triggerIds=[10000409], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000409], arg2=0):
            return 물()


class 물(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108], visible=True, arg3=0, arg4=250)


