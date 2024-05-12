""" trigger/02000298_bf/door_17.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=217, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3171], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3172], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9171], visible=True)
        self.set_agent(triggerIds=[9172], visible=True)
        self.set_agent(triggerIds=[9173], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[117]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=217, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3171], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3172], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9171], visible=False)
        self.set_agent(triggerIds=[9172], visible=False)
        self.set_agent(triggerIds=[9173], visible=False)
        self.create_monster(spawnIds=[1018], animationEffect=True)


initial_state = 시작
