""" trigger/52000070_qd/npcdown_903.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9900, spawnIds=[903]):
            return NpcFight(self.ctx)


class NpcFight(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[903]):
            return NpcDown(self.ctx)


class NpcDown(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[303], animationEffect=False)


initial_state = Wait
