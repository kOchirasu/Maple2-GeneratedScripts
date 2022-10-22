""" trigger/02000247_bf/trigger_01_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[401]):
            return 버튼눌림()
        if user_detected(boxIds=[405]):
            return 사라짐()


class 버튼눌림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[401]):
            return 대기()
        if user_detected(boxIds=[405]):
            return 사라짐()


class 사라짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0, arg5=0)


