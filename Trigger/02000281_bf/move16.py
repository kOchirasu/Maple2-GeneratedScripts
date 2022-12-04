""" trigger/02000281_bf/move16.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[816], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[196]):
            return 발판발동(self.ctx)


class 발판발동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30, startDelay=0)
        self.set_breakable(triggerIds=[816], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            return 대기(self.ctx)


initial_state = 대기
