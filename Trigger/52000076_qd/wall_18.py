""" trigger/52000076_qd/wall_18.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[118]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[118]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


