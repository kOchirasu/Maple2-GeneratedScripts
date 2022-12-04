""" trigger/02020063_bf/interactmachine_5.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002145], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002145], stateValue=0):
            return 재활성대기(self.ctx)


class 재활성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_any_user_additional_effect(boxId=9105, additionalEffectId=99910370, level=1):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
