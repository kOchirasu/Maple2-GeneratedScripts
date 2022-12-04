""" trigger/03000104_tw/slime.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=23000005, textId=23000005, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 알림(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
