""" trigger/02000241_bf/trigger_04_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[308], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[408]):
            return 버튼눌림()


class 버튼눌림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[308], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[707,708], visible=False)
        set_mesh(triggerIds=[309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324], visible=False)


