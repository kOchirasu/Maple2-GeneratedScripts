""" trigger/52000050_qd/main_01.xml """
import trigger_api


# [출연진]
# 101 : 준타 (퀘스트)
# 111,121 : 준타 (연출)
# 102,122 : 틴차이 (퀘스트)
# 112 : 틴차이 (연출)
# 103 : 애니마르 에너지
class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7011], visible=False) # 참새 조용함
        self.set_breakable(triggerIds=[9001,9002,9003,9004,9005], enable=False) # 참새들 조용히 있음
        self.set_visible_breakable_object(triggerIds=[9001,9002,9003,9004,9005], visible=False) # 참새들 조용히 있음
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[3]):
            return quest_end(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[2]):
            return quest_end(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[3]):
            return start_02_resume(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[2]):
            return start_02_j_resume(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[1]):
            return start_02_resume(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[3]):
            return start_02_Ready(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[2]):
            return start_02_Ready(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101,102]) # 퀘스트용 소멸
        self.create_monster(spawnIds=[111,112], animationEffect=False) # 연출용 리젠
        self.move_npc(spawnId=112, patrolName='MS2PatrolData_1201') # 연출용 틴차이 이동
        self.set_conversation(type=1, spawnId=112, script='$52000050_QD__MAIN_01__8$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=112, script='$52000050_QD__MAIN_01__0$', arg4=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_achievement(triggerId=701, type='trigger', achieve='MovetoNewHouse')
            return ready_02(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[112]) # 퀘스트용 소멸
        self.create_monster(spawnIds=[122], animationEffect=False) # 퀘스트용 리젠

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[1]):
            return start_02(self.ctx)


class start_02_Ready(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102])
        self.create_monster(spawnIds=[111,122], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003055], questStates=[1]):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102]) # 퀘스트용 소멸
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_1101') # 연출용 틴차이 이동
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.set_conversation(type=2, spawnId=11001557, script='$52000050_QD__MAIN_01__1$', arg4=4)
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_1205') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user_path(patrolName='MS2PatrolData_9901')
            return start_02_b(self.ctx)


class start_02_resume(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102])
        self.create_monster(spawnIds=[111,122], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_1101') # 연출용 틴차이 이동
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.set_conversation(type=2, spawnId=11001557, script='$52000050_QD__MAIN_01__2$', arg4=4)
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_1205') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user_path(patrolName='MS2PatrolData_9901')
            return start_02_b(self.ctx)


class start_02_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=3000)
        self.set_conversation(type=2, spawnId=11001557, script='$52000050_QD__MAIN_01__3$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_02_c(self.ctx)


class start_02_c(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__4$', arg4=3)
        self.set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_02_d(self.ctx)


class start_02_d(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_1202') # 연출용 틴차이 이동
        self.set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__5$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_02_e(self.ctx)


class start_02_e(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_breakable(triggerIds=[9001,9002,9003,9004,9005], enable=True) # 참새들 조용히 있음
        self.set_visible_breakable_object(triggerIds=[9001,9002,9003,9004,9005], visible=True) # 참새들 조용히 있음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            self.set_mesh(triggerIds=[6001,6002,6003,6004,6005], visible=True)
            self.set_mesh_animation(triggerIds=[6001,6002,6003,6004,6005], visible=True, arg3=0, arg4=0)
            return start_02_f(self.ctx)


class start_02_f(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_effect(triggerIds=[7011], visible=True)
            return start_02_g(self.ctx)


class start_02_g(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003,8004], returnView=False)
        self.set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_breakable(triggerIds=[9001,9002,9003,9004,9005], enable=False)
            self.set_visible_breakable_object(triggerIds=[9001,9002,9003,9004,9005], visible=False)
            self.move_npc(spawnId=122, patrolName='MS2PatrolData_1203')
            return start_02_h(self.ctx)


class start_02_h(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__6$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return start_02_i(self.ctx)


class start_02_i(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3000)
        self.set_conversation(type=2, spawnId=11001708, script='$52000050_QD__MAIN_01__7$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_achievement(triggerId=701, type='trigger', achieve='SingingOfBirds')
            return start_02_j(self.ctx)


class start_02_j(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=True)
        self.destroy_monster(spawnIds=[111]) # 퀘스트용 소멸
        self.create_monster(spawnIds=[121], animationEffect=False) # 퀘스트용 리젠
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[2]):
            return start_02_k(self.ctx)


class start_02_j_resume(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102])
        self.destroy_monster(spawnIds=[111]) # 퀘스트용 소멸
        self.create_monster(spawnIds=[121,122], animationEffect=False) # 퀘스트용 리젠
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005], visible=True) # 참새들 표시
        self.set_effect(triggerIds=[7011], visible=True) # 참새 조용함

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003056], questStates=[2]):
            return start_02_k(self.ctx)


class start_02_k(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=121, patrolName='MS2PatrolData_1204') # 연출용 준타 이동
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_1204') # 연출용 틴차이 이동


class quest_end(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102]) # 퀘스트용 소멸


initial_state = ready
