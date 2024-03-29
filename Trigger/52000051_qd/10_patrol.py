""" trigger/52000051_qd/10_patrol.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PatrolStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PatrolStart', value=1):
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[100,200])
        self.create_monster(spawnIds=[101,201], animationEffect=False) # 스크립트 잡담을 가지고 있는 NPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9301, boxId=1):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9302, boxId=1):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9303, boxId=1):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9304, boxId=1):
            return Patrol04(self.ctx)


class Patrol04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_104')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9305, boxId=1):
            return Patrol05Air(self.ctx)


class Patrol05Air(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=201, script='$52000051_QD__10_PATROL__0$', arg4=2, arg5=1) # 준타
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_105')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NpcChange02(self.ctx)


class NpcChange02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,201])
        self.create_monster(spawnIds=[102,202], animationEffect=False) # 연출용
        self.remove_balloon_talk(spawnId=201)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='PatrolEnd', value=1)


initial_state = Wait
