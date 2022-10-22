""" trigger/52000014_qd/move_6400.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[6400], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9640]):
            return 침몰01()


class 침몰01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=17)
        set_breakable(triggerIds=[6400], enabled=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


