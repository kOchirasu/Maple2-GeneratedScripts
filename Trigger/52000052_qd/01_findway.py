""" trigger/52000052_qd/01_findway.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, arg3=0, arg4=0, arg5=0) # MobGround_AlawaysOff
        set_mesh(triggerIds=[4001,4002,4003,4004,4005,4006,4007,4008], visible=True, arg3=0, arg4=0, arg5=0) # LaserTotemBarrier_AlawaysOn
        set_mesh(triggerIds=[4100,4101,4102,4103,4104,4105,4106], visible=False, arg3=0, arg4=0, arg5=0) # JuntaFlyGround_AlawaysOff
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3101], visible=False, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3001], visible=True, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3101], visible=False, arg3=0, arg4=0) # CrystalOn
        set_effect(triggerIds=[5201], visible=False) # Sound_CrystalOn
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=1):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[100,200], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Dialogue01()


class Dialogue01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=500, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Dialogue02()


class Dialogue02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001557, script='$52000052_QD__01_FINDWAY__0$', arg4=5) # 준타
        set_skip(state=Dialogue02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue02Skip()


class Dialogue02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=500, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToWalkIn01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class ReadyToWalkIn01(state.State):
    def on_enter(self):
        move_npc(spawnId=100, patrolName='MS2PatrolData_100')
        move_npc(spawnId=200, patrolName='MS2PatrolData_200')
        set_conversation(type=1, spawnId=200, arg4=3, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToWalkIn02()


class ReadyToWalkIn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=1301, key='RouteSelected', value=1)
        set_user_value(triggerId=2301, key='RouteSelected', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToWalkIn03()


class ReadyToWalkIn03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=200, script='$52000052_QD__01_FINDWAY__1$', arg4=3, arg5=0) # 준타
        set_conversation(type=1, spawnId=100, script='$52000052_QD__01_FINDWAY__2$', arg4=2, arg5=3) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return Round01_Start()

    def on_exit(self):
        destroy_monster(spawnIds=[100,200])


class Round01_Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False) # 수호대상 틴차이
        create_monster(spawnIds=[2001], arg2=False) # 전투용 준타
        set_user_value(triggerId=901, key='MobWaveStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='01RoundSuccess', value=1):
            return Round01_Sucess()


class Round01_Sucess(state.State):
    def on_enter(self):
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001')
        destroy_monster(spawnIds=[1001])
        create_monster(spawnIds=[101], arg2=False) # 연출용 틴차이
        set_effect(triggerIds=[5201], visible=True) # Sound_CrystalOn
        set_mesh(triggerIds=[3001], visible=False, arg3=100, arg4=0, arg5=0) # CrystalOff
        set_mesh(triggerIds=[3101], visible=True, arg3=0, arg4=0, arg5=0) # CrystalOn
        set_mesh_animation(triggerIds=[3001], visible=False, arg3=0, arg4=0) # CrystalOff
        set_mesh_animation(triggerIds=[3101], visible=True, arg3=0, arg4=0) # CrystalOn
        set_conversation(type=1, spawnId=101, script='$52000052_QD__01_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round01_RouteSelect()


class Round01_RouteSelect(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2001])
        create_monster(spawnIds=[201], arg2=False) # 연출용 준타

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round01_PickRoute_Left()
        if random_condition(rate=50):
            return Round01_PickRoute_Right()


class Round01_PickRoute_Left(state.State):
    def on_enter(self):
        set_user_value(triggerId=1301, key='MakeTrue', value=1)
        set_user_value(triggerId=2301, key='MakeFalse', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound02()


class GoToRound02(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Round01_PickRoute_Right(state.State):
    def on_enter(self):
        set_user_value(triggerId=1301, key='MakeFalse', value=1)
        set_user_value(triggerId=2301, key='MakeTrue', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return GoToRound03()


class GoToRound03(state.State):
    def on_enter(self):
        set_user_value(triggerId=3, key='FindWay', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Quit()


class Quit(state.State):
    pass


