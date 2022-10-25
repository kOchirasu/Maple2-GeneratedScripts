""" trigger/02000298_bf/door_16.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=216, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3161], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3162], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9161], visible=True)
        self.set_agent(triggerIds=[9162], visible=True)
        self.set_agent(triggerIds=[9163], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[116]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=216, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3161], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3162], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9161], visible=False)
        self.set_agent(triggerIds=[9162], visible=False)
        self.set_agent(triggerIds=[9163], visible=False)
        self.create_monster(spawnIds=[1017], animationEffect=True)


initial_state = 시작
