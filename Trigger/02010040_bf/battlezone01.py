""" trigger/02010040_bf/battlezone01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[4101], visible=False)
        set_effect(triggerIds=[4102], visible=False)
        set_mesh(triggerIds=[1100], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1101], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_actor(triggerId=2100, visible=True, initialSequence='Closed') # door
        set_actor(triggerId=2101, visible=True, initialSequence='Closed') # door
        set_agent(triggerIds=[3101], visible=True)
        set_agent(triggerIds=[3102], visible=True)
        set_agent(triggerIds=[3103], visible=True)
        set_agent(triggerIds=[3104], visible=True)
        set_agent(triggerIds=[3105], visible=True)
        set_agent(triggerIds=[3106], visible=True)
        set_agent(triggerIds=[3107], visible=True)
        set_agent(triggerIds=[3108], visible=True)
        set_agent(triggerIds=[3109], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,104,105,106,107,108,109,201,202,203,204,205,206,207,208,209,210], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105,106,107,108,109,201,202,203,204,205,206,207,208,209,210]):
            return 문열기()


class 문열기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1100], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1101], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_effect(triggerIds=[4101], visible=True)
        set_effect(triggerIds=[4102], visible=True)
        set_actor(triggerId=2100, visible=True, initialSequence='Opened') # door
        set_actor(triggerId=2101, visible=True, initialSequence='Opened') # door
        set_agent(triggerIds=[3101], visible=False)
        set_agent(triggerIds=[3102], visible=False)
        set_agent(triggerIds=[3103], visible=False)
        set_agent(triggerIds=[3104], visible=False)
        set_agent(triggerIds=[3105], visible=False)
        set_agent(triggerIds=[3106], visible=False)
        set_agent(triggerIds=[3107], visible=False)
        set_agent(triggerIds=[3108], visible=False)
        set_agent(triggerIds=[3109], visible=False)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


