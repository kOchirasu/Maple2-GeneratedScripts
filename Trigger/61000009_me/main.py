""" trigger/61000009_me/main.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_actor(triggerId=4002, visible=False, initialSequence='Closed_A')
        set_event_ui(type=0, arg2='0,3')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[6001], visible=False)
        set_mesh(triggerIds=[6002], visible=True)
        set_effect(triggerIds=[7999], visible=False)
        set_effect(triggerIds=[7001], visible=False)
        set_effect(triggerIds=[7002], visible=False)
        set_effect(triggerIds=[7003], visible=False)
        set_effect(triggerIds=[7999], visible=False)
        set_effect(triggerIds=[7998], visible=False)
        set_effect(triggerIds=[7801], visible=False)
        set_effect(triggerIds=[7802], visible=False)
        set_effect(triggerIds=[7803], visible=False)
        create_monster(spawnIds=[101], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if count_users(boxId=700, boxId=1):
            return Ready_Idle()


class Ready_Idle(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Ready_Idle_02()


class Ready_Idle_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        set_timer(timerId='30', seconds=30, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return start_02()
        if count_users(boxId=700, boxId=10):
            return start_02()

    def on_exit(self):
        hide_guide_summary(entityId=100)


#  매시브 이벤트에서는 해당 스테이트를 이동하지 않음 
class start_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        play_system_sound_in_box(sound='System_Dark_Intro_Chord_01')
        set_cinematic_ui(type=3, script='$02000374_BF__MAIN__25$') # 오브젝티브
        set_timer(timerId='5', seconds=5, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return start_02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class start_02(state.State):
    def on_enter(self):
        set_achievement(triggerId=700, type='trigger', achieve='dailyquest_start')
        set_user_value(triggerId=2037406, key='timer', value=1) # 타이머 시작 장치
        set_event_ui(type=0, arg2='1,3')
        set_effect(triggerIds=[7998], visible=True)
        set_mesh(triggerIds=[6002], visible=False)
        set_actor(triggerId=4001, visible=True, initialSequence='Opened_A')
        set_portal(portalId=1, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return Round2()
        if user_detected(boxIds=[701]):
            return Round_Talk1()


class Round_Talk1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__0$', arg3='5000')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return Round2()
        if wait_tick(waitTick=6000):
            return Round_Talk_01_1()


class Round_Talk_01_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[110], arg2=False) # 닥터 피피

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return Round2()
        if wait_tick(waitTick=6000):
            return Round_Talk_02_1()


class Round_Talk_02_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__1$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__1$', arg4=3, arg5=0)
        move_npc(spawnId=110, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return Round2()
        if wait_tick(waitTick=4000):
            return Round_Talk_03_1()


class Round_Talk_03_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__2$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round_Talk_04_1()
        if monster_dead(boxIds=[101]):
            return Round2()


class Round_Talk_04_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return Round2()


class Round2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__3$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round_Talk_00_2()


class Round_Talk_00_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__26$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__27$', arg4=3, arg5=0)
        move_npc(spawnId=110, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round_Talk_01_2()


class Round_Talk_01_2(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='2,3')
        select_camera(triggerId=8001, enable=True)
        set_effect(triggerIds=[7801], visible=True)
        set_effect(triggerIds=[7802], visible=True)
        # <action name="이펙트를설정한다" arg1 = "7803" arg2="1" />
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__28$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__29$', arg4=3, arg5=0)
        # <action name="대화를설정한다" arg1="1" arg2="110" arg3="$02000374_BF__MAIN__4$" arg4="3" arg5="1"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_skill(triggerIds=[5001], isEnable=True)
            set_skill(triggerIds=[5002], isEnable=True)
            set_skill(triggerIds=[5003], isEnable=True)
            set_skill(triggerIds=[5004], isEnable=True)
            set_skill(triggerIds=[5005], isEnable=True)
            set_skill(triggerIds=[5006], isEnable=True)
            set_skill(triggerIds=[5007], isEnable=True)
            set_skill(triggerIds=[5008], isEnable=True)
            set_skill(triggerIds=[5009], isEnable=True)
            set_skill(triggerIds=[5010], isEnable=True)
            set_skill(triggerIds=[5011], isEnable=True)
            set_skill(triggerIds=[5012], isEnable=True)
            set_skill(triggerIds=[5013], isEnable=True)
            return Round_Talk_02_2()

    def on_exit(self):
        select_camera(triggerId=8001, enable=False)
        set_effect(triggerIds=[7001], visible=True)
        set_effect(triggerIds=[7002], visible=True)
        set_effect(triggerIds=[7003], visible=True)


class Round_Talk_02_2(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_2003')
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__5$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__5$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Round_Talk_03_2()


class Round_Talk_03_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__6$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__6$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Round_Spawn_Random2()


class Round_Spawn_Random2(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return Round_Spawn_A2()
        if random_condition(rate=33):
            return Round_Spawn_B2()
        if random_condition(rate=33):
            return Round_Spawn_C2()


class Round_Spawn_A2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__7$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__7$', arg4=3, arg5=0) # 카모칸
        set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=85000):
            return Round_Spawn_A_02_Ready2()
        if user_value(key='2Round_A', value=1):
            return Round_Spawn_A_02_Ready2()


class Round_Spawn_B2(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_2004')
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__8$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__8$', arg4=3, arg5=0)
        set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 아구스 소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=85000):
            return Round_Spawn_B_02_Ready2()
        if user_value(key='2Round_B', value=1):
            return Round_Spawn_B_02_Ready2()


class Round_Spawn_C2(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_2005')
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__9$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__9$', arg4=3, arg5=0)
        set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=85000):
            return Round_Spawn_C_02_Ready2()
        if user_value(key='2Round_C', value=1):
            return Round_Spawn_C_02_Ready2()


class Round_Spawn_A_02_Ready2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__10$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__10$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_Spawn_A_02_2()


class Round_Spawn_B_02_Ready2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__13$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__13$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_Spawn_B_02_2()


class Round_Spawn_C_02_Ready2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__16$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__16$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_Spawn_C_02_2()


class Round_Spawn_A_02_2(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round_Spawn_A_B_02_2()
        if random_condition(rate=50):
            return Round_Spawn_A_C_02_2()


class Round_Spawn_A_B_02_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=135000):
            return Round_Spawn_A_B_C2()
        if user_value(key='2Round_B', value=1):
            return Round_Spawn_A_B_C2()


class Round_Spawn_A_C_02_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=135000):
            return Round_Spawn_A_C_B2()
        if user_value(key='2Round_C', value=1):
            return Round_Spawn_A_C_B2()


class Round_Spawn_A_B_C2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__11$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__11$', arg4=3, arg5=1)
        set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Round_End_Condition2()


class Round_Spawn_A_C_B2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__12$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__12$', arg4=3, arg5=1)
        set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Round_End_Condition2()


class Round_Spawn_B_02_2(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round_Spawn_B_A_02_2()
        if random_condition(rate=50):
            return Round_Spawn_B_C_02_2()


class Round_Spawn_B_A_02_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=135000):
            return Round_Spawn_B_A_C2()
        if user_value(key='2Round_A', value=1):
            return Round_Spawn_B_A_C2()


class Round_Spawn_B_C_02_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=135000):
            return Round_Spawn_B_C_A2()
        if user_value(key='2Round_C', value=1):
            return Round_Spawn_B_C_A2()


class Round_Spawn_B_A_C2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__14$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__14$', arg4=3, arg5=1)
        set_user_value(triggerId=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Round_End_Condition2()


class Round_Spawn_B_C_A2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__15$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__15$', arg4=3, arg5=1)
        set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Round_End_Condition2()


class Round_Spawn_C_02_2(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return Round_Spawn_C_A_02_2()
        if random_condition(rate=50):
            return Round_Spawn_C_B_02_2()


class Round_Spawn_C_A_02_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=135000):
            return Round_Spawn_C_A_B2()
        if user_value(key='2Round_A', value=1):
            return Round_Spawn_C_A_B2()


class Round_Spawn_C_B_02_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=135000):
            return Round_Spawn_C_B_A2()
        if user_value(key='2Round_B', value=1):
            return Round_Spawn_C_B_A2()


class Round_Spawn_C_A_B2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__18$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__18$', arg4=3, arg5=1)
        set_user_value(triggerId=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Round_End_Condition2()


class Round_Spawn_C_B_A2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__17$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__17$', arg4=3, arg5=1)
        set_user_value(triggerId=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Round_End_Condition2()


class Round_End_Condition2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,103,104]):
            return Round_Ready3()


class Round_Ready3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Round_Talk01_3()


class Round_Talk01_3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__19$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__19$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_Talk02_3()


class Round_Talk02_3(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='3,3')
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__20$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__20$', arg4=2, arg5=0)
        set_user_value(triggerId=2037405, key='3Round_Effect', value=1) # 3라운드 연출 장치

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_Talk03_3()


class Round_Talk03_3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__21$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__21$', arg4=2, arg5=0)
        set_effect(triggerIds=[7206], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return Round_Talk04_3()


class Round_Talk04_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[199], arg2=False) # 붉은 두꺼비
        set_conversation(type=1, spawnId=199, script='$02000374_BF__MAIN__30$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_Talk05_3()


class Round_Talk05_3(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[199])
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__31$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__32$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Round_Talk06_3()


class Round_Talk06_3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__22$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__22$', arg4=2, arg5=0)
        set_effect(triggerIds=[7205], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return Round_Talk07_3()


class Round_Talk07_3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__23$', arg4=2, arg5=0)
        create_monster(spawnIds=[105], arg2=False) # 둔둔

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105]):
            return Clear()


class Clear(state.State):
    def on_enter(self):
        move_user(mapId=61000009, portalId=6)
        set_actor(triggerId=4002, visible=True, initialSequence='Opened_A')
        move_npc(spawnId=110, patrolName='MS2PatrolData_2999')
        set_event_ui(type=7, arg2='$02000374_BF__MAIN__33$', arg3='3000', arg4='0')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__24$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return End()


class End(state.State):
    def on_enter(self):
        set_actor(triggerId=4002, visible=True, initialSequence='Closed_A')
        set_event_ui(type=1, arg2='$02000374_BF__MAIN__34$', arg3='3000')
        set_conversation(type=1, spawnId=110, script='$02000374_BF__MAIN__35$', arg4=2, arg5=0)
        set_effect(triggerIds=[4102], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return End_02()


class End_02(state.State):
    def on_enter(self):
        set_actor(triggerId=4002, visible=False, initialSequence='Closed_A')
        destroy_monster(spawnIds=[110])
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)


