""" trigger/02000298_bf/door_13.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=213, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3131], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3132], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9131], visible=True)
        self.set_agent(triggerIds=[9132], visible=True)
        self.set_agent(triggerIds=[9133], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[113]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=213, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3131], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3132], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9131], visible=False)
        self.set_agent(triggerIds=[9132], visible=False)
        self.set_agent(triggerIds=[9133], visible=False)
        self.create_monster(spawnIds=[1014], animationEffect=True)


initial_state = 시작
