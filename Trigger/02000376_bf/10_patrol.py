""" trigger/02000376_bf/10_patrol.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PatrolStart', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PatrolStart', value=1):
            return Delay01(self.ctx)


class Delay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcChange01(self.ctx)


class NpcChange01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[100,200])
        self.create_monster(spawnIds=[101,201], animationEffect=False) # 스크립트 잡담을 가지고 있는 NPC

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9301, spawnIds=[101]):
            return Patrol01(self.ctx)


class Patrol01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9302, spawnIds=[101]):
            return Patrol02(self.ctx)


class Patrol02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9303, spawnIds=[101]):
            return Patrol03(self.ctx)


class Patrol03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_203')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9304, spawnIds=[101]):
            return Patrol04(self.ctx)


class Patrol04(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_104')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_204')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9305, spawnIds=[101]):
            return Patrol05Air(self.ctx)


class Patrol05Air(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=201, script='$02000376_BF__10_PATROL__0$', arg4=2, arg5=0) # 준타
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_105')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_205')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NpcChange02(self.ctx)


class NpcChange02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[102,202], animationEffect=False) # 연출용
        self.remove_balloon_talk(spawnId=201)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='PatrolEnd', value=1)


initial_state = Wait
