""" trigger/52010022_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1003,1004], visible=True, arg3=0, arg4=0, arg5=0)


