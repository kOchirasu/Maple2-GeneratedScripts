""" trigger/80000007_bonus/trigger_15.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[302]):
            return 막힘(self.ctx)


class 막힘(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[410,411,412,413,414,415,416,417,418], visible=False)


initial_state = 대기
