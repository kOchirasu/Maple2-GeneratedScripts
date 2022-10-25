""" trigger/63000079_cs/trigger_17.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[317], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[117]):
            return 발판17(self.ctx)


class 발판17(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[317], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[117]):
            return 발판17끝(self.ctx)


class 발판17끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='417', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='417'):
            return 대기(self.ctx)


initial_state = 대기
