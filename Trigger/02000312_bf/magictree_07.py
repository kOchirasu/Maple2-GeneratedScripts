""" trigger/02000312_bf/magictree_07.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001031], state=1)
        self.set_mesh(triggerIds=[1060,1061,1062], visible=True, arg3=0, delay=0, scale=0) # 덩굴

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001031], stateValue=0):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001031], state=0)
        self.set_random_mesh(triggerIds=[1060,1061,1062], visible=False, meshCount=3, arg4=500, delay=100) # 덩굴
        self.set_user_value(triggerId=10, key='6thTreeRemove', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
