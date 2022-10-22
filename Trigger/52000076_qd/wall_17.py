""" trigger/52000076_qd/wall_17.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719,31720], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[117]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719,31720], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[117]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


