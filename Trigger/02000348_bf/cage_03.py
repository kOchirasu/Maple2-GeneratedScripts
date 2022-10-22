""" trigger/02000348_bf/cage_03.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2103], visible=False, arg3=0, arg4=10)
        set_effect(triggerIds=[8003], visible=False)
        set_actor(triggerId=2203, visible=False, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> state.State:
        if user_value(key='cage_03', value=1):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2103], visible=True, arg3=0, arg4=0)
        set_effect(triggerIds=[8003], visible=True)
        set_actor(triggerId=2203, visible=True, initialSequence='Sit_Ground_Idle_A')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[213]):
            return npc()


class npc(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8003], visible=False)
        set_mesh(triggerIds=[2103], visible=False, arg3=0, arg4=10)
        set_actor(triggerId=2203, visible=False, initialSequence='Dead_A')
        create_monster(spawnIds=[223], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[223])


