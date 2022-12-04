""" trigger/52000014_qd/move_6100.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[6100], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9610]):
            return 침몰01(self.ctx)


class 침몰01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=17)
        self.set_breakable(triggerIds=[6100], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
