""" trigger/80000007_bonus/trigger_08.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[157]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 벽재생()


class 벽재생(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[157]):
            return 대기()


