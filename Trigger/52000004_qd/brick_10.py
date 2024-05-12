""" trigger/52000004_qd/brick_10.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3110], visible=True, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[120]):
            return 발판01(self.ctx)


class 발판01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.set_mesh(trigger_ids=[3110], visible=False, start_delay=0, interval=0, fade=0)
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 대기(self.ctx)


initial_state = 대기
