""" trigger/03000086_bf/mimic.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=23000006, text_id=23000006, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 알림(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
