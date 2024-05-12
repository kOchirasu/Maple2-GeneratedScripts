""" trigger/02010040_bf/battlezone03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6, visible=False, enable=False, minimap_visible=False)
        self.set_effect(trigger_ids=[4301], visible=False)
        self.set_effect(trigger_ids=[4302], visible=False)
        self.set_effect(trigger_ids=[4303], visible=False)
        self.set_mesh(trigger_ids=[1300], visible=True, start_delay=0, interval=0, fade=0) # barrier
        self.set_mesh(trigger_ids=[1301], visible=True, start_delay=0, interval=0, fade=0) # barrier
        self.set_mesh(trigger_ids=[1302], visible=True, start_delay=0, interval=0, fade=0) # barrier
        self.set_actor(trigger_id=2300, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=2301, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=2302, visible=True, initial_sequence='Closed') # door
        self.set_agent(trigger_ids=[3301], visible=True)
        self.set_agent(trigger_ids=[3302], visible=True)
        self.set_agent(trigger_ids=[3303], visible=True)
        self.set_agent(trigger_ids=[3304], visible=True)
        self.set_agent(trigger_ids=[3305], visible=True)
        self.set_agent(trigger_ids=[3306], visible=True)
        self.set_agent(trigger_ids=[3307], visible=True)
        self.set_agent(trigger_ids=[3308], visible=True)
        self.set_agent(trigger_ids=[3309], visible=True)
        self.set_agent(trigger_ids=[3310], visible=True)
        self.set_agent(trigger_ids=[3311], visible=True)
        self.set_agent(trigger_ids=[3312], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[501,502,601,602,701,702], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[501,502,601,602,701,702]):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1300], visible=False, start_delay=0, interval=0, fade=0) # barrier
        self.set_mesh(trigger_ids=[1301], visible=False, start_delay=0, interval=0, fade=0) # barrier
        self.set_mesh(trigger_ids=[1302], visible=False, start_delay=0, interval=0, fade=0) # barrier
        self.set_effect(trigger_ids=[4301], visible=True)
        self.set_effect(trigger_ids=[4302], visible=True)
        self.set_effect(trigger_ids=[4303], visible=True)
        self.set_actor(trigger_id=2300, visible=True, initial_sequence='Opened') # door
        self.set_actor(trigger_id=2301, visible=True, initial_sequence='Opened') # door
        self.set_actor(trigger_id=2302, visible=True, initial_sequence='Opened') # door
        self.set_agent(trigger_ids=[3301], visible=False)
        self.set_agent(trigger_ids=[3302], visible=False)
        self.set_agent(trigger_ids=[3303], visible=False)
        self.set_agent(trigger_ids=[3304], visible=False)
        self.set_agent(trigger_ids=[3305], visible=False)
        self.set_agent(trigger_ids=[3306], visible=False)
        self.set_agent(trigger_ids=[3307], visible=False)
        self.set_agent(trigger_ids=[3308], visible=False)
        self.set_agent(trigger_ids=[3309], visible=False)
        self.set_agent(trigger_ids=[3310], visible=False)
        self.set_agent(trigger_ids=[3311], visible=False)
        self.set_agent(trigger_ids=[3312], visible=False)
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
