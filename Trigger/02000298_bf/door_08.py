""" trigger/02000298_bf/door_08.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=208, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3081], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3082], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9081], visible=True)
        set_agent(triggerIds=[9082], visible=True)
        set_agent(triggerIds=[9083], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[108]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=208, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3081], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3082], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9081], visible=False)
        set_agent(triggerIds=[9082], visible=False)
        set_agent(triggerIds=[9083], visible=False)


