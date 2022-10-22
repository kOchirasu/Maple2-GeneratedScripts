""" trigger/02000298_bf/door_04.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=204, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3041], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3042], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9041], visible=True)
        set_agent(triggerIds=[9042], visible=True)
        set_agent(triggerIds=[9043], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=204, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3041], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3042], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9041], visible=False)
        set_agent(triggerIds=[9042], visible=False)
        set_agent(triggerIds=[9043], visible=False)


