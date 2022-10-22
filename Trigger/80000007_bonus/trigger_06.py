""" trigger/80000007_bonus/trigger_06.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[155]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 벽재생()


class 벽재생(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[155]):
            return 대기()


