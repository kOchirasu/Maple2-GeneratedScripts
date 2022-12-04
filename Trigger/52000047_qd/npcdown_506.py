""" trigger/52000047_qd/npcdown_506.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9900, spawnIds=[906]):
            return NpcFight(self.ctx)


class NpcFight(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[906]):
            return NpcDown(self.ctx)


class NpcDown(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[516], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcRemove', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[516])
        self.set_user_value(key='NpcRemove', value=0)


initial_state = Wait
