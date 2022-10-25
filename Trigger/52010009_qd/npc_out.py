""" trigger/52010009_qd/npc_out.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[111]):
            return npc_out(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[112]):
            return npc_out(self.ctx)
        if self.npc_detected(boxId=702, spawnIds=[113]):
            return npc_out(self.ctx)


class npc_out(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111,112,113])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return idle(self.ctx)


initial_state = idle
