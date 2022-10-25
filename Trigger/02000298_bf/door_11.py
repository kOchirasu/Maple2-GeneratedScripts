""" trigger/02000298_bf/door_11.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=211, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3111], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3112], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9111], visible=True)
        self.set_agent(triggerIds=[9112], visible=True)
        self.set_agent(triggerIds=[9113], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[111]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=211, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3111], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3112], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9111], visible=False)
        self.set_agent(triggerIds=[9112], visible=False)
        self.set_agent(triggerIds=[9113], visible=False)


initial_state = 시작
