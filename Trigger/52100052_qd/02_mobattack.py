""" trigger/52100052_qd/02_mobattack.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=False) # DoorOpen
        self.set_effect(triggerIds=[5002], visible=False) # DoorOpen
        self.set_effect(triggerIds=[5003], visible=False) # DoorOpen
        self.set_actor(triggerId=4001, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4002, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=4003, visible=True, initialSequence='Closed')
        self.set_agent(triggerIds=[8000,8001], visible=True)
        self.set_agent(triggerIds=[8002,8003], visible=True)
        self.set_agent(triggerIds=[8004,8005], visible=True)
        self.destroy_monster(spawnIds=[910,911,920,921,930,931]) # Mob
        self.set_user_value(key='MobSpawn', value=0)
        self.set_user_value(key='MobAttack', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawn', value=1):
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[910,911], animationEffect=False) # Mob01
        self.create_monster(spawnIds=[920,921], animationEffect=False) # Mob01
        self.create_monster(spawnIds=[930,931], animationEffect=False) # Mob01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobAttack', value=1):
            return MobAttackDelay(self.ctx)


class MobAttackDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return MobAttack01(self.ctx)


class MobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8000,8001], visible=False)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Opened')
        self.set_effect(triggerIds=[5001], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MobAttack02(self.ctx)


class MobAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8002,8003], visible=False)
        self.set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        self.set_effect(triggerIds=[5002], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MobAttack03(self.ctx)


class MobAttack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[8004,8005], visible=False)
        self.set_actor(triggerId=4003, visible=True, initialSequence='Opened')
        self.set_effect(triggerIds=[5003], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[910,911,920,921,930,931,901,902,903]):
            return MobClear(self.ctx)


class MobClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1, key='MobClear', value=1)


initial_state = Setting
