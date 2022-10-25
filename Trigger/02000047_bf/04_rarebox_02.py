""" trigger/02000047_bf/04_rarebox_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[402], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[202]):
            return 발판02(self.ctx)


class 발판02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[402], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[202]):
            return 발판02끝(self.ctx)


class 발판02끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='502', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='502'):
            return 대기(self.ctx)


initial_state = 대기
