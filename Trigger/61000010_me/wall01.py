""" trigger/61000010_me/wall01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000042], state=1)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000042], arg2=0):
            set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=True, arg3=0, arg4=0, arg5=0)
            return 쿨타임()


class 쿨타임(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class 종료(state.State):
    pass


