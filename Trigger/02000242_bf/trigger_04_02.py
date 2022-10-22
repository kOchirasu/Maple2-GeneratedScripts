""" trigger/02000242_bf/trigger_04_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[303], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[703,704], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[402]):
            return 버튼눌림()


class 버튼눌림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[303], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[703,704], visible=False)
        set_timer(timerId='1', seconds=180)


