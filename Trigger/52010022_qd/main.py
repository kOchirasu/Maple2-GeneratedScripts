""" trigger/52010022_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1003,1004], visible=True, start_delay=0, interval=0, fade=0)


initial_state = idle
