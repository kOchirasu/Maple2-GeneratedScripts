""" trigger/02000298_bf/door_07.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=207, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3071], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3072], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9071], visible=True)
        self.set_agent(triggerIds=[9072], visible=True)
        self.set_agent(triggerIds=[9073], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[107]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=207, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3071], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3072], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9071], visible=False)
        self.set_agent(triggerIds=[9072], visible=False)
        self.set_agent(triggerIds=[9073], visible=False)


initial_state = 시작
