""" trigger/99999874/15000_minipuzzle_interactwithnpc.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='StandAsideTypeA', value=0)
        self.set_user_value(key='StandAsideTypeB', value=0)
        self.set_mesh(triggerIds=[15101], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15102], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.set_actor(triggerId=15100, visible=False, initialSequence='Idle_A') # Dummy RareBox
        self.set_interact_object(triggerIds=[12000070], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거
        self.set_interact_object(triggerIds=[12000078], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeA / Additional Effect 71001051 71001231 부여
        self.set_interact_object(triggerIds=[12000093], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeB / Additional Effect 71001051 71001241 부여
        self.destroy_monster(spawnIds=[15401,15402,15501,15502]) # TypeA 15401 15402
        self.set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        self.set_effect(triggerIds=[15301], visible=False) # Right Sound Effect
        self.set_effect(triggerIds=[15302], visible=False) # Wrong Sound Effect
        self.set_effect(triggerIds=[15303], visible=False) # Happy Sound Effect
        self.set_effect(triggerIds=[15304], visible=False) # Shy Sound Effect

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TimeEventOn', value=1):
            return SettingDelay(self.ctx)


class SettingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return InteractWithNpc_NpcTypeRandomPick(self.ctx)


class InteractWithNpc_NpcTypeRandomPick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[15101], visible=True, arg3=0, delay=0, scale=0) # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15002], visible=True, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.set_actor(triggerId=15100, visible=True, initialSequence='Idle_A') # Dummy RareBox
        self.set_user_value(triggerId=15001, key='PortalOn', value=1)

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            return InteractWithNpc_NpcTypeA_Setting(self.ctx)
        if self.random_condition(rate=50):
            return InteractWithNpc_NpcTypeB_Setting(self.ctx)


# 포잉 TypeA 경계하는 녀석 스폰 / 정중한 인사하면 비켜줌
class InteractWithNpc_NpcTypeA_Setting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000078], state=1) # NPC_TurnedAround / 기믹 시작 오브젝트 / Additional Effect 71001051 부여

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000078], stateValue=0):
            self.set_timer(timerId='1', seconds=90, startDelay=1, interval=0, vOffset=0)
            return InteractWithNpc_NpcTypeA_NpcSpawn(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class InteractWithNpc_NpcTypeA_NpcSpawn(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000078], state=2)
        self.create_monster(spawnIds=[15401], animationEffect=True)
        self.set_user_value(triggerId=1000051, key='NPCTalk', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StandAsideTypeA', value=1):
            self.set_user_value(triggerId=1000051, key='NPCTalk', value=0)
            return InteractWithNpc_NpcTypeA_NpcChange(self.ctx)
        if self.time_expired(timerId='1'):
            return InteractWithNpc_Fail(self.ctx)


class InteractWithNpc_NpcTypeA_NpcChange(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        self.destroy_monster(spawnIds=[15401])
        self.create_monster(spawnIds=[15402], animationEffect=True)
        self.set_user_value(triggerId=15001, key='PortalOn', value=2)
        self.set_mesh(triggerIds=[15101], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15102], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.add_buff(boxIds=[150001], skillId=71001052, level=1, isPlayer=False, isSkillSet=False)
        self.set_timer(timerId='10', seconds=60, startDelay=1, interval=0, vOffset=0)
        self.set_user_value(triggerId=151001, key='NPCKill', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return InteractWithNpc_NpcTypeA_StandAside(self.ctx)


class InteractWithNpc_NpcTypeA_StandAside(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[15303], visible=True)
        self.move_npc(spawnId=15402, patrolName='MS2PatrolData_15600')

    def on_tick(self) -> common.Trigger:
        if self.true():
            self.set_effect(triggerIds=[15303], visible=False)
            return InteractWithNpc_Success(self.ctx)


# 포잉 TypeB 딴청 피우는 녀석 스폰 / 빤히 쳐다보하면 비켜줌
class InteractWithNpc_NpcTypeB_Setting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000093], state=1) # NPC_TurnedAround / 기믹 시작 오브젝트 / Additional Effect 71001051 부여

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000093], stateValue=0):
            self.set_timer(timerId='1', seconds=90, startDelay=1, interval=0, vOffset=0)
            return InteractWithNpc_NpcTypeB_NpcSpawn(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class InteractWithNpc_NpcTypeB_NpcSpawn(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000093], state=2)
        self.create_monster(spawnIds=[15501], animationEffect=True)
        self.set_user_value(triggerId=1000052, key='NPCTalk', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StandAsideTypeB', value=1):
            self.set_user_value(triggerId=1000052, key='NPCTalk', value=0)
            return InteractWithNpc_NpcTypeB_NpcChange(self.ctx)
        if self.time_expired(timerId='1'):
            return InteractWithNpc_Fail(self.ctx)


class InteractWithNpc_NpcTypeB_NpcChange(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[15300], visible=False) # Success Sound Effect
        self.destroy_monster(spawnIds=[15501])
        self.create_monster(spawnIds=[15502], animationEffect=True)
        self.set_user_value(triggerId=15001, key='PortalOn', value=2)
        self.set_mesh(triggerIds=[15101], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Enterance
        self.set_mesh(triggerIds=[15102], visible=False, arg3=0, delay=0, scale=0) # InvisibleBlock_Inside
        self.add_buff(boxIds=[150001], skillId=71001052, level=1, isPlayer=False, isSkillSet=False)
        self.set_timer(timerId='10', seconds=60, startDelay=1, interval=0, vOffset=0)
        self.set_user_value(triggerId=151001, key='NPCKill', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return InteractWithNpc_NpcTypeB_StandAside(self.ctx)


class InteractWithNpc_NpcTypeB_StandAside(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[15304], visible=True)
        self.move_npc(spawnId=15502, patrolName='MS2PatrolData_15600')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return InteractWithNpc_Success(self.ctx)


# 퍼즐 성공 후 종료
class InteractWithNpc_Success(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=15000, key='TimeEventOn', value=0)
        self.set_actor(triggerId=15100, visible=False, initialSequence='Idle_A') # Dummy RareBox
        self.set_interact_object(triggerIds=[12000070], state=1) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000070], stateValue=0):
            return InteractWithNpc_SuccessDelay(self.ctx)
        if self.time_expired(timerId='10'):
            return InteractWithNpc_Fail(self.ctx)


class InteractWithNpc_SuccessDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return InteractWithNpc_Quit(self.ctx)


# 제한 시간 종료
class InteractWithNpc_Fail(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000070], state=2) # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001151 걸어서 71001051 제거
        self.set_interact_object(triggerIds=[12000078], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeA / Additional Effect 71001051 71001231 부여
        self.set_interact_object(triggerIds=[12000093], state=2) # NPC_TurnedAround / 기믹 시작 오브젝트 / TypeB / Additional Effect 71001051 71001241 부여

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'): # 타임이벤트가 종료했으면 완전 초기화
            return InteractWithNpc_Quit(self.ctx)


class InteractWithNpc_Quit(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='10')
        self.set_user_value(triggerId=15001, key='PortalOn', value=0)
        self.destroy_monster(spawnIds=[15401,15402,15501,15502]) # TypeA 15401 15402

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
