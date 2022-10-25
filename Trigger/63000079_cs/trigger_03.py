""" trigger/63000079_cs/trigger_03.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[303], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 발판03(self.ctx)


class 발판03(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[303], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[103]):
            return 발판03끝(self.ctx)


class 발판03끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='403', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='403'):
            return 대기(self.ctx)


initial_state = 대기
