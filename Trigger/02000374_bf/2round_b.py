""" trigger/02000374_bf/2round_b.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='2Round_B', value=1):
            return Spawn_Start_Ready()


class Spawn_Start_Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Spawn_Start()


class Spawn_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7103], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round_Spawn_B_01_Ready2()


class Round_Spawn_B_01_Ready2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7203], visible=True)
        set_effect(triggerIds=[7003], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return Round_Spawn_B_01_2()


class Round_Spawn_B_01_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=False) # 캡틴 모크 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103]):
            return Round_Spawn_B_End2()


class Round_Spawn_B_End2(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_2007')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__2ROUND_B__0$', arg4=2, arg5=1)
        set_user_value(triggerId=2037401, key='2Round_B', value=1) # 캡틴 모크  소환 장치


