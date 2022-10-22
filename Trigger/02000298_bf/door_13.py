""" trigger/02000298_bf/door_13.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=213, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3131], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3132], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9131], visible=True)
        set_agent(triggerIds=[9132], visible=True)
        set_agent(triggerIds=[9133], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[113]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=213, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3131], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3132], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9131], visible=False)
        set_agent(triggerIds=[9132], visible=False)
        set_agent(triggerIds=[9133], visible=False)
        create_monster(spawnIds=[1014], arg2=True)


