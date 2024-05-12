""" trigger/52000014_qd/cube_2201.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2201], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[2202], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[2204], visible=True, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[12201], visible=False) # Fire Cast Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92201]):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_effect(trigger_ids=[12201], visible=True) # Fire Cast Sound
        self.set_mesh(trigger_ids=[2201], visible=False, start_delay=0, interval=0, fade=1)
        self.set_mesh(trigger_ids=[2202], visible=False, start_delay=500, interval=0, fade=1)
        self.set_mesh(trigger_ids=[2204], visible=False, start_delay=750, interval=0, fade=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12201], visible=False) # Fire Cast Sound


initial_state = 대기
