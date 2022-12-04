""" trigger/63000089_cs/trigger_18.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[318], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[118]):
            return 발판18(self.ctx)


class 발판18(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[318], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[118]):
            return 발판18끝(self.ctx)


class 발판18끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='418', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='418'):
            return 대기(self.ctx)


initial_state = 대기
