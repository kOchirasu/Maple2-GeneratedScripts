""" trigger/99999909/triggerbox_103.xml """
from common import *
import state


class 블록(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3031,3032,3033,3034,3035,3036,3037], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 블록생성()


class 블록생성(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3031,3032,3033,3034,3035,3036,3037], visible=True, meshCount=4, arg4=0, delay=1)


