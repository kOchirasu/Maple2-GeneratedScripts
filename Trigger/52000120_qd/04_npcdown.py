""" trigger/52000120_qd/04_npcdown.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001170], state=2)
        self.destroy_monster(spawnIds=[230]) # NPC
        self.set_user_value(key='NpcDown', value=0)
        self.set_user_value(key='BattleEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcDown', value=1):
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='NpcDown', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return NpcDown(self.ctx)


class NpcDown(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[220])
        self.set_interact_object(triggerIds=[10001170], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return Quit(self.ctx)
        if self.object_interacted(interactIds=[10001170], stateValue=0):
            return NpcWakeUp(self.ctx)


class NpcWakeUp(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001170], state=2)
        self.create_monster(spawnIds=[230], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return Quit(self.ctx)
        if self.npc_detected(boxId=9900, spawnIds=[220]):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001170], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return Quit(self.ctx)
        if self.wait_tick(waitTick=20000):
            return NpcDown02(self.ctx)


class NpcDown02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[220])
        self.set_interact_object(triggerIds=[10001170], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return Quit(self.ctx)
        if self.object_interacted(interactIds=[10001170], stateValue=0):
            return NpcWakeUp(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[220,230])
        self.set_interact_object(triggerIds=[10001170], state=0)


initial_state = Wait
