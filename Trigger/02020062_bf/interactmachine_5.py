""" trigger/02020062_bf/interactmachine_5.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002165], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002165], stateValue=0):
            return 재활성대기(self.ctx)


class 재활성대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.check_any_user_additional_effect(boxId=9105, additionalEffectId=99910370, level=1):
            return 시작(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
