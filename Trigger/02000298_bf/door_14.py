""" trigger/02000298_bf/door_14.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=214, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3141], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3142], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9141], visible=True)
        self.set_agent(triggerIds=[9142], visible=True)
        self.set_agent(triggerIds=[9143], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[114]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=214, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3141], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3142], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9141], visible=False)
        self.set_agent(triggerIds=[9142], visible=False)
        self.set_agent(triggerIds=[9143], visible=False)
        self.create_monster(spawnIds=[1015], animationEffect=True)


initial_state = 시작
