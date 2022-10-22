""" trigger/02000298_bf/door_09.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=209, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3091], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3092], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9091], visible=True)
        set_agent(triggerIds=[9092], visible=True)
        set_agent(triggerIds=[9093], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[109]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=209, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3091], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3092], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9091], visible=False)
        set_agent(triggerIds=[9092], visible=False)
        set_agent(triggerIds=[9093], visible=False)


