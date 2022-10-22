""" trigger/80000007_bonus/trigger_09.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[158]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 벽재생()


class 벽재생(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[158]):
            return 대기()


