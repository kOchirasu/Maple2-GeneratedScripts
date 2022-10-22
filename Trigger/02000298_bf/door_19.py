""" trigger/02000298_bf/door_19.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=219, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3191], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3192], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9191], visible=True)
        set_agent(triggerIds=[9192], visible=True)
        set_agent(triggerIds=[9193], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[119]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=219, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3191], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3192], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9191], visible=False)
        set_agent(triggerIds=[9192], visible=False)
        set_agent(triggerIds=[9193], visible=False)
        create_monster(spawnIds=[1020], arg2=True)


