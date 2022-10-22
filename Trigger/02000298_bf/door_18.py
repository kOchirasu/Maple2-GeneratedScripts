""" trigger/02000298_bf/door_18.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=218, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3181], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3182], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9181], visible=True)
        set_agent(triggerIds=[9182], visible=True)
        set_agent(triggerIds=[9183], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[118]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=218, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3181], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3182], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9181], visible=False)
        set_agent(triggerIds=[9182], visible=False)
        set_agent(triggerIds=[9183], visible=False)
        create_monster(spawnIds=[1019], arg2=True)


