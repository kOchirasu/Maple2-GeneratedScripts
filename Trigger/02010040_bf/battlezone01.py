""" trigger/02010040_bf/battlezone01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[4101], visible=False)
        self.set_effect(triggerIds=[4102], visible=False)
        self.set_mesh(triggerIds=[1100], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1101], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_actor(triggerId=2100, visible=True, initialSequence='Closed') # door
        self.set_actor(triggerId=2101, visible=True, initialSequence='Closed') # door
        self.set_agent(triggerIds=[3101], visible=True)
        self.set_agent(triggerIds=[3102], visible=True)
        self.set_agent(triggerIds=[3103], visible=True)
        self.set_agent(triggerIds=[3104], visible=True)
        self.set_agent(triggerIds=[3105], visible=True)
        self.set_agent(triggerIds=[3106], visible=True)
        self.set_agent(triggerIds=[3107], visible=True)
        self.set_agent(triggerIds=[3108], visible=True)
        self.set_agent(triggerIds=[3109], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9100]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103,104,105,106,107,108,109,201,202,203,204,205,206,207,208,209,210], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105,106,107,108,109,201,202,203,204,205,206,207,208,209,210]):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1100], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[1101], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_effect(triggerIds=[4101], visible=True)
        self.set_effect(triggerIds=[4102], visible=True)
        self.set_actor(triggerId=2100, visible=True, initialSequence='Opened') # door
        self.set_actor(triggerId=2101, visible=True, initialSequence='Opened') # door
        self.set_agent(triggerIds=[3101], visible=False)
        self.set_agent(triggerIds=[3102], visible=False)
        self.set_agent(triggerIds=[3103], visible=False)
        self.set_agent(triggerIds=[3104], visible=False)
        self.set_agent(triggerIds=[3105], visible=False)
        self.set_agent(triggerIds=[3106], visible=False)
        self.set_agent(triggerIds=[3107], visible=False)
        self.set_agent(triggerIds=[3108], visible=False)
        self.set_agent(triggerIds=[3109], visible=False)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
