""" trigger/02010040_bf/battlezone02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[4201], visible=False)
        self.set_effect(triggerIds=[4202], visible=False)
        self.set_mesh(triggerIds=[1200], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1201], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_actor(triggerId=2200, visible=True, initialSequence='Closed') # door
        self.set_actor(triggerId=2201, visible=True, initialSequence='Closed') # door
        self.set_agent(triggerIds=[3201], visible=True)
        self.set_agent(triggerIds=[3202], visible=True)
        self.set_agent(triggerIds=[3203], visible=True)
        self.set_agent(triggerIds=[3204], visible=True)
        self.set_agent(triggerIds=[3205], visible=True)
        self.set_agent(triggerIds=[3206], visible=True)
        self.set_agent(triggerIds=[3207], visible=True)
        self.set_agent(triggerIds=[3208], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9200]):
            return 전투시작(self.ctx)


class 전투시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304,305,306,401,402,403,404,405,406,407,408], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301,302,303,304,305,306,401,402,403,404,405,406,407,408]):
            return 문열기(self.ctx)


class 문열기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1200], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1201], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_effect(triggerIds=[4201], visible=True)
        self.set_effect(triggerIds=[4202], visible=True)
        self.set_actor(triggerId=2200, visible=True, initialSequence='Opened') # door
        self.set_actor(triggerId=2201, visible=True, initialSequence='Opened') # door
        self.set_agent(triggerIds=[3201], visible=False)
        self.set_agent(triggerIds=[3202], visible=False)
        self.set_agent(triggerIds=[3203], visible=False)
        self.set_agent(triggerIds=[3204], visible=False)
        self.set_agent(triggerIds=[3205], visible=False)
        self.set_agent(triggerIds=[3206], visible=False)
        self.set_agent(triggerIds=[3207], visible=False)
        self.set_agent(triggerIds=[3208], visible=False)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
