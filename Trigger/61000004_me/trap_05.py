""" trigger/61000004_me/trap_05.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000130], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000130], arg2=0):
            set_mesh(triggerIds=[801,802,803,804,805,806], visible=False, arg3=0, arg4=0)
            return 완료()


class 완료(state.State):
    def on_enter(self):
        set_timer(timerId='130', seconds=5, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='130'):
            set_mesh(triggerIds=[801,802,803,804,805,806], visible=True, arg3=0, arg4=0)
            return 시작()

    def on_exit(self):
        reset_timer(timerId='130')


