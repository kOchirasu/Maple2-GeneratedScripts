""" trigger/02000298_bf/door_02.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=202, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3021], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3022], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9021], visible=True)
        set_agent(triggerIds=[9022], visible=True)
        set_agent(triggerIds=[9023], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=202, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3021], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3022], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9021], visible=False)
        set_agent(triggerIds=[9022], visible=False)
        set_agent(triggerIds=[9023], visible=False)

