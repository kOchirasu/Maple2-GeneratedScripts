""" trigger/02000378_bf/10_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4030], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3010], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3110], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3010], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3110], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5210], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal()


#  포탈로 진입 
class ReadyToWalkIn_FromPortal(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4030], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_user_value(triggerId=1310, key='RouteSelected', value=1)
        set_user_value(triggerId=2310, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02()

    def on_exit(self):
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[2010], arg2=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=110, script='$02000378_BF__10_FINDWAY__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round10_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[110])


class Round10_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1010], arg2=False) # 수호대상 틴차이
        set_conversation(type=1, spawnId=1010, script='$02000378_BF__10_FINDWAY__4$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=910, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='10RoundSuccess', value=1):
            return Round10_Sucess01()


class Round10_Sucess01(state.State):
    def on_enter(self):
        move_npc(spawnId=2010, patrolName='MS2PatrolData_2010')
        destroy_monster(spawnIds=[1010])
        create_monster(spawnIds=[110], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3010], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3110], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3010], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3110], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5210], visible=True) # Sound_CrystalOn
        set_conversation(type=1, spawnId=110, script='$02000378_BF__10_FINDWAY__5$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round10_RouteSelect()


class Round10_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2010])
        create_monster(spawnIds=[210], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round10_PickRoute_Left()
        if random_condition(rate=50):
            return Round10_PickRoute_Right()


class Round10_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1310, key='MakeTrue', value=1)
        set_user_value(triggerId=2310, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal17()


class GoToPortal17(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_17')
        move_npc(spawnId=210, patrolName='MS2PatrolData_27')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Round10_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1310, key='MakeFalse', value=1)
        set_user_value(triggerId=2310, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToPortal18()


class GoToPortal18(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_18')
        move_npc(spawnId=210, patrolName='MS2PatrolData_28')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[110,210])


