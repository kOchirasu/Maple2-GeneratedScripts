""" trigger/52000014_qd/collapse_2700.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2700,2701,2702,2703,2704,2705,2706], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[12700], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22700], visible=False) # Vibrate Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[92700]):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=10)
        self.set_effect(triggerIds=[12700], visible=True) # Vibrate Short
        self.set_effect(triggerIds=[22700], visible=True) # Vibrate Sound
        self.set_random_mesh(triggerIds=[2700,2701,2702,2703,2704,2705,2706], visible=False, meshCount=7, arg4=300, delay=300)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[12700], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22700], visible=False) # Vibrate Sound


initial_state = 대기
