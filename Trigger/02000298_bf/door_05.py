""" trigger/02000298_bf/door_05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=205, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3051], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3052], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9051], visible=True)
        self.set_agent(triggerIds=[9052], visible=True)
        self.set_agent(triggerIds=[9053], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=205, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3051], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3052], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9051], visible=False)
        self.set_agent(triggerIds=[9052], visible=False)
        self.set_agent(triggerIds=[9053], visible=False)


initial_state = 시작
