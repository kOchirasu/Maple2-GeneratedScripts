""" trigger/02010040_bf/battlezone03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[4301], visible=False)
        set_effect(triggerIds=[4302], visible=False)
        set_effect(triggerIds=[4303], visible=False)
        set_mesh(triggerIds=[1300], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1301], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1302], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_actor(triggerId=2300, visible=True, initialSequence='Closed') # door
        set_actor(triggerId=2301, visible=True, initialSequence='Closed') # door
        set_actor(triggerId=2302, visible=True, initialSequence='Closed') # door
        set_agent(triggerIds=[3301], visible=True)
        set_agent(triggerIds=[3302], visible=True)
        set_agent(triggerIds=[3303], visible=True)
        set_agent(triggerIds=[3304], visible=True)
        set_agent(triggerIds=[3305], visible=True)
        set_agent(triggerIds=[3306], visible=True)
        set_agent(triggerIds=[3307], visible=True)
        set_agent(triggerIds=[3308], visible=True)
        set_agent(triggerIds=[3309], visible=True)
        set_agent(triggerIds=[3310], visible=True)
        set_agent(triggerIds=[3311], visible=True)
        set_agent(triggerIds=[3312], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[501,502,601,602,701,702], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[501,502,601,602,701,702]):
            return 문열기()


class 문열기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1300], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1301], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[1302], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_effect(triggerIds=[4301], visible=True)
        set_effect(triggerIds=[4302], visible=True)
        set_effect(triggerIds=[4303], visible=True)
        set_actor(triggerId=2300, visible=True, initialSequence='Opened') # door
        set_actor(triggerId=2301, visible=True, initialSequence='Opened') # door
        set_actor(triggerId=2302, visible=True, initialSequence='Opened') # door
        set_agent(triggerIds=[3301], visible=False)
        set_agent(triggerIds=[3302], visible=False)
        set_agent(triggerIds=[3303], visible=False)
        set_agent(triggerIds=[3304], visible=False)
        set_agent(triggerIds=[3305], visible=False)
        set_agent(triggerIds=[3306], visible=False)
        set_agent(triggerIds=[3307], visible=False)
        set_agent(triggerIds=[3308], visible=False)
        set_agent(triggerIds=[3309], visible=False)
        set_agent(triggerIds=[3310], visible=False)
        set_agent(triggerIds=[3311], visible=False)
        set_agent(triggerIds=[3312], visible=False)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)


