""" trigger/02000348_bf/cage_02.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2102], visible=False, arg3=0, delay=10)
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_actor(triggerId=2202, visible=False, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='cage_02', value=1):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2102], visible=True, arg3=0, delay=0)
        self.set_effect(triggerIds=[8002], visible=True)
        self.set_actor(triggerId=2202, visible=True, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[212]):
            return npc(self.ctx)


class npc(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_mesh(triggerIds=[2102], visible=False, arg3=0, delay=10)
        self.set_actor(triggerId=2202, visible=False, initialSequence='Dead_A')
        self.create_monster(spawnIds=[222], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[222])


initial_state = idle
