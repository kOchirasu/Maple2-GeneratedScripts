""" trigger/52000052_qd/05_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4025], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3005], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3105], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3005], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3105], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5205], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn01()


#  왼쪽에서 진입 
class ReadyToWalkIn01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4025], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        move_npc(spawnId=104, patrolName='MS2PatrolData_105')
        move_npc(spawnId=204, patrolName='MS2PatrolData_205')
        set_conversation(type=1, spawnId=204, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1305, key='RouteSelected', value=1)
        set_user_value(triggerId=2305, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round05_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[104,204])


class Round05_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1005], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2005], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1005, script='$52000052_QD__04_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=905, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='05RoundSuccess', value=1):
            return Round05_Sucess()


class Round05_Sucess(state.State):
    def on_enter(self):
        move_npc(spawnId=2005, patrolName='MS2PatrolData_2005')
        destroy_monster(spawnIds=[1005])
        create_monster(spawnIds=[105], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3005], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3105], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3005], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3105], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5205], visible=True) # Sound_CrystalOn
        set_conversation(type=1, spawnId=105, script='$52000052_QD__04_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round05_RouteSelect()


class Round05_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2005])
        create_monster(spawnIds=[205], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round05_PickRoute_Left()
        if random_condition(rate=50):
            return Round05_PickRoute_Right()


class Round05_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1305, key='MakeTrue', value=1)
        set_user_value(triggerId=2305, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal11()


class GoToPortal11(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_11')
        move_npc(spawnId=205, patrolName='MS2PatrolData_21')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Round05_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1305, key='MakeFalse', value=1)
        set_user_value(triggerId=2305, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal12()


class GoToPortal12(state.State):
    def on_enter(self):
        set_user_value(triggerId=12, key='FindWay', value=1)
        move_npc(spawnId=105, patrolName='MS2PatrolData_12')
        move_npc(spawnId=205, patrolName='MS2PatrolData_22')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105,205])


