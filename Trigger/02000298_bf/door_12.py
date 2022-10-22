""" trigger/02000298_bf/door_12.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=212, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3121], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3122], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9121], visible=True)
        set_agent(triggerIds=[9122], visible=True)
        set_agent(triggerIds=[9123], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[112]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=212, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3121], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3122], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9121], visible=False)
        set_agent(triggerIds=[9122], visible=False)
        set_agent(triggerIds=[9123], visible=False)
        create_monster(spawnIds=[1013], arg2=True)


