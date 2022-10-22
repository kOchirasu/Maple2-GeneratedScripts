""" trigger/02000298_bf/door_06.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=206, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3061], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3062], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9061], visible=True)
        set_agent(triggerIds=[9062], visible=True)
        set_agent(triggerIds=[9063], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=206, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3061], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3062], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9061], visible=False)
        set_agent(triggerIds=[9062], visible=False)
        set_agent(triggerIds=[9063], visible=False)


