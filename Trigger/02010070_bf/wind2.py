""" trigger/02010070_bf/wind2.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='wind02', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[999994]):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[50,51,52,53,54,55,56,57,58,59,60,61], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='wind02', value=1):
            return Change(self.ctx)


class Change(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[34,35,36], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[53], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[46], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[59], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[44], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[45], visible=False, arg3=0, delay=0, scale=0)


initial_state = Wait
