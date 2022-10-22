""" trigger/02000378_bf/11_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4031], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3011], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3111], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3011], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3111], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5211], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal()


#  포탈로 진입 
class ReadyToWalkIn_FromPortal(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4031], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_user_value(triggerId=1311, key='RouteSelected', value=1)
        set_user_value(triggerId=2311, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02()

    def on_exit(self):
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[2011], arg2=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=111, script='$02000378_BF__11_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round11_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[111])


class Round11_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1011], arg2=False) # 수호대상 틴차이
        set_conversation(type=1, spawnId=1011, script='$02000378_BF__11_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=911, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='11RoundSuccess', value=1):
            return Round11_Sucess()


class Round11_Sucess(state.State):
    def on_enter(self):
        move_npc(spawnId=2011, patrolName='MS2PatrolData_2011')
        destroy_monster(spawnIds=[1011])
        create_monster(spawnIds=[111], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3011], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3111], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3011], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3111], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5211], visible=True) # Sound_CrystalOn
        set_conversation(type=1, spawnId=111, script='$02000378_BF__11_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Round11_RouteSelect()


class Round11_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2011])
        create_monster(spawnIds=[211], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round11_PickRoute_Left()
        if random_condition(rate=50):
            return Round11_PickRoute_Right()


class Round11_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1311, key='MakeTrue', value=1)
        set_user_value(triggerId=2311, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal19()


class GoToPortal19(state.State):
    def on_enter(self):
        move_npc(spawnId=111, patrolName='MS2PatrolData_19')
        move_npc(spawnId=211, patrolName='MS2PatrolData_29')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Round11_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1311, key='MakeFalse', value=1)
        set_user_value(triggerId=2311, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal10()


class GoToPortal10(state.State):
    def on_enter(self):
        set_user_value(triggerId=12, key='FindWay', value=1)
        move_npc(spawnId=111, patrolName='MS2PatrolData_10')
        move_npc(spawnId=211, patrolName='MS2PatrolData_20')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111,211])


