""" trigger/02020006_bf/15000_minipuzzle_interactwithnpc.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')
        self.enable_local_camera(isEnable=False) # 로컬카메라 전체 OFF
        self.set_user_value(key='StandAsideTypeA', value=0)
        self.set_user_value(key='StandAsideTypeB', value=0)
        # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15101], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[15102], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.set_actor(triggerId=15100, visible=False, initialSequence='Idle_A') # Dummy RareBox
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거
        self.set_interact_object(triggerIds=[12000250], state=2)
        # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeA / Additional Effect 71001051 71001231 부여
        self.set_interact_object(triggerIds=[12000078], state=2)
        # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeB / Additional Effect 71001051 71001241 부여
        self.set_interact_object(triggerIds=[12000093], state=2)
        self.destroy_monster(spawnIds=[15401,15402,15501,15502]) # TypeA 15401 15402
        # TypeB 15501 15502
        self.set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        self.set_effect(triggerIds=[15301], visible=False) # Right Sound Effect
        self.set_effect(triggerIds=[15302], visible=False) # Wrong Sound Effect
        self.set_effect(triggerIds=[15303], visible=False) # Happy Sound Effect
        self.set_effect(triggerIds=[15304], visible=False) # Shy Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn', value=1):
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.enable_local_camera(isEnable=True) # 로컬카메라 전체 ON
            return InteractWithNpc_NpcTypeRandomPick(self.ctx)


class InteractWithNpc_NpcTypeRandomPick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15101], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[15002], visible=True, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.set_actor(triggerId=15100, visible=True, initialSequence='Idle_A') # Dummy RareBox
        self.set_user_value(triggerId=15001, key='PortalOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return InteractWithNpc_NpcTypeA_Setting(self.ctx)
        if self.random_condition(rate=50):
            return InteractWithNpc_NpcTypeB_Setting(self.ctx)


# 포잉 TypeA 경계하는 녀석 스폰 / 정중한 인사하면 비켜줌
class InteractWithNpc_NpcTypeA_Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # NPC_TurnedAround / 기믹 시작 오브젝트 / Additional Effect 71001051 부여
        self.set_interact_object(triggerIds=[12000078], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000078], stateValue=0):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001051 지속시간 동일
            self.set_timer(timerId='1', seconds=120, startDelay=1, interval=0, vOffset=0)
            return InteractWithNpc_NpcTypeA_NpcSpawn(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class InteractWithNpc_NpcTypeA_NpcSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000078], state=2)
        self.create_monster(spawnIds=[15401], animationEffect=True)
        self.set_user_value(triggerId=1000051, key='NPCTalk', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StandAsideTypeA', value=1):
            # 몬스터 21001030 / AI_KritiasSlime_MiniPuzzle_TypeA 에서 받는 신호
            self.set_user_value(triggerId=1000051, key='NPCTalk', value=0)
            return InteractWithNpc_NpcTypeA_NpcChange(self.ctx)
        if self.time_expired(timerId='1'):
            return InteractWithNpc_Fail(self.ctx)


class InteractWithNpc_NpcTypeA_NpcChange(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        self.destroy_monster(spawnIds=[15401])
        self.create_monster(spawnIds=[15402], animationEffect=True)
        self.set_user_value(triggerId=15001, key='PortalOn', value=2)
        # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15101], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[15102], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.add_buff(boxIds=[150001], skillId=71001052, level=1, isPlayer=False, isSkillSet=False)
        self.set_timer(timerId='10', seconds=60, startDelay=1, interval=0, vOffset=0)
        self.set_user_value(triggerId=151001, key='NPCKill', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return InteractWithNpc_NpcTypeA_StandAside(self.ctx)


class InteractWithNpc_NpcTypeA_StandAside(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[15303], visible=True)
        self.move_npc(spawnId=15402, patrolName='MS2PatrolData_15600')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return InteractWithNpc_Success(self.ctx)


# 포잉 TypeB 딴청 피우는 녀석 스폰 / 빤히 쳐다보하면 비켜줌
class InteractWithNpc_NpcTypeB_Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # NPC_TurnedAround / 기믹 시작 오브젝트 / Additional Effect 71001051 부여
        self.set_interact_object(triggerIds=[12000093], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000093], stateValue=0):
            self.set_timer(timerId='1', seconds=120, startDelay=1, interval=0, vOffset=0)
            return InteractWithNpc_NpcTypeB_NpcSpawn(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class InteractWithNpc_NpcTypeB_NpcSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000093], state=2)
        self.create_monster(spawnIds=[15501], animationEffect=True)
        self.set_user_value(triggerId=1000052, key='NPCTalk', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StandAsideTypeB', value=1):
            # 몬스터 21001031 / AI_KritiasSlime_MiniPuzzle_TypeB 에서 받는 신호
            self.set_user_value(triggerId=1000052, key='NPCTalk', value=0)
            return InteractWithNpc_NpcTypeB_NpcChange(self.ctx)
        if self.time_expired(timerId='1'):
            return InteractWithNpc_Fail(self.ctx)


class InteractWithNpc_NpcTypeB_NpcChange(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        self.destroy_monster(spawnIds=[15501])
        self.create_monster(spawnIds=[15502], animationEffect=True)
        self.set_user_value(triggerId=15001, key='PortalOn', value=2)
        # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15101], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[15102], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.add_buff(boxIds=[150001], skillId=71001052, level=1, isPlayer=False, isSkillSet=False)
        self.set_timer(timerId='10', seconds=60, startDelay=1, interval=0, vOffset=0)
        self.set_user_value(triggerId=151001, key='NPCKill', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return InteractWithNpc_NpcTypeB_StandAside(self.ctx)


class InteractWithNpc_NpcTypeB_StandAside(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[15304], visible=True)
        self.move_npc(spawnId=15502, patrolName='MS2PatrolData_15600')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return InteractWithNpc_Success(self.ctx)


# 퍼즐 성공 후 종료
class InteractWithNpc_Success(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=15000, key='TimeEventOn', value=0)
        self.set_actor(triggerId=15100, visible=False, initialSequence='Idle_A') # Dummy RareBox
        self.set_effect(triggerIds=[15300], visible=True) # Success Sound Effect
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거
        self.set_interact_object(triggerIds=[12000250], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000250], stateValue=0):
            return InteractWithNpc_SuccessDelay(self.ctx)
        if self.time_expired(timerId='10'):
            return InteractWithNpc_Fail(self.ctx)


class InteractWithNpc_SuccessDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return InteractWithNpc_Quit(self.ctx)


# 제한 시간 종료
class InteractWithNpc_Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거
        self.set_interact_object(triggerIds=[12000250], state=2)
        # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeA / Additional Effect 71001051 71001231 부여
        self.set_interact_object(triggerIds=[12000078], state=2)
        # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeB / Additional Effect 71001051 71001241 부여
        self.set_interact_object(triggerIds=[12000093], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'): # 타임이벤트가 종료했으면 완전 초기화
            # 버프 유지 시간이 경과했으면
            return InteractWithNpc_Quit(self.ctx)


class InteractWithNpc_Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')
        self.set_user_value(triggerId=15001, key='PortalOn', value=0)
        self.destroy_monster(spawnIds=[15401,15402,15501,15502]) # TypeA 15401 15402
        # TypeB 15501 15502

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
