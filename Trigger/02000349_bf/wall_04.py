""" trigger/02000349_bf/wall_04.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[34001,34002,34003,34004,34005,34006,34007,34008,34009,34010,34011,34012,34013,34014,34015,34016,34017,34018,34019,34020,34021,34022,34023,34024,34025,34026,34027], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[34001,34002,34003,34004,34005,34006,34007,34008,34009,34010,34011,34012,34013,34014,34015,34016,34017,34018,34019,34020,34021,34022,34023,34024,34025,34026,34027], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[104]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
