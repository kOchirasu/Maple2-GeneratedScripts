""" trigger/52000076_qd/wall_09.xml """
import common


class 벽재생(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[39001,39002,39003,39004,39005,39006,39007,39008,39009,39010,39011,39012,39013,39014,39015,39016,39017,39018,39019], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[109]):
            return 벽삭제(self.ctx)


class 벽삭제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[39001,39002,39003,39004,39005,39006,39007,39008,39009,39010,39011,39012,39013,39014,39015,39016,39017,39018,39019], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[109]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
