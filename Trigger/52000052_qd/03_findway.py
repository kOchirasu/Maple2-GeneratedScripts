""" trigger/52000052_qd/03_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4023], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3103], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3003], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3103], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5203], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn01()


class ReadyToWalkIn01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4023], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        set_conversation(type=1, spawnId=201, script='$52000052_QD__02_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1303, key='RouteSelected', value=1)
        set_user_value(triggerId=2303, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000052_QD__02_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round03_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[101,201])


class Round03_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2003], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1003, script='$52000052_QD__02_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=903, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='03RoundSuccess', value=1):
            return Round03_Sucess01()


class Round03_Sucess01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9003, spawnIds=[2203]):
            return Round03_Sucess02()


class Round03_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2203, patrolName='MS2PatrolData_2003')
        destroy_monster(spawnIds=[1003])
        create_monster(spawnIds=[103], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3003], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3103], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3003], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3103], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5203], visible=True) # Sound_CrystalOn
        set_conversation(type=1, spawnId=103, script='$52000052_QD__02_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round03_RouteSelect()


class Round03_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2203])
        create_monster(spawnIds=[203], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round03_PickRoute_Left()
        if random_condition(rate=50):
            return Round03_PickRoute_Right()


class Round03_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1303, key='MakeTrue', value=1)
        set_user_value(triggerId=2303, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound04()


class GoToRound04(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='FindWayRight', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Round03_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1303, key='MakeFalse', value=1)
        set_user_value(triggerId=2303, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound08()


class GoToRound08(state.State):
    def on_enter(self):
        set_user_value(triggerId=8, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Quit(state.State):
    pass


