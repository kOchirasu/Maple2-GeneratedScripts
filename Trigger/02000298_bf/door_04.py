""" trigger/02000298_bf/door_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=204, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3041], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3042], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9041], visible=True)
        self.set_agent(triggerIds=[9042], visible=True)
        self.set_agent(triggerIds=[9043], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=204, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3041], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3042], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9041], visible=False)
        self.set_agent(triggerIds=[9042], visible=False)
        self.set_agent(triggerIds=[9043], visible=False)


initial_state = 시작
