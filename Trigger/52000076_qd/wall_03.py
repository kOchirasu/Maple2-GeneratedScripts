""" trigger/52000076_qd/wall_03.xml """
import common


class 벽재생(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[33001,33002,33003,33004,33005,33006,33007,33008,33009,33010,33011,33012,33013,33014,33015,33016,33017,33018,33019,33020,33021,33022,33023,33024], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 벽삭제(self.ctx)


class 벽삭제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[33001,33002,33003,33004,33005,33006,33007,33008,33009,33010,33011,33012,33013,33014,33015,33016,33017,33018,33019,33020,33021,33022,33023,33024], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[103]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
