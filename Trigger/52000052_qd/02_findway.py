""" trigger/52000052_qd/02_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4022], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3102], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3002], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3102], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5202], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn01()


class ReadyToWalkIn01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4022], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        set_conversation(type=1, spawnId=201, script='$52000052_QD__02_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1302, key='RouteSelected', value=1)
        set_user_value(triggerId=2302, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$52000052_QD__02_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round02_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[101,201])


class Round02_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2002], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1002, script='$52000052_QD__02_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=902, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='02RoundSuccess', value=1):
            return Round02_Sucess01()


class Round02_Sucess01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9002, spawnIds=[2202]):
            return Round02_Sucess02()


class Round02_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2202, patrolName='MS2PatrolData_2002')
        destroy_monster(spawnIds=[1002])
        create_monster(spawnIds=[102], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3002], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3102], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3102], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5202], visible=True) # Sound_CrystalOn
        set_conversation(type=1, spawnId=102, script='$52000052_QD__02_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round02_RouteSelect()


class Round02_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2202])
        create_monster(spawnIds=[202], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round02_PickRoute_Left()
        if random_condition(rate=50):
            return Round02_PickRoute_Right()


class Round02_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1302, key='MakeTrue', value=1)
        set_user_value(triggerId=2302, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound04()


class GoToRound04(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='FindWayLeft', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Round02_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1302, key='MakeFalse', value=1)
        set_user_value(triggerId=2302, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound07()


class GoToRound07(state.State):
    def on_enter(self):
        set_user_value(triggerId=7, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Quit(state.State):
    pass


