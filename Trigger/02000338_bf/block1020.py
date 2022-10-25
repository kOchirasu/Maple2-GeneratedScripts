""" trigger/02000338_bf/block1020.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1020], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10020]):
            return 준비(self.ctx)


class 준비(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 진행1(self.ctx)


class 진행1(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1020], visible=False, arg3=0, delay=0, scale=2)


initial_state = 대기
