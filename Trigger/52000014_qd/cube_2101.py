""" trigger/52000014_qd/cube_2101.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2101], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2102], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[12101], visible=False) # Fire Cast Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[92101]):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=5)
        self.set_effect(triggerIds=[12101], visible=True) # Fire Cast Sound
        self.set_mesh(triggerIds=[2101], visible=False, arg3=0, delay=0, scale=1)
        self.set_mesh(triggerIds=[2102], visible=False, arg3=500, delay=0, scale=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[12101], visible=False) # Fire Cast Sound


initial_state = 대기
