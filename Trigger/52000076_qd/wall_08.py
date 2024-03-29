""" trigger/52000076_qd/wall_08.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[38001,38002,38003,38004,38005,38006,38007,38008,38009,38010,38011,38012,38013,38014,38015,38016,38017,38018,38019,38020,38021,38022], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[108]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[38001,38002,38003,38004,38005,38006,38007,38008,38009,38010,38011,38012,38013,38014,38015,38016,38017,38018,38019,38020,38021,38022], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[108]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
