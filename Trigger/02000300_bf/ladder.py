""" trigger/02000300_bf/ladder.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000484], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000484], arg2=0):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], visible=True, arg3=0, arg4=0, arg5=5)


