""" trigger/02000298_bf/door_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=202, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3021], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3022], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9021], visible=True)
        self.set_agent(triggerIds=[9022], visible=True)
        self.set_agent(triggerIds=[9023], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=202, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3021], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3022], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9021], visible=False)
        self.set_agent(triggerIds=[9022], visible=False)
        self.set_agent(triggerIds=[9023], visible=False)


initial_state = 시작
