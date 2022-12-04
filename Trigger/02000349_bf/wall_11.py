""" trigger/02000349_bf/wall_11.xml """
import trigger_api


class 벽재생(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31101,31102,31103,31104,31105,31106,31107,31108,31109,31110,31111,31112,31113,31114,31115,31116,31117,31118,31119,31120,31121,31122], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[111]):
            return 벽삭제(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31101,31102,31103,31104,31105,31106,31107,31108,31109,31110,31111,31112,31113,31114,31115,31116,31117,31118,31119,31120,31121,31122], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[111]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
