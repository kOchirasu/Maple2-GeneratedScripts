""" trigger/63000089_cs/trigger_14.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[314], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[114]):
            return 발판14(self.ctx)


class 발판14(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[314], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[114]):
            return 발판14끝(self.ctx)


class 발판14끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='414', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='414'):
            return 대기(self.ctx)


initial_state = 대기
