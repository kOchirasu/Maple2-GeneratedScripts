""" trigger/99999909/triggerbox_102.xml """
from common import *
import state


class 블록(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 블록생성()


class 블록생성(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028], visible=True, meshCount=6, arg4=0, delay=1)


