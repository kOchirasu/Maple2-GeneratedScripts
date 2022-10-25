""" trigger/03000087_bf/slime.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 알림(self.ctx)


class 알림(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=23000005, textId=23000005, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 알림(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
