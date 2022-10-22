""" trigger/52000076_qd/wall_03.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[33001,33002,33003,33004,33005,33006,33007,33008,33009,33010,33011,33012,33013,33014,33015,33016,33017,33018,33019,33020,33021,33022,33023,33024], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[33001,33002,33003,33004,33005,33006,33007,33008,33009,33010,33011,33012,33013,33014,33015,33016,33017,33018,33019,33020,33021,33022,33023,33024], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[103]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


