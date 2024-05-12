""" trigger/63000079_cs/trigger_16.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[316], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[116]):
            return 발판16(self.ctx)


class 발판16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[316], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[116]):
            return 발판16끝(self.ctx)


class 발판16끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='416', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='416'):
            return 대기(self.ctx)


initial_state = 대기
