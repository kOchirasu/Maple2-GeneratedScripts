""" trigger/52000076_qd/wall_07.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[37001,37002,37003,37004,37005,37006,37007,37008,37009,37010,37011,37012,37013,37014,37015,37016,37017,37018,37019], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[37001,37002,37003,37004,37005,37006,37007,37008,37009,37010,37011,37012,37013,37014,37015,37016,37017,37018,37019], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[107]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


