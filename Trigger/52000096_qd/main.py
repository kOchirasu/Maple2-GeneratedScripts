""" trigger/52000096_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001514], questStates=[1]):
            return 몹소환01()
        if quest_user_detected(boxIds=[9000], questIds=[50100040], questStates=[1]):
            return 몹소환01()


class 몹소환01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8001], returnView=False)
        create_monster(spawnIds=[1001], arg2=False) # 몬스터 스폰포인트 1
        create_monster(spawnIds=[1002], arg2=False) # 몬스터 스폰포인트 2
        create_monster(spawnIds=[1003], arg2=False) # 몬스터 스폰포인트 3
        create_monster(spawnIds=[1004], arg2=False) # 몬스터 스폰포인트 4

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 위협당함01()


class 위협당함01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1001, script='$52000096_QD__MAIN__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 위협당함02()


class 위협당함02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1002, script='$52000096_QD__MAIN__1$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 위협당함03()


class 위협당함03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1003, script='$52000096_QD__MAIN__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 위협당함04()


class 위협당함04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1004, script='$52000096_QD__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시점이동()


class 시점이동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 경로이동()


class 경로이동(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000096_QD__MAIN__4$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 몹말풍선01()


class 몹말풍선01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=3)
        set_conversation(type=1, spawnId=1003, script='$52000096_QD__MAIN__5$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC_01')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터재스폰()


class 몬스터재스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=True) # 몬스터 스폰포인트 1
        create_monster(spawnIds=[1002], arg2=True) # 몬스터 스폰포인트 2
        create_monster(spawnIds=[1003], arg2=True) # 몬스터 스폰포인트 3
        create_monster(spawnIds=[1004], arg2=True) # 몬스터 스폰포인트 4

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


