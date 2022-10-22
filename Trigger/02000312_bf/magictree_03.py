""" trigger/02000312_bf/magictree_03.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001027], state=1)
        set_mesh(triggerIds=[1020,1021,1022,1023,1024], visible=True, arg3=0, arg4=0, arg5=0) # 덩굴

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001027], arg2=0):
            return Remove()


class Remove(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001027], state=0)
        set_random_mesh(triggerIds=[1020,1021,1022,1023,1024], visible=False, meshCount=5, arg4=500, delay=100) # 덩굴
        set_user_value(triggerId=10, key='2ndTreeRemove', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


