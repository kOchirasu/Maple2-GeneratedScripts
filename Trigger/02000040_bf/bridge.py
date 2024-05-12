""" trigger/02000040_bf/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302,303], visible=False, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10000319], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000319], state=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302,303], visible=True, start_delay=0, interval=500, fade=2)
        self.set_timer(timer_id='3', seconds=3, start_delay=0, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[303,302,301], visible=False, start_delay=0, interval=500, fade=2)
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10, start_delay=0, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 대기(self.ctx)


initial_state = 대기
