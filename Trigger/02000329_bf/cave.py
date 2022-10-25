""" trigger/02000329_bf/cave.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[711]):
            return 동굴전환시작(self.ctx)


class 동굴전환시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6701], visible=False)


initial_state = 대기
