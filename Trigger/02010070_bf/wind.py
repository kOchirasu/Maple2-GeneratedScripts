""" trigger/02010070_bf/wind.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='wind01', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999994]):
            return Start()


class Start(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='wind01', value=1):
            return Change()


class Change(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[30], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[31], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[50], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[49], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[56], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[39], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[40], visible=False, arg3=0, arg4=0, arg5=0)


