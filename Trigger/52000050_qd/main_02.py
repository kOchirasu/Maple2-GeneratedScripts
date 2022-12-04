""" trigger/52000050_qd/main_02.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=7001, visible=False, initialSequence='Sit_Down_A') # 준타
        self.set_actor(triggerId=7002, visible=False, initialSequence='Down_Idle_A') # 틴차이
        self.set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025,6026,6027,6028,6029,6030], visible=False, arg3=0, delay=0, scale=0) # 짹쨱이
        self.set_mesh(triggerIds=[6011], visible=True, arg3=0, delay=0, scale=0) # 원래 벽돌 안보이게
        self.set_interact_object(triggerIds=[10000478], state=1)
        self.set_effect(triggerIds=[7010], visible=False)
        self.set_breakable(triggerIds=[9010,9011,9012,9013,9014], enable=False) # 참새들 조용히 있음
        self.set_visible_breakable_object(triggerIds=[9010,9011,9012,9013,9014], visible=False) # 참새들 조용히 있음

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003059], questStates=[1]):
            return start_c(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003058], questStates=[2]):
            return start_c(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003058], questStates=[1]):
            return start_b(self.ctx)


class start_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7011], visible=True)
        self.set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025], visible=True, arg3=0, delay=0, scale=0) # 짹쨱이
        self.set_mesh_animation(triggerIds=[6020,6021,6022,6023,6024,6025], visible=True, arg3=0, arg4=0)
        self.destroy_monster(spawnIds=[101,102,103,111,112,121,122]) # 퀘스트용 소멸
        self.set_actor(triggerId=7001, visible=True, initialSequence='Sit_Down_A') # 준타
        self.set_actor(triggerId=7002, visible=True, initialSequence='Down_Idle_A') # 틴차이
        self.set_mesh(triggerIds=[6010], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[6011], visible=False, arg3=0, delay=0, scale=0) # 원래 벽돌 안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000478], stateValue=0):
            return start_b_02(self.ctx)


class start_b_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.move_user(mapId=52000048, portalId=1)
            return None # Missing State: start_02_end


class start_c(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6020,6021,6022,6023,6024], visible=True, arg3=0, delay=0, scale=0) # 짹쨱이
        self.set_mesh_animation(triggerIds=[6020,6021,6022,6023,6024,6025], visible=True, arg3=0, arg4=0)
        self.destroy_monster(spawnIds=[101,102,111,112,121,122]) # 퀘스트용 소멸
        self.set_actor(triggerId=7001, visible=True, initialSequence='Sit_Down_A') # 준타
        self.set_actor(triggerId=7002, visible=True, initialSequence='Down_Idle_A') # 틴차이
        self.set_mesh(triggerIds=[6010], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh_animation(triggerIds=[6010], visible=True, arg3=0, arg4=0)
        self.set_interact_object(triggerIds=[10000478], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003059], questStates=[1]):
            self.move_user(mapId=52000050, portalId=2)
            return start_c_02(self.ctx)


class start_c_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025], visible=False, arg3=0, delay=0, scale=0) # 짹쨱이
        self.set_mesh(triggerIds=[6026,6027,6028,6029,6030], visible=True, arg3=0, delay=0, scale=0) # 짹쨱이
        self.set_mesh_animation(triggerIds=[6026,6027,6028,6029,6030], visible=True, arg3=0, arg4=0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8010,8011,8001], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_9902') # 유저를 이동시킨다
        self.set_conversation(type=1, spawnId=0, script='$52000050_QD__MAIN_02__0$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_c_03(self.ctx)


class start_c_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000050_QD__MAIN_02__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_c_04(self.ctx)


class start_c_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000050_QD__MAIN_02__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_c_05(self.ctx)


class start_c_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[9010,9011,9012,9013,9014], enable=True) # 참새들 조용히 있음
        self.set_visible_breakable_object(triggerIds=[9010,9011,9012,9013,9014], visible=True) # 참새들 조용히 있음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.set_mesh(triggerIds=[6026,6027,6028,6029,6030], visible=False, arg3=0, delay=0, scale=0)
            return start_c_06(self.ctx)


class start_c_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7011], visible=False) # 지저귐 삭제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[8001], returnView=True)
        self.set_achievement(triggerId=701, type='trigger', achieve='FlyingBirds') # 퀘스트 목표 체크용 업적이벤트 발생

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.set_breakable(triggerIds=[9010,9011,9012,9013,9014], enable=False)
            self.set_visible_breakable_object(triggerIds=[9010,9011,9012,9013,9014], visible=False)
            return start_c_07(self.ctx)


class start_c_07(trigger_api.Trigger):
    pass


initial_state = ready
