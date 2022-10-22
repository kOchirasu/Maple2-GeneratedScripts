""" trigger/02000298_bf/door_10.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=210, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3101], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3102], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9101], visible=True)
        set_agent(triggerIds=[9102], visible=True)
        set_agent(triggerIds=[9103], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[110]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=210, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3101], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3102], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9101], visible=False)
        set_agent(triggerIds=[9102], visible=False)
        set_agent(triggerIds=[9103], visible=False)


