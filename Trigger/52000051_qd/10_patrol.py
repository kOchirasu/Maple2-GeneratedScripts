""" trigger/52000051_qd/10_patrol.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PatrolStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PatrolStart', value=1):
            return Delay01()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcChange01()


class NpcChange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[100,200])
        create_monster(spawnIds=[101,201], arg2=False) # 스크립트 잡담을 가지고 있는 NPC

    def on_tick(self) -> state.State:
        if count_users(boxId=9301, boxId=1):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if count_users(boxId=9302, boxId=1):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if count_users(boxId=9303, boxId=1):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        move_npc(spawnId=201, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if count_users(boxId=9304, boxId=1):
            return Patrol04()


class Patrol04(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_104')
        move_npc(spawnId=201, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if count_users(boxId=9305, boxId=1):
            return Patrol05Air()


class Patrol05Air(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$52000051_QD__10_PATROL__0$', arg4=2, arg5=1) # 준타
        move_npc(spawnId=101, patrolName='MS2PatrolData_105')
        move_npc(spawnId=201, patrolName='MS2PatrolData_205')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NpcChange02()


class NpcChange02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[102,202], arg2=False) # 연출용
        remove_balloon_talk(spawnId=201)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='PatrolEnd', value=1)


