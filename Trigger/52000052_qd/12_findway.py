""" trigger/52000052_qd/12_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=4000, visible=True, initialSequence='or_fi_struc_stonegate_A01_off') # StoneGate
        set_effect(triggerIds=[5012], visible=False) # 12Round_BridgeApp
        set_effect(triggerIds=[5013], visible=False) # Sound_StoneGate
        set_mesh(triggerIds=[331200,331201,331202,331203,331204,331205,331206,331207,331208,331209,331210,331211,331212,331213,331214,331215,331216,331217,331218,331219,331220,331221,331222,331223,331224,331225,331226,331227,331228,331229,331230,331231,331232,331233,331234,331235,331236,331237,331238,331239,331240,331241,331242,331243,331244,331245,331246,331247,331248,331249,331250,331251,331252,331253,331254,331255,331256,331257,331258,331259,331260,331261,331262,331263,331264,331265,331266,331267,331268,331269,331270,331271,331272,331273,331274,331275,331276,331277], visible=False, arg3=0, arg4=0, arg5=0) # Stairs
        set_mesh(triggerIds=[4032], visible=True, arg3=0, arg4=0, arg5=0) # RoundBarrier
        set_mesh(triggerIds=[3012], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3112], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3012], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3112], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5212], visible=False) # Sound_CrystalOn
        set_user_value(key='FindWay', value=0)
        set_agent(triggerIds=[28120], visible=True)
        set_agent(triggerIds=[28121], visible=True)
        set_agent(triggerIds=[28122], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='FindWay', value=1):
            return MovingDelay01()


class MovingDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn01()


class ReadyToWalkIn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[112,212], arg2=False) # 연출용
        set_mesh(triggerIds=[4032], visible=False, arg3=0, arg4=0, arg5=0) # RoundBarrier
        move_npc(spawnId=112, patrolName='MS2PatrolData_112')
        move_npc(spawnId=212, patrolName='MS2PatrolData_212')
        set_conversation(type=1, spawnId=212, script='$52000052_QD__12_FINDWAY__0$', arg4=3, arg5=1) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=112, script='$52000052_QD__12_FINDWAY__1$', arg4=3, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round12_Start()


class Round12_Start(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[112,212])
        create_monster(spawnIds=[1012], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2012], arg2=False) # 전투용 준타
        set_conversation(type=1, spawnId=1012, script='$52000052_QD__12_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        set_user_value(triggerId=912, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='12RoundSuccess', value=1):
            return Round12_Sucess01()


#  20170223 업데이트 던전 개편 단축 
class Round12_Sucess01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9012, spawnIds=[2212]):
            return Round12_Sucess02()


class Round12_Sucess02(state.State):
    def on_enter(self):
        move_npc(spawnId=2212, patrolName='MS2PatrolData_2012')
        destroy_monster(spawnIds=[1012])
        create_monster(spawnIds=[113], arg2=False) # 연출용 틴차이
        set_mesh(triggerIds=[3012], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3112], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3012], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3112], visible=True, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5212], visible=True) # Sound_CrystalOn
        set_agent(triggerIds=[28120], visible=False)
        set_agent(triggerIds=[28121], visible=False)
        set_agent(triggerIds=[28122], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round12_RouteSelect()


class Round12_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2213,2212])
        create_monster(spawnIds=[213], arg2=False) # 연출용 준타
        set_conversation(type=1, spawnId=113, script='$52000052_QD__12_FINDWAY__3$', arg4=3, arg5=0) # 틴차이
        move_npc(spawnId=113, patrolName='MS2PatrolData_199')
        move_npc(spawnId=213, patrolName='MS2PatrolData_299')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Round12_RouteApp01()


class Round12_RouteApp01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5012], visible=True) # 12Round_BridgeApp
        set_random_mesh(triggerIds=[331200,331201,331202,331203,331204,331205,331206,331207,331208,331209,331210,331211,331212,331213,331214,331215,331216,331217,331218,331219,331220,331221,331222,331223,331224,331225,331226,331227,331228,331229,331230,331231,331232,331233,331234,331235,331236,331237,331238,331239,331240,331241,331242,331243,331244,331245,331246,331247,331248,331249,331250,331251,331252,331253,331254,331255,331256,331257,331258,331259,331260,331261,331262,331263,331264,331265,331266,331267,331268,331269,331270,331271,331272,331273,331274,331275,331276,331277], visible=True, meshCount=78, arg4=100, delay=30) # Stairs

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round12_RouteApp02()


class Round12_RouteApp02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5013], visible=False) # Sound_StoneGate

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Round12_RouteApp03()


class Round12_RouteApp03(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='or_fi_struc_stonegate_A01_on') # StoneGate
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9013, spawnIds=[213]):
            return GoToNextMap01()


class GoToNextMap01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[213])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToNextMap02()


class GoToNextMap02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[113])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


