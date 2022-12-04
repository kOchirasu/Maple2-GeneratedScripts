""" trigger/63000079_cs/trigger_10.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[310], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[110]):
            return 발판10(self.ctx)


class 발판10(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[310], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[110]):
            return 발판10끝(self.ctx)


class 발판10끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='410', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='410'):
            return 대기(self.ctx)


initial_state = 대기
