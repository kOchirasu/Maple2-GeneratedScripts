""" trigger/99999874/151001_npckill.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='NPCKill', value=1):
            return NPCKillWait(self.ctx)


class NPCKillWait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7500):
            return NPCKill(self.ctx)


class NPCKill(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[15401,15402,15501,15502])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return KillEnd(self.ctx)


class KillEnd(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=151001, key='NPCKill', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
