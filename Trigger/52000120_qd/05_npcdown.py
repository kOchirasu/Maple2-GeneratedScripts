""" trigger/52000120_qd/05_npcdown.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001169], state=2)
        self.destroy_monster(spawnIds=[231]) # NPC
        self.set_user_value(key='NpcDown', value=0)
        self.set_user_value(key='BattleEnd', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='NpcDown', value=1):
            return Delay(self.ctx)


class Delay(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='NpcDown', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return NpcDown(self.ctx)


class NpcDown(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[221])
        self.set_interact_object(triggerIds=[10001169], state=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return Quit(self.ctx)
        if self.object_interacted(interactIds=[10001169], stateValue=0):
            return NpcWakeUp(self.ctx)


class NpcWakeUp(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001169], state=2)
        self.create_monster(spawnIds=[231], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return Quit(self.ctx)
        if self.npc_detected(boxId=9900, spawnIds=[221]):
            return Delay02(self.ctx)


class Delay02(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001169], state=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=45000):
            return NpcDown02(self.ctx)


class NpcDown02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[231])
        self.set_interact_object(triggerIds=[10001169], state=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return Quit(self.ctx)
        if self.object_interacted(interactIds=[10001169], stateValue=0):
            return NpcWakeUp(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[221,231])
        self.set_interact_object(triggerIds=[10001169], state=0)


initial_state = Wait
