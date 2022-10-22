""" trigger/61000004_me/trap_03.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000128], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000128], arg2=0):
            set_mesh(triggerIds=[601,602,603,604], visible=False, arg3=0, arg4=0)
            return 완료()


class 완료(state.State):
    def on_enter(self):
        set_timer(timerId='128', seconds=5, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='128'):
            set_mesh(triggerIds=[601,602,603,604], visible=True, arg3=0, arg4=0)
            return 시작()

    def on_exit(self):
        reset_timer(timerId='128')


