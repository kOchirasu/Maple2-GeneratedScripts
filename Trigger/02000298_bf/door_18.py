""" trigger/02000298_bf/door_18.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=218, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3181], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3182], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9181], visible=True)
        self.set_agent(triggerIds=[9182], visible=True)
        self.set_agent(triggerIds=[9183], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[118]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=218, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3181], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3182], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9181], visible=False)
        self.set_agent(triggerIds=[9182], visible=False)
        self.set_agent(triggerIds=[9183], visible=False)
        self.create_monster(spawnIds=[1019], animationEffect=True)


initial_state = 시작
