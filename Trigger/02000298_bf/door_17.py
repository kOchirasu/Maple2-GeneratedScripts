""" trigger/02000298_bf/door_17.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=217, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3171], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3172], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9171], visible=True)
        set_agent(triggerIds=[9172], visible=True)
        set_agent(triggerIds=[9173], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[117]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=217, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3171], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3172], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9171], visible=False)
        set_agent(triggerIds=[9172], visible=False)
        set_agent(triggerIds=[9173], visible=False)
        create_monster(spawnIds=[1018], arg2=True)


