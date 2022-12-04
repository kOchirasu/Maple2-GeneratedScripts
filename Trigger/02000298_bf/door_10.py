""" trigger/02000298_bf/door_10.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=210, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3101], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3102], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9101], visible=True)
        self.set_agent(triggerIds=[9102], visible=True)
        self.set_agent(triggerIds=[9103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[110]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=210, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3101], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3102], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9101], visible=False)
        self.set_agent(triggerIds=[9102], visible=False)
        self.set_agent(triggerIds=[9103], visible=False)


initial_state = 시작
