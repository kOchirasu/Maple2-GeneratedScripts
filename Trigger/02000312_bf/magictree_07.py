""" trigger/02000312_bf/magictree_07.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001031], state=1)
        set_mesh(triggerIds=[1060,1061,1062], visible=True, arg3=0, arg4=0, arg5=0) # 덩굴

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001031], arg2=0):
            return Remove()


class Remove(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001031], state=0)
        set_random_mesh(triggerIds=[1060,1061,1062], visible=False, meshCount=3, arg4=500, delay=100) # 덩굴
        set_user_value(triggerId=10, key='6thTreeRemove', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


