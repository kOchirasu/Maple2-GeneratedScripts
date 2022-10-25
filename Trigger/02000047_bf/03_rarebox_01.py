""" trigger/02000047_bf/03_rarebox_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 발판01(self.ctx)


class 발판01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[101]):
            return 발판01끝(self.ctx)


class 발판01끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='401', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='401'):
            return 대기(self.ctx)


initial_state = 대기
