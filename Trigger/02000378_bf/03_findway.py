""" trigger/02000378_bf/03_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=25, visible=False, enabled=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
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
        create_monster(spawnIds=[904,905,906], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        set_conversation(type=1, spawnId=201, script='$02000378_BF__03_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1303, key='RouteSelected', value=1)
        set_user_value(triggerId=2303, key='RouteSelected', value=1)
        set_conversation(type=1, spawnId=201, script='$02000378_BF__03_FINDWAY__1$', arg4=2, arg5=1) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000378_BF__03_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round03_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[101,201])


class Round03_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1003], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2003], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1003, script='$02000378_BF__03_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=903, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='03RoundSuccess', value=1):
            return Round03_Sucess02()


class Round03_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2003, patrolName='MS2PatrolData_2003')
        destroy_monster(spawnIds=[1003])
        create_monster(spawnIds=[103], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3003], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh_animation(triggerIds=[3003], visible=False, arg3=0, arg4=0) # CrystalOff
        set_effect(triggerIds=[5203], visible=True) # Sound_CrystalOn
        set_portal(portalId=25, visible=True, enabled=True, minimapVisible=False)
        set_conversation(type=1, spawnId=103, script='$02000378_BF__03_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round03_RouteSelect()


class Round03_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2003])
        create_monster(spawnIds=[203], arg2=False) # 연출용 준타
        move_npc(spawnId=103, patrolName='MS2PatrolData_103New')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound12()
        """
        <condition name="랜덤조건" arg1="50">        
                    <transition state="Round03_PickRoute_Left"/>    
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round03_PickRoute_Right" />
                </condition>
        """


class GoToRound12(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        move_npc(spawnId=203, patrolName='MS2PatrolData_203New')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[203])
        destroy_monster(spawnIds=[904,905,906])


