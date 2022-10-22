""" trigger/02000349_bf/wall_09.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[39001,39002,39003,39004,39005,39006,39007,39008,39009,39010,39011,39012,39013,39014,39015,39016,39017,39018,39019], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[109]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[39001,39002,39003,39004,39005,39006,39007,39008,39009,39010,39011,39012,39013,39014,39015,39016,39017,39018,39019], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[109]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


