""" trigger/02010026_bf/05_mesh12.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[50004]):
            return 발판01(self.ctx)


class 발판01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[50004]):
            return 발판01끝(self.ctx)


class 발판01끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2, start_delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
