""" trigger/63000089_cs/trigger_hint.xml """
from common import *
import state


class 힌트(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818], visible=True, meshCount=2, arg4=0, delay=1000)
        set_timer(timerId='99', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818], visible=False)
        set_timer(timerId='41', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='41'):
            return 힌트()


