""" trigger/99999909/triggerbox_101.xml """
from common import *
import state


class 블록(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 블록생성()


class 블록생성(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008,3009], visible=True, meshCount=4, arg4=0, delay=1)


