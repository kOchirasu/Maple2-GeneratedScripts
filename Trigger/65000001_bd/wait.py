""" trigger/65000001_bd/wait.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='60', seconds=60, clearAtZero=True, display=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 어나운스01()


class 어나운스01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26500201, textId=26500201, duration=4500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 어나운스01()
        if count_users(boxId=101, boxId=2):
            return 종료()
        if time_expired(timerId='60'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=26500201)


class 종료(state.State):
    pass


