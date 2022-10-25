""" trigger/02000066_bf/reward.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[11000011], state=2)
        self.set_interact_object(triggerIds=[11000012], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return None # Missing State: 생성조건


initial_state = 시작
