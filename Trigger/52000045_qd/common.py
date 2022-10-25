""" trigger/52000045_qd/common.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[201]):
            return npc_exit_01(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[202]):
            return npc_exit_02(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[203]):
            return npc_exit_03(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[204]):
            return npc_exit_04(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[205]):
            return npc_exit_05(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[206]):
            return npc_exit_06(self.ctx)


class npc_exit_01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class npc_exit_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class npc_exit_03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[203])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class npc_exit_04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[204])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class npc_exit_05(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[205])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class npc_exit_06(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[206])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


initial_state = idle
