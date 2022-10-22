""" trigger/02000298_bf/door_11.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=211, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3111], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3112], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9111], visible=True)
        set_agent(triggerIds=[9112], visible=True)
        set_agent(triggerIds=[9113], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[111]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=211, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3111], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3112], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9111], visible=False)
        set_agent(triggerIds=[9112], visible=False)
        set_agent(triggerIds=[9113], visible=False)


