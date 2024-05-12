""" trigger/02000348_bf/cage_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2104], visible=False, arg3=0, delay=10)
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_actor(triggerId=2204, visible=False, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cage_04', value=1):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2104], visible=True, arg3=0, delay=0)
        self.set_effect(triggerIds=[8004], visible=True)
        self.set_actor(triggerId=2204, visible=True, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[214]):
            return npc(self.ctx)


class npc(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_mesh(triggerIds=[2104], visible=False, arg3=0, delay=10)
        self.set_actor(triggerId=2204, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[224], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[224])


initial_state = idle
