""" trigger/02000298_bf/door_15.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=215, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3151], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3152], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9151], visible=True)
        self.set_agent(triggerIds=[9152], visible=True)
        self.set_agent(triggerIds=[9153], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[115]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=215, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3151], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3152], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9151], visible=False)
        self.set_agent(triggerIds=[9152], visible=False)
        self.set_agent(triggerIds=[9153], visible=False)
        self.create_monster(spawnIds=[1016], animationEffect=True)


initial_state = 시작
