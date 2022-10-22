""" trigger/02000298_bf/door_03.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=203, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3031], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3032], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9031], visible=True)
        set_agent(triggerIds=[9032], visible=True)
        set_agent(triggerIds=[9033], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=203, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3031], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3032], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9031], visible=False)
        set_agent(triggerIds=[9032], visible=False)
        set_agent(triggerIds=[9033], visible=False)


