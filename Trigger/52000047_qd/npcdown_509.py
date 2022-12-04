""" trigger/52000047_qd/npcdown_509.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9900, spawnIds=[909]):
            return NpcFight(self.ctx)


class NpcFight(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[909]):
            return NpcDown(self.ctx)


class NpcDown(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[519], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcRemove', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[519])
        self.set_user_value(key='NpcRemove', value=0)


initial_state = Wait
