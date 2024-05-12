""" trigger/63000079_cs/trigger_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[302], visible=False, start_delay=0, interval=0, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 발판02(self.ctx)


class 발판02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[302], visible=True, start_delay=0, interval=0, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[102]):
            return 발판02끝(self.ctx)


class 발판02끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='402', seconds=2, start_delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='402'):
            return 대기(self.ctx)


initial_state = 대기
