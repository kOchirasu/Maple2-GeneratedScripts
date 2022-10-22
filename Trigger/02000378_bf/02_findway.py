""" trigger/02000378_bf/02_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=24, visible=False, enabled=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
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
        create_monster(spawnIds=[901,902,903], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        set_conversation(type=1, spawnId=201, script='$02000378_BF__02_FINDWAY__0$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1302, key='RouteSelected', value=1)
        set_user_value(triggerId=2302, key='RouteSelected', value=1)
        set_conversation(type=1, spawnId=201, script='$02000378_BF__02_FINDWAY__1$', arg4=2, arg5=1) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000378_BF__02_FINDWAY__2$', arg4=2, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round02_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[101,201])


class Round02_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2002], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1002, script='$02000378_BF__02_FINDWAY__3$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=902, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='02RoundSuccess', value=1):
            return Round02_Sucess02()


class Round02_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2002')
        destroy_monster(spawnIds=[1002])
        create_monster(spawnIds=[102], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3002], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh_animation(triggerIds=[3002], visible=False, arg3=0, arg4=0) # CrystalOff
        set_effect(triggerIds=[5202], visible=True) # Sound_CrystalOn
        set_portal(portalId=24, visible=True, enabled=True, minimapVisible=False)
        set_conversation(type=1, spawnId=102, script='$02000378_BF__02_FINDWAY__4$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round02_RouteSelect()


class Round02_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])
        create_monster(spawnIds=[202], arg2=False) # 연출용 준타
        move_npc(spawnId=102, patrolName='MS2PatrolData_102New')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound12()
        """
        <condition name="랜덤조건" arg1="50">    
                    <transition state="Round02_PickRoute_Left"/>    
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round02_PickRoute_Right" />
                </condition>
        """


class GoToRound12(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        move_npc(spawnId=202, patrolName='MS2PatrolData_202New')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[901,902,903])


