""" trigger/02000298_bf/door_01.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3011], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3012], visible=True, arg3=0, arg4=0, arg5=0)
        set_agent(triggerIds=[9011], visible=True)
        set_agent(triggerIds=[9012], visible=True)
        set_agent(triggerIds=[9013], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        set_mesh(triggerIds=[3011], visible=False, arg3=0, arg4=0, arg5=5)
        set_mesh(triggerIds=[3012], visible=False, arg3=0, arg4=0, arg5=5)
        set_agent(triggerIds=[9011], visible=False)
        set_agent(triggerIds=[9012], visible=False)
        set_agent(triggerIds=[9013], visible=False)


