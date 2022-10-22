""" trigger/02000482_bf/02_mobattack.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False) # DoorOpen
        set_effect(triggerIds=[5002], visible=False) # DoorOpen
        set_effect(triggerIds=[5003], visible=False) # DoorOpen
        set_actor(triggerId=4001, visible=True, initialSequence='Closed')
        set_actor(triggerId=4002, visible=True, initialSequence='Closed')
        set_actor(triggerId=4003, visible=True, initialSequence='Closed')
        set_agent(triggerIds=[8000,8001], visible=True)
        set_agent(triggerIds=[8002,8003], visible=True)
        set_agent(triggerIds=[8004,8005], visible=True)
        destroy_monster(spawnIds=[910,911,920,921,930,931]) # Mob
        set_user_value(key='MobSpawn', value=0)
        set_user_value(key='MobAttack', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='MobSpawn', value=1):
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[910,911], arg2=False) # Mob01
        create_monster(spawnIds=[920,921], arg2=False) # Mob01
        create_monster(spawnIds=[930,931], arg2=False) # Mob01

    def on_tick(self) -> state.State:
        if user_value(key='MobAttack', value=1):
            return MobAttackDelay()


class MobAttackDelay(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return MobAttack01()


class MobAttack01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000,8001], visible=False)
        set_actor(triggerId=4001, visible=True, initialSequence='Opened')
        set_effect(triggerIds=[5001], visible=True) # DoorOpen

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MobAttack02()


class MobAttack02(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8002,8003], visible=False)
        set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        set_effect(triggerIds=[5002], visible=True) # DoorOpen

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MobAttack03()


class MobAttack03(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8004,8005], visible=False)
        set_actor(triggerId=4003, visible=True, initialSequence='Opened')
        set_effect(triggerIds=[5003], visible=True) # DoorOpen

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910,911,920,921,930,931,901,902,903]):
            return MobClear()


class MobClear(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='MobClear', value=1)


