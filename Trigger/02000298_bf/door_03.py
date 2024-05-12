""" trigger/02000298_bf/door_03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=203, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3031], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3032], visible=True, start_delay=0, interval=0, fade=0)
        self.set_agent(trigger_ids=[9031], visible=True)
        self.set_agent(trigger_ids=[9032], visible=True)
        self.set_agent(trigger_ids=[9033], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=203, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3031], visible=False, start_delay=0, interval=0, fade=5)
        self.set_mesh(trigger_ids=[3032], visible=False, start_delay=0, interval=0, fade=5)
        self.set_agent(trigger_ids=[9031], visible=False)
        self.set_agent(trigger_ids=[9032], visible=False)
        self.set_agent(trigger_ids=[9033], visible=False)


initial_state = 시작
