""" trigger/02000378_bf/09_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4029], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3009], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3109], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3009], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3109], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5209], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal()


#  포탈로 진입 
class ReadyToWalkIn_FromPortal(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4029], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_user_value(triggerId=1309, key='RouteSelected', value=1)
        set_user_value(triggerId=2309, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02()

    def on_exit(self):
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[2009], arg2=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=109, script='$02000378_BF__09_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round09_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[109])


class Round09_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1009], arg2=False) # 수호대상 틴차이
        set_conversation(type=1, spawnId=1009, script='$02000378_BF__09_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=909, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='09RoundSuccess', value=1):
            return Round09_Sucess()


class Round09_Sucess(state.State):
    def on_enter(self):
        move_npc(spawnId=2009, patrolName='MS2PatrolData_2009')
        destroy_monster(spawnIds=[1009])
        create_monster(spawnIds=[109], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3009], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3109], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3009], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3109], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5209], visible=True) # Sound_CrystalOn
        set_conversation(type=1, spawnId=109, script='$02000378_BF__09_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round09_RouteSelect()


class Round09_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2009])
        create_monster(spawnIds=[209], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round09_PickRoute_Left()
        if random_condition(rate=50):
            return Round09_PickRoute_Right()


class Round09_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1309, key='MakeTrue', value=1)
        set_user_value(triggerId=2309, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal15()


class GoToPortal15(state.State):
    def on_enter(self):
        move_npc(spawnId=109, patrolName='MS2PatrolData_15')
        move_npc(spawnId=209, patrolName='MS2PatrolData_25')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Round09_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1309, key='MakeFalse', value=1)
        set_user_value(triggerId=2309, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal16()


class GoToPortal16(state.State):
    def on_enter(self):
        set_user_value(triggerId=12, key='FindWay', value=1)
        move_npc(spawnId=109, patrolName='MS2PatrolData_16')
        move_npc(spawnId=209, patrolName='MS2PatrolData_26')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109,209])


