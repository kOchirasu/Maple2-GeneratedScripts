""" trigger/02010026_bf/05_mesh12.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[50004]):
            return 발판01(self.ctx)


class 발판01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5004], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[50004]):
            return 발판01끝(self.ctx)


class 발판01끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
