""" trigger/52000070_qd/npcdown_901.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9900, spawnIds=[901]):
            return NpcFight(self.ctx)


class NpcFight(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[901]):
            return NpcDown(self.ctx)


class NpcDown(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301], animationEffect=False)


initial_state = Wait
