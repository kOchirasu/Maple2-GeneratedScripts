""" trigger/63000079_cs/trigger_11.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[311], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[111]):
            return 발판11(self.ctx)


class 발판11(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[311], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[111]):
            return 발판11끝(self.ctx)


class 발판11끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='411', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='411'):
            return 대기(self.ctx)


initial_state = 대기
