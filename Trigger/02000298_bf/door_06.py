""" trigger/02000298_bf/door_06.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=206, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3061], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3062], visible=True, arg3=0, delay=0, scale=0)
        self.set_agent(triggerIds=[9061], visible=True)
        self.set_agent(triggerIds=[9062], visible=True)
        self.set_agent(triggerIds=[9063], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[106]):
            return 문열림(self.ctx)


class 문열림(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=206, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3061], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3062], visible=False, arg3=0, delay=0, scale=5)
        self.set_agent(triggerIds=[9061], visible=False)
        self.set_agent(triggerIds=[9062], visible=False)
        self.set_agent(triggerIds=[9063], visible=False)


initial_state = 시작
