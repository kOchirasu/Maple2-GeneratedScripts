""" trigger/52000025_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=False) # 렌듀비앙
        set_effect(triggerIds=[7001], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[20002235], questStates=[1], jobCode=90):
            return start()
        if quest_user_detected(boxIds=[701], questIds=[20002235], questStates=[2], jobCode=90):
            return start_B()
        if quest_user_detected(boxIds=[701], questIds=[20002235], questStates=[3], jobCode=90):
            return start_B()


class start_B(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202,299], arg2=False) # 이슈라 퀘스트
        destroy_monster(spawnIds=[203,204,205])


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,203,204], arg2=False) # 이슈라
        create_monster(spawnIds=[101,102], arg2=False) # 적 몬스터 1차

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102]):
            return start_02()

    def on_exit(self):
        set_conversation(type=1, spawnId=201, script='$52000025_QD__MAIN__0$', arg4=2, arg5=1)


class start_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,112,113,114,115,116], arg2=False) # 적 몬스터 2차
        set_conversation(type=1, spawnId=201, script='$52000025_QD__MAIN__1$', arg4=2, arg5=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114,115,116]):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN__2$', arg4=4) # 음성 코드 00001288
        set_effect(triggerIds=[7001], visible=True) # 음성 코드 00001288

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_04()


class start_04(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_2000') # 이슈라를 이동시킨다
        set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN__3$', arg4=6) # 음성 코드 00001289
        set_effect(triggerIds=[7004], visible=True) # 음성 코드 00001289

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return start_05()

    def on_exit(self):
        set_cinematic_ui(type=4)


class start_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[203,204,205])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Start_06()

    def on_exit(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        move_user(mapId=52000025, portalId=99)


class Start_06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=201, patrolName='MS2PatrolData_2001') # 이슈라를 이동시킨다
        move_user_path(patrolName='MS2PatrolData_2002') # 유저를 이동시킨다
        select_camera_path(pathIds=[8001,8002], returnView=False) # 카메라 뒤로 당김

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start_07()


class Start_07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN__4$', arg4=3) # 렌듀비앙 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start_08()


class Start_08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN__5$', arg4=5)
        set_effect(triggerIds=[7002], visible=True) # 음성 코드 00001290

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Start_09()


class Start_09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN__6$', arg4=4) # 렌듀비앙 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Start_10()


class Start_10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN__7$', arg4=3) # 렌듀비앙 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Start_11()

    def on_exit(self):
        select_camera(triggerId=8001, enable=False) # 카메라 초기화


class Start_11(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201]) # 이슈라
        create_monster(spawnIds=[299], arg2=False) # 이슈라 퀘스트
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=701, type='trigger', achieve='SweepthePriates')


