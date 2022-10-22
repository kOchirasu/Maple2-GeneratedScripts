""" trigger/02020031_bf/15000_minipuzzle_interactwithnpc.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='10')
        enable_local_camera(isEnable=False) # 로컬카메라 전체 OFF
        set_user_value(key='StandAsideTypeA', value=0)
        set_user_value(key='StandAsideTypeB', value=0)
        set_mesh(triggerIds=[15101], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Enterance
        set_mesh(triggerIds=[15102], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Inside
        set_actor(triggerId=15100, visible=False, initialSequence='Idle_A') # Dummy RareBox
        set_interact_object(triggerIds=[12000252], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거
        set_interact_object(triggerIds=[12000078], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeA / Additional Effect 71001051 71001231 부여
        set_interact_object(triggerIds=[12000093], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeB / Additional Effect 71001051 71001241 부여
        destroy_monster(spawnIds=[15401,15402,15501,15502]) # TypeA 15401 15402
        set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        set_effect(triggerIds=[15301], visible=False) # Right Sound Effect
        set_effect(triggerIds=[15302], visible=False) # Wrong Sound Effect
        set_effect(triggerIds=[15303], visible=False) # Happy Sound Effect
        set_effect(triggerIds=[15304], visible=False) # Shy Sound Effect

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=1):
            return SettingDelay()


class SettingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            enable_local_camera(isEnable=True)
            return InteractWithNpc_NpcTypeRandomPick()


class InteractWithNpc_NpcTypeRandomPick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[15101], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Enterance
        set_mesh(triggerIds=[15002], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Inside
        set_actor(triggerId=15100, visible=True, initialSequence='Idle_A') # Dummy RareBox
        set_user_value(triggerId=15001, key='PortalOn', value=1)

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return InteractWithNpc_NpcTypeA_Setting()
        if random_condition(rate=50):
            return InteractWithNpc_NpcTypeB_Setting()


#  포잉 TypeA 경계하는 녀석 스폰 / 정중한 인사하면 비켜줌 
class InteractWithNpc_NpcTypeA_Setting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000078], state=1) # NPC_TurnedAround / 기믹 시작 오브젝트 / Additional Effect 71001051 부여

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000078], arg2=0):
            set_timer(timerId='1', seconds=120, clearAtZero=True, display=False, arg5=0)
            return InteractWithNpc_NpcTypeA_NpcSpawn()
        if user_value(key='TimeEventOn', value=0):
            return Wait()


class InteractWithNpc_NpcTypeA_NpcSpawn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000078], state=2)
        create_monster(spawnIds=[15401], arg2=True)
        set_user_value(triggerId=1000051, key='NPCTalk', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='StandAsideTypeA', value=1):
            set_user_value(triggerId=1000051, key='NPCTalk', value=0)
            return InteractWithNpc_NpcTypeA_NpcChange()
        if time_expired(timerId='1'):
            return InteractWithNpc_Fail()


class InteractWithNpc_NpcTypeA_NpcChange(state.State):
    def on_enter(self):
        set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        destroy_monster(spawnIds=[15401])
        create_monster(spawnIds=[15402], arg2=True)
        set_user_value(triggerId=15001, key='PortalOn', value=2)
        set_mesh(triggerIds=[15101], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Enterance
        set_mesh(triggerIds=[15102], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Inside
        add_buff(boxIds=[150001], skillId=71001052, level=1, arg4=False, arg5=False)
        set_timer(timerId='10', seconds=60, clearAtZero=True, display=False, arg5=0)
        set_user_value(triggerId=151001, key='NPCKill', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return InteractWithNpc_NpcTypeA_StandAside()


class InteractWithNpc_NpcTypeA_StandAside(state.State):
    def on_enter(self):
        set_effect(triggerIds=[15303], visible=True)
        move_npc(spawnId=15402, patrolName='MS2PatrolData_15600')

    def on_tick(self) -> state.State:
        if true():
            return InteractWithNpc_Success()


#  포잉 TypeB 딴청 피우는 녀석 스폰 / 빤히 쳐다보하면 비켜줌 
class InteractWithNpc_NpcTypeB_Setting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000093], state=1) # NPC_TurnedAround / 기믹 시작 오브젝트 / Additional Effect 71001051 부여

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000093], arg2=0):
            set_timer(timerId='1', seconds=120, clearAtZero=True, display=False, arg5=0)
            return InteractWithNpc_NpcTypeB_NpcSpawn()
        if user_value(key='TimeEventOn', value=0):
            return Wait()


class InteractWithNpc_NpcTypeB_NpcSpawn(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000093], state=2)
        create_monster(spawnIds=[15501], arg2=True)
        set_user_value(triggerId=1000052, key='NPCTalk', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='StandAsideTypeB', value=1):
            set_user_value(triggerId=1000052, key='NPCTalk', value=0)
            return InteractWithNpc_NpcTypeB_NpcChange()
        if time_expired(timerId='1'):
            return InteractWithNpc_Fail()


class InteractWithNpc_NpcTypeB_NpcChange(state.State):
    def on_enter(self):
        set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        destroy_monster(spawnIds=[15501])
        create_monster(spawnIds=[15502], arg2=True)
        set_user_value(triggerId=15001, key='PortalOn', value=2)
        set_mesh(triggerIds=[15101], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Enterance
        set_mesh(triggerIds=[15102], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleBlock_Inside
        add_buff(boxIds=[150001], skillId=71001052, level=1, arg4=False, arg5=False)
        set_timer(timerId='10', seconds=60, clearAtZero=True, display=False, arg5=0)
        set_user_value(triggerId=151001, key='NPCKill', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return InteractWithNpc_NpcTypeB_StandAside()


class InteractWithNpc_NpcTypeB_StandAside(state.State):
    def on_enter(self):
        set_effect(triggerIds=[15304], visible=True)
        move_npc(spawnId=15502, patrolName='MS2PatrolData_15600')

    def on_tick(self) -> state.State:
        if true():
            return InteractWithNpc_Success()


#  퍼즐 성공 후 종료 
class InteractWithNpc_Success(state.State):
    def on_enter(self):
        set_user_value(triggerId=15000, key='TimeEventOn', value=0)
        set_actor(triggerId=15100, visible=False, initialSequence='Idle_A') # Dummy RareBox
        set_effect(triggerIds=[15300], visible=True) # Success Sound Effect
        set_interact_object(triggerIds=[12000252], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000252], arg2=0):
            return InteractWithNpc_SuccessDelay()
        if time_expired(timerId='10'):
            return InteractWithNpc_Fail()


class InteractWithNpc_SuccessDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return InteractWithNpc_Quit()


#  제한 시간 종료 
class InteractWithNpc_Fail(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000251], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거
        set_interact_object(triggerIds=[12000078], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeA / Additional Effect 71001051 71001231 부여
        set_interact_object(triggerIds=[12000093], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeB / Additional Effect 71001051 71001241 부여

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'): # 타임이벤트가 종료했으면 완전 초기화
            return InteractWithNpc_Quit()


class InteractWithNpc_Quit(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='10')
        set_user_value(triggerId=15001, key='PortalOn', value=0)
        destroy_monster(spawnIds=[15401,15402,15501,15502]) # TypeA 15401 15402

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


