""" trigger/02010040_bf/battlezone03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[4301], visible=False)
        self.set_effect(triggerIds=[4302], visible=False)
        self.set_effect(triggerIds=[4303], visible=False)
        self.set_mesh(triggerIds=[1300], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1301], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1302], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_actor(triggerId=2300, visible=True, initialSequence='Closed') # door
        self.set_actor(triggerId=2301, visible=True, initialSequence='Closed') # door
        self.set_actor(triggerId=2302, visible=True, initialSequence='Closed') # door
        self.set_agent(triggerIds=[3301], visible=True)
        self.set_agent(triggerIds=[3302], visible=True)
        self.set_agent(triggerIds=[3303], visible=True)
        self.set_agent(triggerIds=[3304], visible=True)
        self.set_agent(triggerIds=[3305], visible=True)
        self.set_agent(triggerIds=[3306], visible=True)
        self.set_agent(triggerIds=[3307], visible=True)
        self.set_agent(triggerIds=[3308], visible=True)
        self.set_agent(triggerIds=[3309], visible=True)
        self.set_agent(triggerIds=[3310], visible=True)
        self.set_agent(triggerIds=[3311], visible=True)
        self.set_agent(triggerIds=[3312], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9300]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[501,502,601,602,701,702], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501,502,601,602,701,702]):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1300], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1301], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1302], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_effect(triggerIds=[4301], visible=True)
        self.set_effect(triggerIds=[4302], visible=True)
        self.set_effect(triggerIds=[4303], visible=True)
        self.set_actor(triggerId=2300, visible=True, initialSequence='Opened') # door
        self.set_actor(triggerId=2301, visible=True, initialSequence='Opened') # door
        self.set_actor(triggerId=2302, visible=True, initialSequence='Opened') # door
        self.set_agent(triggerIds=[3301], visible=False)
        self.set_agent(triggerIds=[3302], visible=False)
        self.set_agent(triggerIds=[3303], visible=False)
        self.set_agent(triggerIds=[3304], visible=False)
        self.set_agent(triggerIds=[3305], visible=False)
        self.set_agent(triggerIds=[3306], visible=False)
        self.set_agent(triggerIds=[3307], visible=False)
        self.set_agent(triggerIds=[3308], visible=False)
        self.set_agent(triggerIds=[3309], visible=False)
        self.set_agent(triggerIds=[3310], visible=False)
        self.set_agent(triggerIds=[3311], visible=False)
        self.set_agent(triggerIds=[3312], visible=False)
        self.set_portal(portalId=6, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
