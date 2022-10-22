""" trigger/52000050_qd/main_02.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        set_actor(triggerId=7001, visible=False, initialSequence='Sit_Down_A') # 준타
        set_actor(triggerId=7002, visible=False, initialSequence='Down_Idle_A') # 틴차이
        set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025,6026,6027,6028,6029,6030], visible=False, arg3=0, arg4=0, arg5=0) # 짹쨱이
        set_mesh(triggerIds=[6011], visible=True, arg3=0, arg4=0, arg5=0) # 원래 벽돌 안보이게
        set_interact_object(triggerIds=[10000478], state=1)
        set_effect(triggerIds=[7010], visible=False)
        set_breakable(triggerIds=[9010,9011,9012,9013,9014], enabled=False) # 참새들 조용히 있음
        set_visible_breakable_object(triggerIds=[9010,9011,9012,9013,9014], arg2=False) # 참새들 조용히 있음

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003059], questStates=[1]):
            return start_c()
        if quest_user_detected(boxIds=[701], questIds=[10003058], questStates=[2]):
            return start_c()
        if quest_user_detected(boxIds=[701], questIds=[10003058], questStates=[1]):
            return start_b()


class start_b(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7011], visible=True)
        set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025], visible=True, arg3=0, arg4=0, arg5=0) # 짹쨱이
        set_mesh_animation(triggerIds=[6020,6021,6022,6023,6024,6025], visible=True, arg3=0, arg4=0)
        destroy_monster(spawnIds=[101,102,103,111,112,121,122]) # 퀘스트용 소멸
        set_actor(triggerId=7001, visible=True, initialSequence='Sit_Down_A') # 준타
        set_actor(triggerId=7002, visible=True, initialSequence='Down_Idle_A') # 틴차이
        set_mesh(triggerIds=[6010], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[6011], visible=False, arg3=0, arg4=0, arg5=0) # 원래 벽돌 안보이게

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000478], arg2=0):
            return start_b_02()


class start_b_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7010], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            move_user(mapId=52000048, portalId=1)
            return None # Missing State: start_02_end


class start_c(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6020,6021,6022,6023,6024], visible=True, arg3=0, arg4=0, arg5=0) # 짹쨱이
        set_mesh_animation(triggerIds=[6020,6021,6022,6023,6024,6025], visible=True, arg3=0, arg4=0)
        destroy_monster(spawnIds=[101,102,111,112,121,122]) # 퀘스트용 소멸
        set_actor(triggerId=7001, visible=True, initialSequence='Sit_Down_A') # 준타
        set_actor(triggerId=7002, visible=True, initialSequence='Down_Idle_A') # 틴차이
        set_mesh(triggerIds=[6010], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh_animation(triggerIds=[6010], visible=True, arg3=0, arg4=0)
        set_interact_object(triggerIds=[10000478], state=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003059], questStates=[1]):
            move_user(mapId=52000050, portalId=2)
            return start_c_02()


class start_c_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025], visible=False, arg3=0, arg4=0, arg5=0) # 짹쨱이
        set_mesh(triggerIds=[6026,6027,6028,6029,6030], visible=True, arg3=0, arg4=0, arg5=0) # 짹쨱이
        set_mesh_animation(triggerIds=[6026,6027,6028,6029,6030], visible=True, arg3=0, arg4=0)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8010,8011,8001], returnView=False)
        move_user_path(patrolName='MS2PatrolData_9902') # 유저를 이동시킨다
        set_conversation(type=1, spawnId=0, script='$52000050_QD__MAIN_02__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_c_03()


class start_c_03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000050_QD__MAIN_02__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_c_04()


class start_c_04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000050_QD__MAIN_02__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_c_05()


class start_c_05(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[9010,9011,9012,9013,9014], enabled=True) # 참새들 조용히 있음
        set_visible_breakable_object(triggerIds=[9010,9011,9012,9013,9014], arg2=True) # 참새들 조용히 있음

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            set_mesh(triggerIds=[6026,6027,6028,6029,6030], visible=False, arg3=0, arg4=0, arg5=0)
            return start_c_06()


class start_c_06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7011], visible=False) # 지저귐 삭제
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera_path(pathIds=[8001], returnView=True)
        set_achievement(triggerId=701, type='trigger', achieve='FlyingBirds') # 퀘스트 목표 체크용 업적이벤트 발생

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            set_breakable(triggerIds=[9010,9011,9012,9013,9014], enabled=False)
            set_visible_breakable_object(triggerIds=[9010,9011,9012,9013,9014], arg2=False)
            return start_c_07()


class start_c_07(state.State):
    pass


