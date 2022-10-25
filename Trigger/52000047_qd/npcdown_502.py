""" trigger/52000047_qd/npcdown_502.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9900, spawnIds=[902]):
            return NpcFight(self.ctx)


class NpcFight(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[902]):
            return NpcDown(self.ctx)


class NpcDown(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[512], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='NpcRemove', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[512])
        self.set_user_value(key='NpcRemove', value=0)


initial_state = Wait
