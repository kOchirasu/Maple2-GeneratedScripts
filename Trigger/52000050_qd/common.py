""" trigger/52000050_qd/common.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[121]):
            return npc_exit_01(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[122]):
            return npc_exit_02(self.ctx)


class npc_exit_01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[121])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class npc_exit_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[122])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


initial_state = idle
