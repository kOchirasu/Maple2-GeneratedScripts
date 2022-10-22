""" trigger/02000349_bf/wall_08.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[38001,38002,38003,38004,38005,38006,38007,38008,38009,38010,38011,38012,38013,38014,38015,38016,38017,38018,38019,38020,38021,38022], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[108]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[38001,38002,38003,38004,38005,38006,38007,38008,38009,38010,38011,38012,38013,38014,38015,38016,38017,38018,38019,38020,38021,38022], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[108]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


