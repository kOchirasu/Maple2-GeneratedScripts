""" trigger/02010070_bf/wind2.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='wind02', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999994]):
            return Start()


class Start(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[50,51,52,53,54,55,56,57,58,59,60,61], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='wind02', value=1):
            return Change()


class Change(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[34,35,36], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[53], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[46], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[59], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[44], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[45], visible=False, arg3=0, arg4=0, arg5=0)


