""" trigger/02000388_bf/anchor_02.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1505,1506,1507,1508,1509], visible=True, arg3=0, arg4=0, arg5=10)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001098], arg2=0):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1505,1506,1507,1508,1509], visible=False, arg3=0, arg4=0, arg5=10)


