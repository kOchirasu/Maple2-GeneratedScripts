""" trigger/02000298_bf/door_08.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=208, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3081], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3082], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9081], visible=True)
        self.set_agent(triggerIds=[9082], visible=True)
        self.set_agent(triggerIds=[9083], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[108]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=208, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3081], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3082], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9081], visible=False)
        self.set_agent(triggerIds=[9082], visible=False)
        self.set_agent(triggerIds=[9083], visible=False)


initial_state = 시작
