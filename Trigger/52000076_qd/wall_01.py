""" trigger/52000076_qd/wall_01.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017,31018,31019,31020,31021,31022,31023,31024], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017,31018,31019,31020,31021,31022,31023,31024], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


