""" trigger/52000076_qd/wall_06.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[36001,36002,36003,36004,36005,36006,36007,36008,36009,36010,36011,36012,36013,36014,36015,36016,36017,36018,36019,36020,36021], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[36001,36002,36003,36004,36005,36006,36007,36008,36009,36010,36011,36012,36013,36014,36015,36016,36017,36018,36019,36020,36021], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[106]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


