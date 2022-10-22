""" trigger/02000298_bf/door_07.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=207, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3071], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3072], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9071], visible=True)
        set_agent(triggerIds=[9072], visible=True)
        set_agent(triggerIds=[9073], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=207, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3071], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3072], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9071], visible=False)
        set_agent(triggerIds=[9072], visible=False)
        set_agent(triggerIds=[9073], visible=False)


