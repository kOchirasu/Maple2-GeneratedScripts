""" trigger/02000298_bf/door_15.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=215, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3151], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3152], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9151], visible=True)
        set_agent(triggerIds=[9152], visible=True)
        set_agent(triggerIds=[9153], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[115]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=215, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3151], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3152], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9151], visible=False)
        set_agent(triggerIds=[9152], visible=False)
        set_agent(triggerIds=[9153], visible=False)
        create_monster(spawnIds=[1016], arg2=True)


