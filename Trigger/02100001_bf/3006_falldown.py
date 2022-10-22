""" trigger/02100001_bf/3006_falldown.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3006], visible=True, arg3=0, arg4=0, arg5=0) # 투명 발판

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9006]):
            return RemoveMesh()


class RemoveMesh(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3006], visible=False, arg3=0, arg4=0, arg5=0) # 투명 발판

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9006]):
            return Wait()


