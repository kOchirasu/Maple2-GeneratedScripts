""" trigger/63000040_cs/common.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[101]):
            return npc_exit_01(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[103]):
            return npc_exit_02(self.ctx)


class npc_exit_01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class npc_exit_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


initial_state = idle
