""" trigger/63000089_cs/trigger_06.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[306], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[106]):
            return 발판06(self.ctx)


class 발판06(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[306], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[106]):
            return 발판06끝(self.ctx)


class 발판06끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='406', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='406'):
            return 대기(self.ctx)


initial_state = 대기
