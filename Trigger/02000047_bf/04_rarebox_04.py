""" trigger/02000047_bf/04_rarebox_04.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[404], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[204]):
            return 발판04(self.ctx)


class 발판04(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[404], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[204]):
            return 발판04끝(self.ctx)


class 발판04끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='504', seconds=2, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='504'):
            return 대기(self.ctx)


initial_state = 대기
