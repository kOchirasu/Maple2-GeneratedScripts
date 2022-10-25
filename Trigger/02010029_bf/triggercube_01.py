""" trigger/02010029_bf/triggercube_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 발판(self.ctx)


class 발판(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 발판숨김(self.ctx)


class 발판숨김(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


initial_state = 대기
