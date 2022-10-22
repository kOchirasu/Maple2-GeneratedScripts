""" trigger/61000003_me_003/wait.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='60', seconds=60, clearAtZero=True, display=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=26100001, textId=26100001)

    def on_tick(self) -> state.State:
        if count_users(boxId=100, boxId=50):
            return 종료()
        if wait_tick(waitTick=5000):
            return 대기2()
        if time_expired(timerId='60'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=26100001)


class 대기2(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100002, textId=26100002)

    def on_tick(self) -> state.State:
        if count_users(boxId=100, boxId=50):
            return 종료()
        if wait_tick(waitTick=5000):
            return 대기()
        if time_expired(timerId='60'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=26100002)


class 종료(state.State):
    pass


