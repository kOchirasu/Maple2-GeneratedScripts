""" trigger/52000052_qd/06_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4026], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3006], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3106], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3006], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3106], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5206], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn01()


#  왼쪽에서 진입 
class ReadyToWalkIn01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4026], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        move_npc(spawnId=104, patrolName='MS2PatrolData_106')
        move_npc(spawnId=204, patrolName='MS2PatrolData_206')
        set_conversation(type=1, spawnId=204, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1306, key='RouteSelected', value=1)
        set_user_value(triggerId=2306, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round06_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[104,204])


class Round06_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2006], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1006, script='$52000052_QD__04_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=906, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='06RoundSuccess', value=1):
            return Round06_Sucess()


class Round06_Sucess(state.State):
    def on_enter(self):
        move_npc(spawnId=2006, patrolName='MS2PatrolData_2006')
        destroy_monster(spawnIds=[1006])
        create_monster(spawnIds=[106], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3006], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3106], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3006], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3106], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5206], visible=True) # Sound_CrystalOn
        set_conversation(type=1, spawnId=106, script='$52000052_QD__04_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Round06_RouteSelect()


class Round06_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2006])
        create_monster(spawnIds=[206], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round06_PickRoute_Left()
        if random_condition(rate=50):
            return Round06_PickRoute_Right()


class Round06_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1306, key='MakeTrue', value=1)
        set_user_value(triggerId=2306, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal13()


class GoToPortal13(state.State):
    def on_enter(self):
        move_npc(spawnId=106, patrolName='MS2PatrolData_13')
        move_npc(spawnId=206, patrolName='MS2PatrolData_23')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Round06_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1306, key='MakeFalse', value=1)
        set_user_value(triggerId=2306, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal14()


class GoToPortal14(state.State):
    def on_enter(self):
        set_user_value(triggerId=12, key='FindWay', value=1)
        move_npc(spawnId=106, patrolName='MS2PatrolData_14')
        move_npc(spawnId=206, patrolName='MS2PatrolData_24')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[106,206])


