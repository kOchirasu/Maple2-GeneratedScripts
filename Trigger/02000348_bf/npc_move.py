""" trigger/02000348_bf/npc_move.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=60004, boxId=1):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000348_BF__NPC_MOVE__0$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return start_02(self.ctx)


class start_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=60003, spawnIds=[102]):
            return end(self.ctx)
        if self.wait_tick(waitTick=2000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])


initial_state = idle
