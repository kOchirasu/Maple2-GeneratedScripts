""" trigger/02010051_bf/soundeffect05.xml """
import trigger_api


class 대기01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[900], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 음성연출(self.ctx)


class 음성연출(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)
        self.set_effect(triggerIds=[900], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기02(self.ctx)


class 대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10000]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[900], visible=False)


initial_state = 대기01
