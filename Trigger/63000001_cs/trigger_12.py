""" trigger/63000001_cs/trigger_12.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[312], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[112]):
            return 발판12(self.ctx)


class 발판12(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[312], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[112]):
            return 발판12끝(self.ctx)


class 발판12끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='412', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='412'):
            return 대기(self.ctx)


initial_state = 대기
