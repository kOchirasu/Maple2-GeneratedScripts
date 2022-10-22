""" trigger/02000378_bf/04_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False) # 20170223 업데이트 던전 개편 단축
        set_mesh(triggerIds=[4024], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3004], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3104], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3004], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3104], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5204], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal()


#  포탈로 진입 
class ReadyToWalkIn_FromPortal(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4024], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_user_value(triggerId=1304, key='RouteSelected', value=1)
        set_user_value(triggerId=2304, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02()

    def on_exit(self):
        create_monster(spawnIds=[2004], arg2=False) # 전투용 준타
        create_monster(spawnIds=[104], arg2=False)


class ReadyToWalkIn_FromPortal02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$02000378_BF__04_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round04_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[104])


class Round04_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1004], arg2=False) # 수호대상 틴차이
        set_conversation(type=1, spawnId=1004, script='$02000378_BF__04_FINDWAY__4$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=904, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='04RoundSuccess', value=1):
            return Round04_Sucess02()


class Round04_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2004, patrolName='MS2PatrolData_2004')
        destroy_monster(spawnIds=[1004])
        create_monster(spawnIds=[104], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3004], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh_animation(triggerIds=[3004], visible=False, arg3=0, arg4=0) # CrystalOff
        set_effect(triggerIds=[5204], visible=True) # Sound_CrystalOn
        set_portal(portalId=21, visible=True, enabled=True, minimapVisible=False)
        set_conversation(type=1, spawnId=104, script='$02000378_BF__04_FINDWAY__5$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round04_RouteSelect()


class Round04_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2004])
        create_monster(spawnIds=[204], arg2=False) # 연출용 준타
        move_npc(spawnId=104, patrolName='MS2PatrolData_104New')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound12()
        """
        <condition name="랜덤조건" arg1="50">    
                    <transition state="Round04_PickRoute_Left"/>    
                </condition> 
                <condition name="랜덤조건" arg1="50"> 
                    <transition state="Round04_PickRoute_Right" />
                </condition>
        """


class GoToRound12(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])
        move_npc(spawnId=204, patrolName='MS2PatrolData_204New')
        set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[204])


