""" trigger/61000010_me/bridge01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000041], state=1)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000041], arg2=0):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110], visible=False, arg3=0, arg4=100, arg5=1)
            return 종료()


class 종료(state.State):
    pass


