""" trigger/02000298_bf/door_14.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=214, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3141], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3142], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9141], visible=True)
        set_agent(triggerIds=[9142], visible=True)
        set_agent(triggerIds=[9143], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[114]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=214, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3141], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3142], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9141], visible=False)
        set_agent(triggerIds=[9142], visible=False)
        set_agent(triggerIds=[9143], visible=False)
        create_monster(spawnIds=[1015], arg2=True)


