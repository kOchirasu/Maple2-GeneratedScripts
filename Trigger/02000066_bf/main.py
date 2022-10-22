""" trigger/02000066_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=False) # 아노스 던전 시작01
        set_effect(triggerIds=[603], visible=False) # 아노스  소환
        set_effect(triggerIds=[604], visible=False) # 아노스 게이트 파괴
        set_effect(triggerIds=[605], visible=False) # 아노스 경비병 사망
        set_effect(triggerIds=[606], visible=False) # 파토스 성공01
        set_effect(triggerIds=[607], visible=False) # 파토스 성공02
        set_effect(triggerIds=[608], visible=False) # 파토스 성공03
        set_effect(triggerIds=[609], visible=False) # 파토스 성공04
        set_effect(triggerIds=[610], visible=False) # 파토스 성공05
        set_effect(triggerIds=[611], visible=False) # 파토스 리젠
        set_effect(triggerIds=[612], visible=False) # 아노스 성공
        set_effect(triggerIds=[613], visible=False) # 파토스 실패01
        set_effect(triggerIds=[614], visible=False) # 파토스 실패02
        set_effect(triggerIds=[615], visible=False) # 파토스 실패03
        set_effect(triggerIds=[616], visible=False) # 파토스 실패04
        set_effect(triggerIds=[617], visible=False) # 파토스 실패05
        set_effect(triggerIds=[618], visible=False) # 파토스 실패06
        set_effect(triggerIds=[619], visible=False) # 파토스 실패07
        set_effect(triggerIds=[620], visible=False)
        set_effect(triggerIds=[6003], visible=False) # 미션 성공
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[99], arg2=False)
        set_mesh(triggerIds=[9001], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if dungeon_max_user_count(value=4):
            return 연출시작()
        if dungeon_max_user_count(value=3):
            set_user_value(triggerId=9995001, key='randomTalk', value=1)
            return 연출시작()
        if dungeon_max_user_count(value=2):
            set_user_value(triggerId=9995002, key='randomTalk', value=1)
            set_user_value(triggerId=9995003, key='randomTalk', value=1)
            return 연출시작()
        if dungeon_max_user_count(value=1):
            set_user_value(triggerId=9995001, key='randomTalk', value=1)
            set_user_value(triggerId=9995002, key='randomTalk', value=1)
            set_user_value(triggerId=9995003, key='randomTalk', value=1)
            return 연출시작()
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=9995001, key='randomTalk', value=1)
            set_user_value(triggerId=9995002, key='randomTalk', value=1)
            set_user_value(triggerId=9995003, key='randomTalk', value=1)
            return 연출시작()

state.DungeonStart = DungeonStart


class 연출시작(state.State):
    def on_enter(self):
        select_camera(triggerId=300, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=차어나운스03_1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차어나운스01_1()


class 차어나운스01_1(state.State):
    def on_enter(self):
        set_effect(visible=True)
        add_cinematic_talk(npcId=11000032, illustId='Anos_serious', msg='$02000066_BF__MAIN__4$', duration=5000, align='center')
        set_skip(state=차어나운스03_1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차어나운스02_1()


class 차어나운스02_1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000032, illustId='Anos_serious', msg='$02000066_BF__MAIN__5$', duration=5000, align='center')
        set_skip(state=차어나운스03_1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차어나운스03_1()


class 차어나운스03_1(state.State):
    def on_enter(self):
        set_skip()
        select_camera(triggerId=300, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_event_ui(type=0, arg2='1,3')
        show_count_ui(text='$02000066_BF__MAIN__6$', stage=1, count=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차웨이브1()


class 차웨이브1(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120, clearAtZero=False, display=True, arg5=0)
        create_monster(spawnIds=[900], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            return 차웨이브성공1()
        if monster_dead(boxIds=[99]):
            return 차웨이브실패1()

    def on_exit(self):
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[1006])
        destroy_monster(spawnIds=[1007])
        destroy_monster(spawnIds=[1008])
        destroy_monster(spawnIds=[1101])
        destroy_monster(spawnIds=[1102])
        destroy_monster(spawnIds=[1103])
        destroy_monster(spawnIds=[1104])
        destroy_monster(spawnIds=[1105])
        destroy_monster(spawnIds=[1106])
        destroy_monster(spawnIds=[1107])
        destroy_monster(spawnIds=[1108])
        destroy_monster(spawnIds=[1201])
        destroy_monster(spawnIds=[1202])
        destroy_monster(spawnIds=[1203])
        destroy_monster(spawnIds=[1204])
        destroy_monster(spawnIds=[1205])
        destroy_monster(spawnIds=[1206])
        destroy_monster(spawnIds=[1207])
        destroy_monster(spawnIds=[1208])
        destroy_monster(spawnIds=[1299])
        destroy_monster(spawnIds=[1301])
        destroy_monster(spawnIds=[1302])
        destroy_monster(spawnIds=[1303])
        destroy_monster(spawnIds=[1304])
        destroy_monster(spawnIds=[1305])
        destroy_monster(spawnIds=[1306])
        destroy_monster(spawnIds=[1307])
        destroy_monster(spawnIds=[1308])
        destroy_monster(spawnIds=[1401])
        destroy_monster(spawnIds=[1402])
        destroy_monster(spawnIds=[1403])
        destroy_monster(spawnIds=[1404])
        destroy_monster(spawnIds=[1601])
        destroy_monster(spawnIds=[1602])
        destroy_monster(spawnIds=[1603])
        destroy_monster(spawnIds=[1604])


class 차웨이브실패1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[613], visible=True)
        set_event_ui(type=5, arg2='$02000066_BF__MAIN__7$', arg3='3000', arg4='0')
        destroy_monster(spawnIds=[900])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 실패()


class 차웨이브성공1(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20000662, textId=20000662)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        destroy_monster(spawnIds=[900])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차어나운스01_2()
        if monster_dead(boxIds=[99]):
            return 차웨이브실패1()

    def on_exit(self):
        hide_guide_summary(entityId=20000662)


class 차어나운스01_2(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20000665, textId=20000665, duration=7000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 차어나운스02_2()
        if monster_dead(boxIds=[99]):
            return 차웨이브실패1()

    def on_exit(self):
        hide_guide_summary(entityId=20000665)


class 차어나운스02_2(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='2,3')
        show_count_ui(text='$02000066_BF__MAIN__10$', stage=2, count=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차웨이브2()
        if monster_dead(boxIds=[99]):
            return 차웨이브실패1()


class 차웨이브2(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120, clearAtZero=False, display=True)
        create_monster(spawnIds=[901], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            return 차웨이브성공2()
        if monster_dead(boxIds=[99]):
            return 차웨이브실패2()

    def on_exit(self):
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[1006])
        destroy_monster(spawnIds=[1007])
        destroy_monster(spawnIds=[1008])
        destroy_monster(spawnIds=[1101])
        destroy_monster(spawnIds=[1102])
        destroy_monster(spawnIds=[1103])
        destroy_monster(spawnIds=[1104])
        destroy_monster(spawnIds=[1105])
        destroy_monster(spawnIds=[1106])
        destroy_monster(spawnIds=[1107])
        destroy_monster(spawnIds=[1108])
        destroy_monster(spawnIds=[1201])
        destroy_monster(spawnIds=[1202])
        destroy_monster(spawnIds=[1203])
        destroy_monster(spawnIds=[1204])
        destroy_monster(spawnIds=[1205])
        destroy_monster(spawnIds=[1206])
        destroy_monster(spawnIds=[1207])
        destroy_monster(spawnIds=[1208])
        destroy_monster(spawnIds=[1299])
        destroy_monster(spawnIds=[1301])
        destroy_monster(spawnIds=[1302])
        destroy_monster(spawnIds=[1303])
        destroy_monster(spawnIds=[1304])
        destroy_monster(spawnIds=[1305])
        destroy_monster(spawnIds=[1306])
        destroy_monster(spawnIds=[1307])
        destroy_monster(spawnIds=[1308])
        destroy_monster(spawnIds=[1401])
        destroy_monster(spawnIds=[1402])
        destroy_monster(spawnIds=[1403])
        destroy_monster(spawnIds=[1404])
        destroy_monster(spawnIds=[1601])
        destroy_monster(spawnIds=[1602])
        destroy_monster(spawnIds=[1603])
        destroy_monster(spawnIds=[1604])


class 차웨이브실패2(state.State):
    def on_enter(self):
        set_event_ui(type=5, arg2='$02000066_BF__MAIN__11$', arg3='3000', arg4='0')
        destroy_monster(spawnIds=[901])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 실패()


class 차웨이브성공2(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20000662, textId=20000662)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        destroy_monster(spawnIds=[901])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 차웨이브실패2()
        if wait_tick(waitTick=5000):
            return 차어나운스01_3()

    def on_exit(self):
        hide_guide_summary(entityId=20000662)


class 차어나운스01_3(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20000665, textId=20000665, duration=7000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 차웨이브실패2()
        if wait_tick(waitTick=10000):
            return 차어나운스02_3()

    def on_exit(self):
        hide_guide_summary(entityId=20000665)


class 차어나운스02_3(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='3,3')
        show_count_ui(text='$02000066_BF__MAIN__14$', stage=3, count=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 차웨이브실패2()
        if wait_tick(waitTick=6000):
            return 차웨이브3()


class 차웨이브3(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120, clearAtZero=False, display=True)
        create_monster(spawnIds=[902], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            return 차웨이브성공3()
        if monster_dead(boxIds=[99]):
            return 차웨이브실패3()

    def on_exit(self):
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[1006])
        destroy_monster(spawnIds=[1007])
        destroy_monster(spawnIds=[1008])
        destroy_monster(spawnIds=[1101])
        destroy_monster(spawnIds=[1102])
        destroy_monster(spawnIds=[1103])
        destroy_monster(spawnIds=[1104])
        destroy_monster(spawnIds=[1105])
        destroy_monster(spawnIds=[1106])
        destroy_monster(spawnIds=[1107])
        destroy_monster(spawnIds=[1108])
        destroy_monster(spawnIds=[1201])
        destroy_monster(spawnIds=[1202])
        destroy_monster(spawnIds=[1203])
        destroy_monster(spawnIds=[1204])
        destroy_monster(spawnIds=[1205])
        destroy_monster(spawnIds=[1206])
        destroy_monster(spawnIds=[1207])
        destroy_monster(spawnIds=[1208])
        destroy_monster(spawnIds=[1299])
        destroy_monster(spawnIds=[1301])
        destroy_monster(spawnIds=[1302])
        destroy_monster(spawnIds=[1303])
        destroy_monster(spawnIds=[1304])
        destroy_monster(spawnIds=[1305])
        destroy_monster(spawnIds=[1306])
        destroy_monster(spawnIds=[1307])
        destroy_monster(spawnIds=[1308])
        destroy_monster(spawnIds=[1401])
        destroy_monster(spawnIds=[1402])
        destroy_monster(spawnIds=[1403])
        destroy_monster(spawnIds=[1404])
        destroy_monster(spawnIds=[1601])
        destroy_monster(spawnIds=[1602])
        destroy_monster(spawnIds=[1603])
        destroy_monster(spawnIds=[1604])


class 차웨이브실패3(state.State):
    def on_enter(self):
        set_event_ui(type=5, arg2='$02000066_BF__MAIN__15$', arg3='3000', arg4='0')
        destroy_monster(spawnIds=[902])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 실패()


class 차웨이브성공3(state.State):
    def on_enter(self):
        set_event_ui(type=7, arg2='$02000066_BF__MAIN__33$', arg3='3000', arg4='0')
        set_event_ui(type=0, arg2='0,0')
        set_effect(triggerIds=[6003], visible=True)
        show_guide_summary(entityId=20000662, textId=20000662)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_achievement(triggerId=103, type='trigger', achieve='EdgeofSpirits')
        destroy_monster(spawnIds=[902])
        set_mesh(triggerIds=[9001], visible=False)
        destroy_monster(spawnIds=[99])
        set_npc_emotion_loop(spawnId=99, sequenceName='Attack_Idle_A', duration=1E+12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_effect(triggerIds=[6003], visible=False)
            return 차승리연출랜덤3()

    def on_exit(self):
        hide_guide_summary(entityId=20000662)


class 차승리연출랜덤3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return 차승리연출01_3()
        if random_condition(rate=20):
            return 차승리연출02_3()
        if random_condition(rate=20):
            return 차승리연출03_3()
        if random_condition(rate=20):
            return 차승리연출04_3()
        if random_condition(rate=20):
            return 차승리연출05_3()


class 차승리연출01_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__17$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차승리연출종료3()


class 차승리연출02_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__18$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차승리연출종료3()


class 차승리연출03_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__19$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차승리연출종료3()


class 차승리연출04_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__20$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차승리연출종료3()


class 차승리연출05_3(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__21$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5982):
            return 차승리연출종료3()


class 차승리연출종료3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 분기점()

    def on_exit(self):
        set_achievement(triggerId=103, type='trigger', achieve='ClearAnosSOS') # ClearAnosSOS 퀘스트


class 분기점(state.State):
    def on_enter(self):
        set_effect(triggerIds=[612], visible=True)
        dungeon_clear()
        set_achievement(triggerId=103, type='trigger', achieve='ClearLifeForest')
        set_user_value(triggerId=10003067, key='woodsoflife', value=1)
        create_monster(spawnIds=[907], arg2=False)
        move_user(mapId=2000066, portalId=3, boxId=103)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            show_guide_summary(entityId=20000666, textId=20000666)
            set_effect(triggerIds=[620], visible=True)
            destroy_monster(spawnIds=[907])
            return 완료()


class 완료(state.State):
    def on_enter(self):
        set_user_value(key='woodsoflife', value=0)


class 실패(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3) # action name="스킵을설정한다" arg1="실패연출종료" /

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return 실패연출01()
        if random_condition(rate=15):
            return 실패연출02()
        if random_condition(rate=14):
            return 실패연출03()
        if random_condition(rate=14):
            return 실패연출04()
        if random_condition(rate=14):
            return 실패연출05()
        if random_condition(rate=14):
            return 실패연출06()
        if random_condition(rate=14):
            return 실패연출07()


class 실패연출01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__40$', arg4=3)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 실패연출종료()


class 실패연출02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__41$', arg4=3)
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 실패연출종료()


class 실패연출03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__42$', arg4=5)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 실패연출종료()


class 실패연출04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__43$', arg4=5)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 실패연출종료()


class 실패연출05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__44$', arg4=5)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 실패연출종료()


class 실패연출06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__45$', arg4=6)
        set_timer(timerId='7', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return 실패연출종료()


class 실패연출07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__46$', arg4=4)
        set_timer(timerId='6', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 실패연출종료()


class 실패연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 실패강제이동()


class 실패강제이동(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        move_user(mapId=0, portalId=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            move_user(mapId=0, portalId=0)
            return 대기()


