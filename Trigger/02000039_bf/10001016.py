""" trigger/02000039_bf/10001016.xml """
from common import *
import state


class 오브젝트반응대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001016], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001016], arg2=0):
            return 열림()


class 열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 오브젝트반응대기()


