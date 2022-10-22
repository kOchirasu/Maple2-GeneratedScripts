""" trigger/63000003_cs/50001475.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[50001475], questStates=[3]):
            return 말풍선01()


class 말풍선01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=1, spawnId=1001, script='$63000003_CS__50001475__0$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_A')
        move_npc(spawnId=1002, patrolName='MS2PatrolData_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC이동()


class PC이동(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


