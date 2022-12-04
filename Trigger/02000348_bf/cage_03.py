""" trigger/02000348_bf/cage_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2103], visible=False, arg3=0, delay=10)
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_actor(triggerId=2203, visible=False, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cage_03', value=1):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2103], visible=True, arg3=0, delay=0)
        self.set_effect(triggerIds=[8003], visible=True)
        self.set_actor(triggerId=2203, visible=True, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[213]):
            return npc(self.ctx)


class npc(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_mesh(triggerIds=[2103], visible=False, arg3=0, delay=10)
        self.set_actor(triggerId=2203, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[223], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[223])


initial_state = idle
