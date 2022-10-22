""" trigger/02000378_bf/07_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=22, visible=False, enabled=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        set_mesh(triggerIds=[4027], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3007], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3107], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3007], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3107], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5207], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal()


#  포탈로 진입 
class ReadyToWalkIn_FromPortal(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4027], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_user_value(triggerId=1307, key='RouteSelected', value=1)
        set_user_value(triggerId=2307, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02()

    def on_exit(self):
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[2007], arg2=False) # 전투용 준타


class ReadyToWalkIn_FromPortal02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=107, script='$02000378_BF__07_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round07_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[107])


class Round07_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1007], arg2=False) # 수호대상 틴차이
        set_conversation(type=1, spawnId=1007, script='$02000378_BF__07_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=907, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='07RoundSuccess', value=1):
            return Round07_Sucess02()


class Round07_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2007, patrolName='MS2PatrolData_2007') # action name="NPC를이동시킨다" arg1="2207" arg2="MS2PatrolData_2007" /
        destroy_monster(spawnIds=[1007])
        create_monster(spawnIds=[107], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3007], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh_animation(triggerIds=[3007], visible=False, arg3=0, arg4=0) # CrystalOff
        set_effect(triggerIds=[5207], visible=True) # Sound_CrystalOn
        set_portal(portalId=22, visible=True, enabled=True, minimapVisible=False)
        set_conversation(type=1, spawnId=107, script='$02000378_BF__07_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round07_RouteSelect()


class Round07_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2007])
        create_monster(spawnIds=[207], arg2=False) # 연출용 준타
        move_npc(spawnId=107, patrolName='MS2PatrolData_107New')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound12()
        """
        <condition name="랜덤조건" arg1="50">    
                    <transition state="Round07_PickRoute_Left"/>    
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round07_PickRoute_Right" />
                </condition>
        """


class GoToRound12(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[107])
        move_npc(spawnId=207, patrolName='MS2PatrolData_207New')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[207])


