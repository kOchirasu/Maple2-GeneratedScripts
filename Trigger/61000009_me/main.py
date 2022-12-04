""" trigger/61000009_me/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4002, visible=False, initialSequence='Closed_A')
        self.set_event_ui(type=0, arg2='0,3')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[6001], visible=False)
        self.set_mesh(triggerIds=[6002], visible=True)
        self.set_effect(triggerIds=[7999], visible=False)
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7999], visible=False)
        self.set_effect(triggerIds=[7998], visible=False)
        self.set_effect(triggerIds=[7801], visible=False)
        self.set_effect(triggerIds=[7802], visible=False)
        self.set_effect(triggerIds=[7803], visible=False)
        self.create_monster(spawnIds=[101], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=700, boxId=1):
            return Ready_Idle(self.ctx)


class Ready_Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return Ready_Idle_02(self.ctx)


class Ready_Idle_02(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.set_timer(timerId='30', seconds=30, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            return start_02(self.ctx)
        if self.count_users(boxId=700, boxId=10):
            return start_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=100)


# 매시브 이벤트에서는 해당 스테이트를 이동하지 않음
class start_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.play_system_sound_in_box(sound='System_Dark_Intro_Chord_01')
        self.set_cinematic_ui(type=3, script='$02000374_BF__MAIN__25$') # 오브젝티브
        self.set_timer(timerId='5', seconds=5, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return start_02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=700, type='trigger', achieve='dailyquest_start')
        self.set_user_value(triggerId=2037406, key='timer', value=1) # 타이머 시작 장치
        self.set_event_ui(type=0, arg2='1,3')
        self.set_effect(triggerIds=[7998], visible=True)
        self.set_mesh(triggerIds=[6002], visible=False)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Opened_A')
        self.set_portal(portalId=1, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return Round2(self.ctx)
        if self.user_detected(boxIds=[701]):
            return Round_Talk1(self.ctx)


class Round_Talk1(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__0$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return Round2(self.ctx)
        if self.wait_tick(waitTick=6000):
            return Round_Talk_01_1(self.ctx)


class Round_Talk_01_1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[110], animationEffect=False) # 닥터 피피

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return Round2(self.ctx)
        if self.wait_tick(waitTick=6000):
            return Round_Talk_02_1(self.ctx)


class Round_Talk_02_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__1$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__1$', arg4=3, arg5=0)
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return Round2(self.ctx)
        if self.wait_tick(waitTick=4000):
            return Round_Talk_03_1(self.ctx)


class Round_Talk_03_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__2$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round_Talk_04_1(self.ctx)
        if self.monster_dead(boxIds=[101]):
            return Round2(self.ctx)


class Round_Talk_04_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return Round2(self.ctx)


class Round2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__3$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round_Talk_00_2(self.ctx)


class Round_Talk_00_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__26$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__27$', arg4=3, arg5=0)
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round_Talk_01_2(self.ctx)


class Round_Talk_01_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='2,3')
        self.select_camera(triggerId=8001, enable=True)
        self.set_effect(triggerIds=[7801], visible=True)
        self.set_effect(triggerIds=[7802], visible=True)
        # <action name="이펙트를설정한다" arg1 = "7803" arg2="1" />
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__28$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__29$', arg4=3, arg5=0)
        # <action name="대화를설정한다" arg1="1" arg2="110" arg3="$02000374_BF__MAIN__4$" arg4="3" arg5="1"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_skill(triggerIds=[5001], enable=True)
            self.set_skill(triggerIds=[5002], enable=True)
            self.set_skill(triggerIds=[5003], enable=True)
            self.set_skill(triggerIds=[5004], enable=True)
            self.set_skill(triggerIds=[5005], enable=True)
            self.set_skill(triggerIds=[5006], enable=True)
            self.set_skill(triggerIds=[5007], enable=True)
            self.set_skill(triggerIds=[5008], enable=True)
            self.set_skill(triggerIds=[5009], enable=True)
            self.set_skill(triggerIds=[5010], enable=True)
            self.set_skill(triggerIds=[5011], enable=True)
            self.set_skill(triggerIds=[5012], enable=True)
            self.set_skill(triggerIds=[5013], enable=True)
            return Round_Talk_02_2(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=8001, enable=False)
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_effect(triggerIds=[7002], visible=True)
        self.set_effect(triggerIds=[7003], visible=True)


class Round_Talk_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2003')
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__5$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__5$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return Round_Talk_03_2(self.ctx)


class Round_Talk_03_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__6$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__6$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round_Spawn_Random2(self.ctx)


class Round_Spawn_Random2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return Round_Spawn_A2(self.ctx)
        if self.random_condition(rate=33):
            return Round_Spawn_B2(self.ctx)
        if self.random_condition(rate=33):
            return Round_Spawn_C2(self.ctx)


class Round_Spawn_A2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__7$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__7$', arg4=3, arg5=0) # 카모칸
        self.set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=85000):
            return Round_Spawn_A_02_Ready2(self.ctx)
        if self.user_value(key='2Round_A', value=1):
            return Round_Spawn_A_02_Ready2(self.ctx)


class Round_Spawn_B2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2004')
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__8$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__8$', arg4=3, arg5=0)
        self.set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 아구스 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=85000):
            return Round_Spawn_B_02_Ready2(self.ctx)
        if self.user_value(key='2Round_B', value=1):
            return Round_Spawn_B_02_Ready2(self.ctx)


class Round_Spawn_C2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2005')
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__9$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__9$', arg4=3, arg5=0)
        self.set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=85000):
            return Round_Spawn_C_02_Ready2(self.ctx)
        if self.user_value(key='2Round_C', value=1):
            return Round_Spawn_C_02_Ready2(self.ctx)


class Round_Spawn_A_02_Ready2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__10$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__10$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_Spawn_A_02_2(self.ctx)


class Round_Spawn_B_02_Ready2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__13$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__13$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_Spawn_B_02_2(self.ctx)


class Round_Spawn_C_02_Ready2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__16$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__16$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_Spawn_C_02_2(self.ctx)


class Round_Spawn_A_02_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round_Spawn_A_B_02_2(self.ctx)
        if self.random_condition(rate=50):
            return Round_Spawn_A_C_02_2(self.ctx)


class Round_Spawn_A_B_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=135000):
            return Round_Spawn_A_B_C2(self.ctx)
        if self.user_value(key='2Round_B', value=1):
            return Round_Spawn_A_B_C2(self.ctx)


class Round_Spawn_A_C_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=135000):
            return Round_Spawn_A_C_B2(self.ctx)
        if self.user_value(key='2Round_C', value=1):
            return Round_Spawn_A_C_B2(self.ctx)


class Round_Spawn_A_B_C2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__11$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__11$', arg4=3, arg5=1)
        self.set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_A_C_B2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__12$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__12$', arg4=3, arg5=1)
        self.set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_B_02_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round_Spawn_B_A_02_2(self.ctx)
        if self.random_condition(rate=50):
            return Round_Spawn_B_C_02_2(self.ctx)


class Round_Spawn_B_A_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=135000):
            return Round_Spawn_B_A_C2(self.ctx)
        if self.user_value(key='2Round_A', value=1):
            return Round_Spawn_B_A_C2(self.ctx)


class Round_Spawn_B_C_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=135000):
            return Round_Spawn_B_C_A2(self.ctx)
        if self.user_value(key='2Round_C', value=1):
            return Round_Spawn_B_C_A2(self.ctx)


class Round_Spawn_B_A_C2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__14$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__14$', arg4=3, arg5=1)
        self.set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_B_C_A2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__15$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__15$', arg4=3, arg5=1)
        self.set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_C_02_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round_Spawn_C_A_02_2(self.ctx)
        if self.random_condition(rate=50):
            return Round_Spawn_C_B_02_2(self.ctx)


class Round_Spawn_C_A_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=135000):
            return Round_Spawn_C_A_B2(self.ctx)
        if self.user_value(key='2Round_A', value=1):
            return Round_Spawn_C_A_B2(self.ctx)


class Round_Spawn_C_B_02_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=135000):
            return Round_Spawn_C_B_A2(self.ctx)
        if self.user_value(key='2Round_B', value=1):
            return Round_Spawn_C_B_A2(self.ctx)


class Round_Spawn_C_A_B2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__18$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__18$', arg4=3, arg5=1)
        self.set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_C_B_A2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__17$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__17$', arg4=3, arg5=1)
        self.set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Round_End_Condition2(self.ctx)


class Round_End_Condition2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102,103,104]):
            return Round_Ready3(self.ctx)


class Round_Ready3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round_Talk01_3(self.ctx)


class Round_Talk01_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__19$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__19$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_Talk02_3(self.ctx)


class Round_Talk02_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='3,3')
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__20$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__20$', arg4=2, arg5=0)
        self.set_user_value(triggerId=2037405, key='3Round_Effect', value=1) # 3라운드 연출 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_Talk03_3(self.ctx)


class Round_Talk03_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__21$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__21$', arg4=2, arg5=0)
        self.set_effect(triggerIds=[7206], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2300):
            return Round_Talk04_3(self.ctx)


class Round_Talk04_3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[199], animationEffect=False) # 붉은 두꺼비
        self.set_conversation(type=1, spawnId=199, script='$02000374_BF__MAIN__30$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_Talk05_3(self.ctx)


class Round_Talk05_3(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[199])
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__31$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__32$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Round_Talk06_3(self.ctx)


class Round_Talk06_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__22$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__22$', arg4=2, arg5=0)
        self.set_effect(triggerIds=[7205], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2300):
            return Round_Talk07_3(self.ctx)


class Round_Talk07_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__23$', arg4=2, arg5=0)
        self.create_monster(spawnIds=[105], animationEffect=False) # 둔둔

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[105]):
            return Clear(self.ctx)


class Clear(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=61000009, portalId=6)
        self.set_actor(triggerId=4002, visible=True, initialSequence='Opened_A')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2999')
        self.set_event_ui(type=7, arg2='$02000374_BF__MAIN__33$', arg3='3000', arg4='0')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__24$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4002, visible=True, initialSequence='Closed_A')
        self.set_event_ui(type=1, arg2='$02000374_BF__MAIN__34$', arg3='3000')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__35$', arg4=2, arg5=0)
        self.set_effect(triggerIds=[4102], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return End_02(self.ctx)


class End_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4002, visible=False, initialSequence='Closed_A')
        self.destroy_monster(spawnIds=[110])
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)


initial_state = Ready
