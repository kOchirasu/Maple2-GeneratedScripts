""" trigger/63000001_cs/trigger_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[302], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 발판02(self.ctx)


class 발판02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[302], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[102]):
            return 발판02끝(self.ctx)


class 발판02끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='402', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='402'):
            return 대기(self.ctx)


initial_state = 대기
