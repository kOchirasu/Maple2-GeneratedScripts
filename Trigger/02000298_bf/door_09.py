""" trigger/02000298_bf/door_09.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=209, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3091], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3092], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9091], visible=True)
        self.set_agent(triggerIds=[9092], visible=True)
        self.set_agent(triggerIds=[9093], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[109]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=209, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3091], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3092], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9091], visible=False)
        self.set_agent(triggerIds=[9092], visible=False)
        self.set_agent(triggerIds=[9093], visible=False)


initial_state = 시작
