""" trigger/02000047_bf/04_rarebox_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[403], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[203]):
            return 발판03(self.ctx)


class 발판03(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[403], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[203]):
            return 발판03끝(self.ctx)


class 발판03끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='503', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='503'):
            return 대기(self.ctx)


initial_state = 대기
