""" trigger/02000047_bf/04_rarebox_05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[405], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[205]):
            return 발판05(self.ctx)


class 발판05(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[405], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[205]):
            return 발판05끝(self.ctx)


class 발판05끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='505', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='505'):
            return 대기(self.ctx)


initial_state = 대기
