""" trigger/52000052_qd/08_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=23, visible=False, enabled=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        set_mesh(triggerIds=[4028], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3008], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3108], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3008], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3108], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5208], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn01()


class ReadyToWalkIn01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4028], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        move_npc(spawnId=103, patrolName='MS2PatrolData_108')
        move_npc(spawnId=203, patrolName='MS2PatrolData_208')
        set_conversation(type=1, spawnId=203, script='$52000052_QD__04_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1308, key='RouteSelected', value=1)
        set_user_value(triggerId=2308, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=103, script='$52000052_QD__04_FINDWAY__1$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round08_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[103,203])


class Round08_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1008], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2008], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1008, script='$52000052_QD__04_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=908, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='08RoundSuccess', value=1):
            return Round08_Sucess02()


class Round08_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2008, patrolName='MS2PatrolData_2008') # action name="NPC를이동시킨다" arg1="2208" arg2="MS2PatrolData_2008" /
        destroy_monster(spawnIds=[1008])
        create_monster(spawnIds=[108], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3008], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh_animation(triggerIds=[3008], visible=False, arg3=0, arg4=0) # CrystalOff
        set_effect(triggerIds=[5208], visible=True) # Sound_CrystalOn
        set_portal(portalId=23, visible=True, enabled=True, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        set_conversation(type=1, spawnId=108, script='$52000052_QD__04_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round08_RouteSelect()


class Round08_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2008]) # action name="몬스터소멸시킨다" arg1="2208" /
        create_monster(spawnIds=[208], arg2=False) # 연출용 준타
        move_npc(spawnId=108, patrolName='MS2PatrolData_108New')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GoToRound12()
        """
        <condition name="랜덤조건" arg1="50">    
                    <transition state="Round08_PickRoute_Left"/>        
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round08_PickRoute_Right" />
                </condition>
        """


class GoToRound12(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[108])
        move_npc(spawnId=208, patrolName='MS2PatrolData_208New')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[208])


#  20170223 업데이트 던전 개편 단축 
class Round08_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1308, key='MakeTrue', value=1)
        set_user_value(triggerId=2308, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound10()


class GoToRound10(state.State):
    def on_enter(self):
        set_user_value(triggerId=10, key='FindWayRight', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Round08_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1308, key='MakeFalse', value=1)
        set_user_value(triggerId=2308, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound11()


class GoToRound11(state.State):
    def on_enter(self):
        set_user_value(triggerId=11, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Quit(state.State):
    pass


