""" trigger/52000049_qd/main_01.xml """
from common import *
import state


#  
# [출연진]
# 101 : 준타 (퀘스트)
# 111,121 : 준타 (연출)
# 102,122 : 틴차이 (퀘스트)
# 112 : 틴차이 (연출)
# 103 : 애니마르 에너지
#  
class ready(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8099], isEnable=False)
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False) # 연출용 라오즈리젠
        set_mesh(triggerIds=[2116], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[2201,2202,2203,2204,2205,2206], visible=False, arg3=0, arg4=0, arg5=0) # 투명 발판

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[1]):
            return start()
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[2]):
            return start_23()
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[3]):
            return start_23()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_2001') # 유저를 이동시킨다
        select_camera_path(pathIds=[8001,8002,8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7012], visible=True)
        set_mesh(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115], visible=False, arg3=0, arg4=100, arg5=8) # 모니터 켜짐
        set_mesh(triggerIds=[2116], visible=True, arg3=0, arg4=100, arg5=3)
        create_monster(spawnIds=[101], arg2=False) # 연출용 리젠 칸두라
        move_user_path(patrolName='MS2PatrolData_2002') # 유저를 이동시킨다
        set_conversation(type=2, spawnId=11001761, script='$52000049_QD__MAIN_01__0$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7012], visible=False)
        set_conversation(type=1, spawnId=0, script='$52000049_QD__MAIN_01__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_04()


class start_04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001761, script='$52000049_QD__MAIN_01__2$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_05()


class start_05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001761, script='$52000049_QD__MAIN_01__3$', arg4=4)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Event_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            select_camera_path(pathIds=[8004], returnView=False)
            return start_06()


class start_06(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            destroy_monster(spawnIds=[301,302,303,304,305,306])
            return start_07()


class start_07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001,7002,7003,7004,7005,7006], visible=True)
        create_monster(spawnIds=[201,202,203,204,205,206], arg2=False) # 연출용 비전 리젠

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_08()


class start_08(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2003') # 유저를 이동시킨다
        select_camera_path(pathIds=[8005,8006,8007], returnView=False)
        set_conversation(type=2, spawnId=11001761, script='$52000049_QD__MAIN_01__4$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_09()


class start_09(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000049_QD__MAIN_01__5$', arg4=3, arg5=0)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_A','Emotion_Failure_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_10()


class start_10(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000049_QD__MAIN_01__6$', arg4=3, arg5=0)
        set_pc_emotion_loop(sequenceName='Emotion_Failure_Idle_A', duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_11()


class start_11(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001761, script='$52000049_QD__MAIN_01__7$', arg4=4)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Event_A')
        select_camera_path(pathIds=[8008], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_12()


class start_12(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2004') # 유저를 이동시킨다
        select_camera_path(pathIds=[8009], returnView=False)
        set_conversation(type=2, spawnId=11001761, script='$52000049_QD__MAIN_01__8$', arg4=4)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_D')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_13()


class start_13(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7010], visible=True)
        move_npc(spawnId=201, patrolName='MS2PatrolData_2011') # 비전 클론 이동
        move_npc(spawnId=202, patrolName='MS2PatrolData_2012') # 비전 클론 이동
        move_npc(spawnId=203, patrolName='MS2PatrolData_2013') # 비전 클론 이동
        move_npc(spawnId=204, patrolName='MS2PatrolData_2014') # 비전 클론 이동
        move_npc(spawnId=205, patrolName='MS2PatrolData_2015') # 비전 클론 이동
        move_npc(spawnId=206, patrolName='MS2PatrolData_2016') # 비전 클론 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_14()


class start_14(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7011], visible=True)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Failure_A','Emotion_Failure_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_15()


class start_15(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Emotion_Failure_Idle_A', duration=18000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_16()


class start_16(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_17()


class start_17(state.State):
    def on_enter(self):
        create_monster(spawnIds=[501], arg2=False) # 연출용 리젠 준타
        select_camera_path(pathIds=[8010,8011,8012], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            set_skill(triggerIds=[8099], isEnable=True)
            move_npc(spawnId=201, patrolName='MS2PatrolData_2021')
            move_npc(spawnId=202, patrolName='MS2PatrolData_2022')
            move_npc(spawnId=203, patrolName='MS2PatrolData_2023')
            move_npc(spawnId=204, patrolName='MS2PatrolData_2024')
            move_npc(spawnId=205, patrolName='MS2PatrolData_2025')
            move_npc(spawnId=206, patrolName='MS2PatrolData_2026')
            set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B')
            set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_B')
            set_npc_emotion_sequence(spawnId=203, sequenceName='Bore_B')
            set_npc_emotion_sequence(spawnId=204, sequenceName='Bore_B')
            set_npc_emotion_sequence(spawnId=205, sequenceName='Bore_B')
            set_npc_emotion_sequence(spawnId=206, sequenceName='Bore_B')
            return start_18()


class start_18(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_effect(triggerIds=[7010], visible=False)
            destroy_monster(spawnIds=[201,202,203,204,205,206])
            return start_19()


class start_19(state.State):
    def on_enter(self):
        move_npc(spawnId=501, patrolName='MS2PatrolData_2030') # 준타 이동
        set_conversation(type=1, spawnId=501, script='$52000049_QD__MAIN_01__9$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_conversation(type=1, spawnId=101, script='$52000049_QD__MAIN_01__10$', arg4=3, arg5=0)
            move_npc(spawnId=101, patrolName='MS2PatrolData_2099')
            return start_20()


class start_20(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_achievement(triggerId=701, type='trigger', achieve='HeroJunta')
            set_mesh(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115], visible=True, arg3=0, arg4=100, arg5=8)
            destroy_monster(spawnIds=[101])
            select_camera_path(pathIds=[8013], returnView=True)
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return start_21()


class start_21(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[2]):
            destroy_monster(spawnIds=[501])
            create_monster(spawnIds=[502], arg2=False)
            return start_22()


class start_22(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[1]):
            move_user(mapId=52000050, portalId=1)
            return end()


class start_23(state.State):
    def on_enter(self):
        create_monster(spawnIds=[502], arg2=False) # 연출용 리젠 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_22()


class end(state.State):
    pass


