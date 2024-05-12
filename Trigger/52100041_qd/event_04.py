""" trigger/52100041_qd/event_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1803], visible=True, start_delay=0, interval=200, fade=0)
        self.set_mesh(trigger_ids=[1804], visible=False, start_delay=0, interval=200, fade=0)
        self.set_mesh(trigger_ids=[1805], visible=False, start_delay=0, interval=200, fade=0)
        self.set_mesh(trigger_ids=[1806], visible=False, start_delay=0, interval=200, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1803], visible=False, start_delay=0, interval=200, fade=85)
        self.set_mesh(trigger_ids=[1804], visible=True, start_delay=0, interval=200, fade=85)
        self.set_mesh(trigger_ids=[1805], visible=False, start_delay=0, interval=200, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Ready_02(self.ctx)


class Ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1803], visible=False, start_delay=0, interval=200, fade=5)
        self.set_mesh(trigger_ids=[1804], visible=True, start_delay=0, interval=200, fade=5)
        self.set_mesh(trigger_ids=[1806], visible=True, start_delay=0, interval=200, fade=5)
        # self.set_achievement(trigger_id=705, type='trigger', achieve='Hauntedmansion')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ready_03(self.ctx)


class Ready_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1806], visible=False, start_delay=0, interval=200, fade=5)


initial_state = idle
