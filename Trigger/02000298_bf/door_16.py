""" trigger/02000298_bf/door_16.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=216, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3161], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3162], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9161], visible=True)
        set_agent(triggerIds=[9162], visible=True)
        set_agent(triggerIds=[9163], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[116]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=216, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3161], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3162], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9161], visible=False)
        set_agent(triggerIds=[9162], visible=False)
        set_agent(triggerIds=[9163], visible=False)
        create_monster(spawnIds=[1017], arg2=True)


