""" trigger/52000024_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[20002233], questStates=[1]):
            return start()
        if quest_user_detected(boxIds=[701], questIds=[20002233], questStates=[2]):
            return start()
        if quest_user_detected(boxIds=[701], questIds=[20002233], questStates=[3]):
            return start_B()


class start_B(state.State):
    def on_enter(self):
        create_monster(spawnIds=[106], arg2=False) # 유페리아
        create_monster(spawnIds=[101], arg2=False) # 레잔


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        move_user_path(patrolName='MS2PatrolData_2101') # 유저를 이동시킨다
        create_monster(spawnIds=[101], arg2=False) # 레잔
        create_monster(spawnIds=[102], arg2=False) # 유페리아
        create_monster(spawnIds=[103], arg2=False) # 이슈라
        select_camera_path(pathIds=[8001,8002,8003], returnView=False) # 카메라 뒤로 당김

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Start_02()


class Start_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Start_03()


class Start_03(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_2001') # 이슈라를 이동시킨다
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002') # 유페리아를 이동시킨다

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Start_04()


class Start_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7006], visible=True)
        set_conversation(type=2, spawnId=11001564, script='$52000024_QD__MAIN__0$', arg4=5) # 유페리아 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Start_05()

    def on_exit(self):
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[104], arg2=False) # 이슈라


class Start_05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=8004, enable=False) # 카메라 초기화

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return startB_01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class startB_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=8005, enable=True) # 카메라 초기화
        move_user(mapId=52000024, portalId=99)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return startB_02()


class startB_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return startB_04()


class startB_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005,8006], returnView=False) # 카메라 뒤로 당김
        set_effect(triggerIds=[7003], visible=True) # 음성 코드 00001283
        set_conversation(type=2, spawnId=11001244, script='$52000024_QD__MAIN__1$', arg4=3) # 음성 코드 00001283

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return startB_07()


class startB_07(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=False)
        set_effect(triggerIds=[7001], visible=True) # 음성 코드 03000870
        set_conversation(type=2, spawnId=11001570, script='$52000024_QD__MAIN__2$', arg4=7) # 음성 코드 03000870

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return startB_08()


class startB_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007,8008], returnView=False) # 카메라 뒤로 당김
        move_npc(spawnId=104, patrolName='MS2PatrolData_2006') # 이슈라 슌을 바라봄
        move_npc(spawnId=102, patrolName='MS2PatrolData_2005') # 유페리아 슌을 바라봄
        move_user_path(patrolName='MS2PatrolData_2102') # 유저를 이동시킨다

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return startB_09()


class startB_09(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_2008') # 이슈라 슌을 바라봄
        set_conversation(type=2, spawnId=11001244, script='$52000024_QD__MAIN__3$', arg4=5) # 음성 코드 00001287
        set_effect(triggerIds=[7004], visible=True) # 음성 코드 00001287

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return startB_10()


class startB_10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001570, script='$52000024_QD__MAIN__4$', arg4=2) # 음성 코드 03000871
        set_effect(triggerIds=[7002], visible=True) # 음성 코드 03000871

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return startB_11()


class startB_11(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_2007') # 슌 집에감

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return startB_12()


class startB_12(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105]) # 슌 사라짐
        select_camera(triggerId=8005, enable=False) # 카메라 초기화
        set_achievement(triggerId=701, type='trigger', achieve='PirateRiddenSea')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[20002233], questStates=[3]):
            return startC_01()


class startC_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$52000024_QD__MAIN__5$', arg4=3, arg5=0) # 음성 코드 00001309
        set_effect(triggerIds=[7005], visible=True) # 음성 코드 00001309

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return startC_02()


class startC_02(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        move_npc(spawnId=104, patrolName='MS2PatrolData_2007') # 이슈라 집에감

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return startC_03()


class startC_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104]) # 이슈라 사라짐

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return startD_01()


class startD_01(state.State):
    pass


