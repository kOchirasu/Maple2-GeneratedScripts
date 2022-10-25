""" trigger/63000001_cs/trigger_07.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[307], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[107]):
            return 발판07(self.ctx)


class 발판07(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[307], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[107]):
            return 발판07끝(self.ctx)


class 발판07끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='407', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='407'):
            return 대기(self.ctx)


initial_state = 대기
