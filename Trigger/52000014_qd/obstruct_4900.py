""" trigger/52000014_qd/obstruct_4900.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[4900], enable=False)
        self.set_effect(triggerIds=[490], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 발동준비(self.ctx)


class 발동준비(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 발동(self.ctx)


class 발동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=3)
        self.set_skill(triggerIds=[4900], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 초기화(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=1)
        self.set_skill(triggerIds=[4900], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 발동준비(self.ctx)


initial_state = 대기
