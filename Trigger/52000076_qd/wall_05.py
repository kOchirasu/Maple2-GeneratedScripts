""" trigger/52000076_qd/wall_05.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[35001,35002,35003,35004,35005,35006,35007,35008,35009,35010,35011,35012,35013,35014,35015,35016,35017,35018,35019,35020], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[35001,35002,35003,35004,35005,35006,35007,35008,35009,35010,35011,35012,35013,35014,35015,35016,35017,35018,35019,35020], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[105]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
