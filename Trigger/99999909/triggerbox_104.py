""" trigger/99999909/triggerbox_104.xml """
from common import *
import state


class 블록(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3038,3039,3040,3041,3042,3043,3044,3045,3046], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 블록생성()


class 블록생성(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3038,3039,3040,3041,3042,3043,3044,3045,3046], visible=True, meshCount=4, arg4=0, delay=1)


