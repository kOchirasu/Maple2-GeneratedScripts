""" trigger/02000386_bf/main_02.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=702, spawnIds=[901]):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=901, script='$02000386_BF__MAIN_02__0$', arg4=2, arg5=0)
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901])


initial_state = idle
