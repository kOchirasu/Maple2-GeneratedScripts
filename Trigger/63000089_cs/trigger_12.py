""" trigger/63000089_cs/trigger_12.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[312], visible=False, start_delay=0, interval=0, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[112]):
            return 발판12(self.ctx)


class 발판12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[312], visible=True, start_delay=0, interval=0, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[112]):
            return 발판12끝(self.ctx)


class 발판12끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='412', seconds=2, start_delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='412'):
            return 대기(self.ctx)


initial_state = 대기
