""" trigger/02000374_bf/2round_a.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='2Round_A', value=1):
            return Spawn_Start_Ready()


class Spawn_Start_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Spawn_Start()


class Spawn_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7102], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round_Spawn_A_01_Ready2()


class Round_Spawn_A_01_Ready2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7202], visible=True)
        set_effect(triggerIds=[7002], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return Round_Spawn_A_01_2()


class Round_Spawn_A_01_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False) # 파모칸 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return Round_Spawn_A_End2()


class Round_Spawn_A_End2(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_2006')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__2ROUND_A__0$', arg4=2, arg5=1)
        set_user_value(triggerId=2037401, key='2Round_A', value=1) # 파모칸 소환 장치


