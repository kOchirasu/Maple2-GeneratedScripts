""" trigger/02000312_bf/magictree_05.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001029], state=1)
        self.set_mesh(triggerIds=[1040,1041,1042,1043,1044], visible=True, arg3=0, delay=0, scale=0) # 덩굴

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001029], stateValue=0):
            return Remove(self.ctx)


class Remove(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001029], state=0)
        self.set_random_mesh(triggerIds=[1040,1041,1042,1043,1044], visible=False, meshCount=5, arg4=500, delay=100) # 덩굴
        self.set_user_value(triggerId=10, key='4thTreeRemove', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
