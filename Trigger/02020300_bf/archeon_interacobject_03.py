""" trigger/02020300_bf/archeon_interacobject_03.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[901]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002188], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002188], stateValue=0):
            self.set_interact_object(triggerIds=[10002188], state=2)
            return 재활성대기(self.ctx)


class 재활성대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return 시작(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
