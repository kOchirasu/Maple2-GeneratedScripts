""" trigger/02000298_bf/door_19.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=219, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3191], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3192], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9191], visible=True)
        self.set_agent(triggerIds=[9192], visible=True)
        self.set_agent(triggerIds=[9193], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[119]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=219, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3191], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3192], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9191], visible=False)
        self.set_agent(triggerIds=[9192], visible=False)
        self.set_agent(triggerIds=[9193], visible=False)
        self.create_monster(spawnIds=[1020], animationEffect=True)


initial_state = 시작
