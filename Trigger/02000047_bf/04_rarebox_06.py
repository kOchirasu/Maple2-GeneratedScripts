""" trigger/02000047_bf/04_rarebox_06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[406], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[206]):
            return 발판06(self.ctx)


class 발판06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[406], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[206]):
            return 발판06끝(self.ctx)


class 발판06끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='506', seconds=2, start_delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='506'):
            return 대기(self.ctx)


initial_state = 대기
