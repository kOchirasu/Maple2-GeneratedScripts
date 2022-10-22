""" trigger/52000050_qd/main_01.xml """
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
        set_effect(triggerIds=[7011], visible=False) # 참새 조용함
        set_breakable(triggerIds=[9001,9002,9003,9004,9005], enabled=False) # 참새들 조용히 있음
        set_visible_breakable_object(triggerIds=[9001,9002,9003,9004,9005], arg2=False) # 참새들 조용히 있음
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[101,102,103], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[3]):
            return quest_end()
        if quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[2]):
            return quest_end()
        if quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[3]):
            return start_02_resume()
        if quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[2]):
            return start_02_j_resume()
        if quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[1]):
            return start_02_resume()
        if quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[3]):
            return start_02_Ready()
        if quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[2]):
            return start_02_Ready()
        if quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[1]):
            return start()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[101,102]) # 퀘스트용 소멸
        create_monster(spawnIds=[111,112], arg2=False) # 연출용 리젠
        move_npc(spawnId=112, patrolName='MS2PatrolData_1201') # 연출용 틴차이 이동
        set_conversation(type=1, spawnId=112, script='$52000050_QD__MAIN_01__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=112, script='$52000050_QD__MAIN_01__0$', arg4=2, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_achievement(triggerId=701, type='trigger', achieve='MovetoNewHouse')
            return ready_02()


class ready_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[112]) # 퀘스트용 소멸
        create_monster(spawnIds=[122], arg2=False) # 퀘스트용 리젠

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[1]):
            return start_02()


class start_02_Ready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102])
        create_monster(spawnIds=[111,122], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[1]):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102]) # 퀘스트용 소멸
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=111, patrolName='MS2PatrolData_1101') # 연출용 틴차이 이동
        select_camera_path(pathIds=[8005], returnView=False)
        set_conversation(type=2, spawnId=11001557, script='$52000050_QD__MAIN_01__1$', arg4=4)
        move_npc(spawnId=122, patrolName='MS2PatrolData_1205') # 연출용 틴차이 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user_path(patrolName='MS2PatrolData_9901')
            return start_02_b()


class start_02_resume(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102])
        create_monster(spawnIds=[111,122], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=111, patrolName='MS2PatrolData_1101') # 연출용 틴차이 이동
        select_camera_path(pathIds=[8005], returnView=False)
        set_conversation(type=2, spawnId=11001557, script='$52000050_QD__MAIN_01__2$', arg4=4)
        move_npc(spawnId=122, patrolName='MS2PatrolData_1205') # 연출용 틴차이 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user_path(patrolName='MS2PatrolData_9901')
            return start_02_b()


class start_02_b(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=3000)
        set_conversation(type=2, spawnId=11001557, script='$52000050_QD__MAIN_01__3$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_02_c()


class start_02_c(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__4$', arg4=3)
        set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_02_d()


class start_02_d(state.State):
    def on_enter(self):
        move_npc(spawnId=122, patrolName='MS2PatrolData_1202') # 연출용 틴차이 이동
        set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__5$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_02_e()


class start_02_e(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_breakable(triggerIds=[9001,9002,9003,9004,9005], enabled=True) # 참새들 조용히 있음
        set_visible_breakable_object(triggerIds=[9001,9002,9003,9004,9005], arg2=True) # 참새들 조용히 있음

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            set_mesh(triggerIds=[6001,6002,6003,6004,6005], visible=True)
            set_mesh_animation(triggerIds=[6001,6002,6003,6004,6005], visible=True, arg3=0, arg4=0)
            return start_02_f()


class start_02_f(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_effect(triggerIds=[7011], visible=True)
            return start_02_g()


class start_02_g(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003,8004], returnView=False)
        set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_breakable(triggerIds=[9001,9002,9003,9004,9005], enabled=False)
            set_visible_breakable_object(triggerIds=[9001,9002,9003,9004,9005], arg2=False)
            move_npc(spawnId=122, patrolName='MS2PatrolData_1203')
            return start_02_h()


class start_02_h(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__6$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_02_i()


class start_02_i(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3000)
        set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__7$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_achievement(triggerId=701, type='trigger', achieve='SingingOfBirds')
            return start_02_j()


class start_02_j(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=True)
        destroy_monster(spawnIds=[111]) # 퀘스트용 소멸
        create_monster(spawnIds=[121], arg2=False) # 퀘스트용 리젠
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[2]):
            return start_02_k()


class start_02_j_resume(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102])
        destroy_monster(spawnIds=[111]) # 퀘스트용 소멸
        create_monster(spawnIds=[121,122], arg2=False) # 퀘스트용 리젠
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_mesh(triggerIds=[6001,6002,6003,6004,6005], visible=True) # 참새들 표시
        set_effect(triggerIds=[7011], visible=True) # 참새 조용함

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[2]):
            return start_02_k()


class start_02_k(state.State):
    def on_enter(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_1204') # 연출용 준타 이동
        move_npc(spawnId=122, patrolName='MS2PatrolData_1204') # 연출용 틴차이 이동


class quest_end(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102]) # 퀘스트용 소멸


