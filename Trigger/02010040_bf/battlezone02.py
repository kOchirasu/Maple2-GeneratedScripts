""" trigger/02010040_bf/battlezone02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[4201], visible=False)
        set_effect(triggerIds=[4202], visible=False)
        set_mesh(triggerIds=[1200], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1201], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_actor(triggerId=2200, visible=True, initialSequence='Closed') # door
        set_actor(triggerId=2201, visible=True, initialSequence='Closed') # door
        set_agent(triggerIds=[3201], visible=True)
        set_agent(triggerIds=[3202], visible=True)
        set_agent(triggerIds=[3203], visible=True)
        set_agent(triggerIds=[3204], visible=True)
        set_agent(triggerIds=[3205], visible=True)
        set_agent(triggerIds=[3206], visible=True)
        set_agent(triggerIds=[3207], visible=True)
        set_agent(triggerIds=[3208], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301,302,303,304,305,306,401,402,403,404,405,406,407,408], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[301,302,303,304,305,306,401,402,403,404,405,406,407,408]):
            return 문열기()


class 문열기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1200], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1201], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_effect(triggerIds=[4201], visible=True)
        set_effect(triggerIds=[4202], visible=True)
        set_actor(triggerId=2200, visible=True, initialSequence='Opened') # door
        set_actor(triggerId=2201, visible=True, initialSequence='Opened') # door
        set_agent(triggerIds=[3201], visible=False)
        set_agent(triggerIds=[3202], visible=False)
        set_agent(triggerIds=[3203], visible=False)
        set_agent(triggerIds=[3204], visible=False)
        set_agent(triggerIds=[3205], visible=False)
        set_agent(triggerIds=[3206], visible=False)
        set_agent(triggerIds=[3207], visible=False)
        set_agent(triggerIds=[3208], visible=False)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)


