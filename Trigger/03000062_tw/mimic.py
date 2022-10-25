""" trigger/03000062_tw/mimic.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 알림(self.ctx)


class 알림(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=23000006, textId=23000006, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 알림(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
