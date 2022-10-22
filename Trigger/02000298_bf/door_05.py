""" trigger/02000298_bf/door_05.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=205, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3051], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3052], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9051], visible=True)
        set_agent(triggerIds=[9052], visible=True)
        set_agent(triggerIds=[9053], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=205, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3051], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3052], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9051], visible=False)
        set_agent(triggerIds=[9052], visible=False)
        set_agent(triggerIds=[9053], visible=False)


