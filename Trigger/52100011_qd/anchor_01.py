""" trigger/52100011_qd/anchor_01.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1500,1501,1502,1503,1504], visible=True, arg3=0, arg4=0, arg5=10)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002055], arg2=0):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1500,1501,1502,1503,1504], visible=False, arg3=0, arg4=0, arg5=10)


