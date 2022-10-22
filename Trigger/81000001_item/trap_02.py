""" trigger/81000001_item/trap_02.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000127], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000127], arg2=0):
            set_mesh(triggerIds=[501,502,503,504,505], visible=False, arg3=0, arg4=0)
            return 완료()


class 완료(state.State):
    def on_enter(self):
        set_timer(timerId='127', seconds=5, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='127'):
            set_mesh(triggerIds=[501,502,503,504,505], visible=True, arg3=0, arg4=0)
            return 시작()

    def on_exit(self):
        reset_timer(timerId='127')


