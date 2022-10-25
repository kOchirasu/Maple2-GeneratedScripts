""" trigger/52000116_qd/idle.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101]) # Nelf_11003163

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return nelftalk(self.ctx)


class nelftalk(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$52000116_QD__IDLE__0$', arg4=3, arg5=0) # 넬프 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return nelfmove(self.ctx)


class nelfmove(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3001')


initial_state = idle
