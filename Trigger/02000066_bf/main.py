""" trigger/02000066_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 초기화
        self.set_effect(triggerIds=[602], visible=False) # 아노스 던전 시작01
        self.set_effect(triggerIds=[603], visible=False) # 아노스  소환
        self.set_effect(triggerIds=[604], visible=False) # 아노스 게이트 파괴
        self.set_effect(triggerIds=[605], visible=False) # 아노스 경비병 사망
        self.set_effect(triggerIds=[606], visible=False) # 파토스 성공01
        self.set_effect(triggerIds=[607], visible=False) # 파토스 성공02
        self.set_effect(triggerIds=[608], visible=False) # 파토스 성공03
        self.set_effect(triggerIds=[609], visible=False) # 파토스 성공04
        self.set_effect(triggerIds=[610], visible=False) # 파토스 성공05
        self.set_effect(triggerIds=[611], visible=False) # 파토스 리젠
        self.set_effect(triggerIds=[612], visible=False) # 아노스 성공
        self.set_effect(triggerIds=[613], visible=False) # 파토스 실패01
        self.set_effect(triggerIds=[614], visible=False) # 파토스 실패02
        self.set_effect(triggerIds=[615], visible=False) # 파토스 실패03
        self.set_effect(triggerIds=[616], visible=False) # 파토스 실패04
        self.set_effect(triggerIds=[617], visible=False) # 파토스 실패05
        self.set_effect(triggerIds=[618], visible=False) # 파토스 실패06
        self.set_effect(triggerIds=[619], visible=False) # 파토스 실패07
        self.set_effect(triggerIds=[620], visible=False)
        self.set_effect(triggerIds=[6003], visible=False) # 미션 성공
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[99], animationEffect=False)
        self.set_mesh(triggerIds=[9001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_max_user_count(value=4):
            # 던전 최대 인원수가 4이면
            return 연출시작(self.ctx)
        if self.dungeon_max_user_count(value=3):
            # 던전 최대 인원수가 3이면
            self.set_user_value(triggerId=9995001, key='randomTalk', value=1)
            return 연출시작(self.ctx)
        if self.dungeon_max_user_count(value=2):
            # 던전 최대 인원수가 2이면
            self.set_user_value(triggerId=9995002, key='randomTalk', value=1)
            self.set_user_value(triggerId=9995003, key='randomTalk', value=1)
            return 연출시작(self.ctx)
        if self.dungeon_max_user_count(value=1):
            # 던전 최대 인원수가 1이면
            self.set_user_value(triggerId=9995001, key='randomTalk', value=1)
            self.set_user_value(triggerId=9995002, key='randomTalk', value=1)
            self.set_user_value(triggerId=9995003, key='randomTalk', value=1)
            return 연출시작(self.ctx)
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=9995001, key='randomTalk', value=1)
            self.set_user_value(triggerId=9995002, key='randomTalk', value=1)
            self.set_user_value(triggerId=9995003, key='randomTalk', value=1)
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=300, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=차어나운스03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차어나운스01_1(self.ctx)


class 차어나운스01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(visible=True)
        self.add_cinematic_talk(npcId=11000032, illustId='Anos_serious', msg='$02000066_BF__MAIN__4$', duration=5000, align='center')
        self.set_skip(state=차어나운스03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차어나운스02_1(self.ctx)


class 차어나운스02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11000032, illustId='Anos_serious', msg='$02000066_BF__MAIN__5$', duration=5000, align='center')
        self.set_skip(state=차어나운스03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차어나운스03_1(self.ctx)


class 차어나운스03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.select_camera(triggerId=300, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=0, arg2='1,3')
        self.show_count_ui(text='$02000066_BF__MAIN__6$', stage=1, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 차웨이브1(self.ctx)


class 차웨이브1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120, startDelay=0, interval=1, vOffset=0)
        self.create_monster(spawnIds=[900], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return 차웨이브성공1(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패1(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[1001])
        self.destroy_monster(spawnIds=[1002])
        self.destroy_monster(spawnIds=[1003])
        self.destroy_monster(spawnIds=[1004])
        self.destroy_monster(spawnIds=[1005])
        self.destroy_monster(spawnIds=[1006])
        self.destroy_monster(spawnIds=[1007])
        self.destroy_monster(spawnIds=[1008])
        self.destroy_monster(spawnIds=[1101])
        self.destroy_monster(spawnIds=[1102])
        self.destroy_monster(spawnIds=[1103])
        self.destroy_monster(spawnIds=[1104])
        self.destroy_monster(spawnIds=[1105])
        self.destroy_monster(spawnIds=[1106])
        self.destroy_monster(spawnIds=[1107])
        self.destroy_monster(spawnIds=[1108])
        self.destroy_monster(spawnIds=[1201])
        self.destroy_monster(spawnIds=[1202])
        self.destroy_monster(spawnIds=[1203])
        self.destroy_monster(spawnIds=[1204])
        self.destroy_monster(spawnIds=[1205])
        self.destroy_monster(spawnIds=[1206])
        self.destroy_monster(spawnIds=[1207])
        self.destroy_monster(spawnIds=[1208])
        self.destroy_monster(spawnIds=[1299])
        self.destroy_monster(spawnIds=[1301])
        self.destroy_monster(spawnIds=[1302])
        self.destroy_monster(spawnIds=[1303])
        self.destroy_monster(spawnIds=[1304])
        self.destroy_monster(spawnIds=[1305])
        self.destroy_monster(spawnIds=[1306])
        self.destroy_monster(spawnIds=[1307])
        self.destroy_monster(spawnIds=[1308])
        self.destroy_monster(spawnIds=[1401])
        self.destroy_monster(spawnIds=[1402])
        self.destroy_monster(spawnIds=[1403])
        self.destroy_monster(spawnIds=[1404])
        self.destroy_monster(spawnIds=[1601])
        self.destroy_monster(spawnIds=[1602])
        self.destroy_monster(spawnIds=[1603])
        self.destroy_monster(spawnIds=[1604])


class 차웨이브실패1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[613], visible=True)
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__7$', arg3='3000', arg4='0')
        self.destroy_monster(spawnIds=[900])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 실패(self.ctx)


class 차웨이브성공1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20000662, textId=20000662)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawnIds=[900])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차어나운스01_2(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패1(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000662)


class 차어나운스01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20000665, textId=20000665, duration=7000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 차어나운스02_2(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패1(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000665)


class 차어나운스02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='2,3')
        self.show_count_ui(text='$02000066_BF__MAIN__10$', stage=2, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 차웨이브2(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패1(self.ctx)


class 차웨이브2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120, startDelay=0, interval=1)
        self.create_monster(spawnIds=[901], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return 차웨이브성공2(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패2(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[1001])
        self.destroy_monster(spawnIds=[1002])
        self.destroy_monster(spawnIds=[1003])
        self.destroy_monster(spawnIds=[1004])
        self.destroy_monster(spawnIds=[1005])
        self.destroy_monster(spawnIds=[1006])
        self.destroy_monster(spawnIds=[1007])
        self.destroy_monster(spawnIds=[1008])
        self.destroy_monster(spawnIds=[1101])
        self.destroy_monster(spawnIds=[1102])
        self.destroy_monster(spawnIds=[1103])
        self.destroy_monster(spawnIds=[1104])
        self.destroy_monster(spawnIds=[1105])
        self.destroy_monster(spawnIds=[1106])
        self.destroy_monster(spawnIds=[1107])
        self.destroy_monster(spawnIds=[1108])
        self.destroy_monster(spawnIds=[1201])
        self.destroy_monster(spawnIds=[1202])
        self.destroy_monster(spawnIds=[1203])
        self.destroy_monster(spawnIds=[1204])
        self.destroy_monster(spawnIds=[1205])
        self.destroy_monster(spawnIds=[1206])
        self.destroy_monster(spawnIds=[1207])
        self.destroy_monster(spawnIds=[1208])
        self.destroy_monster(spawnIds=[1299])
        self.destroy_monster(spawnIds=[1301])
        self.destroy_monster(spawnIds=[1302])
        self.destroy_monster(spawnIds=[1303])
        self.destroy_monster(spawnIds=[1304])
        self.destroy_monster(spawnIds=[1305])
        self.destroy_monster(spawnIds=[1306])
        self.destroy_monster(spawnIds=[1307])
        self.destroy_monster(spawnIds=[1308])
        self.destroy_monster(spawnIds=[1401])
        self.destroy_monster(spawnIds=[1402])
        self.destroy_monster(spawnIds=[1403])
        self.destroy_monster(spawnIds=[1404])
        self.destroy_monster(spawnIds=[1601])
        self.destroy_monster(spawnIds=[1602])
        self.destroy_monster(spawnIds=[1603])
        self.destroy_monster(spawnIds=[1604])


class 차웨이브실패2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__11$', arg3='3000', arg4='0')
        self.destroy_monster(spawnIds=[901])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 실패(self.ctx)


class 차웨이브성공2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20000662, textId=20000662)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawnIds=[901])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패2(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 차어나운스01_3(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000662)


class 차어나운스01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20000665, textId=20000665, duration=7000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패2(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 차어나운스02_3(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000665)


class 차어나운스02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='3,3')
        self.show_count_ui(text='$02000066_BF__MAIN__14$', stage=3, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패2(self.ctx)
        if self.wait_tick(waitTick=6000):
            return 차웨이브3(self.ctx)


class 차웨이브3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120, startDelay=0, interval=1)
        self.create_monster(spawnIds=[902], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return 차웨이브성공3(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 차웨이브실패3(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[1001])
        self.destroy_monster(spawnIds=[1002])
        self.destroy_monster(spawnIds=[1003])
        self.destroy_monster(spawnIds=[1004])
        self.destroy_monster(spawnIds=[1005])
        self.destroy_monster(spawnIds=[1006])
        self.destroy_monster(spawnIds=[1007])
        self.destroy_monster(spawnIds=[1008])
        self.destroy_monster(spawnIds=[1101])
        self.destroy_monster(spawnIds=[1102])
        self.destroy_monster(spawnIds=[1103])
        self.destroy_monster(spawnIds=[1104])
        self.destroy_monster(spawnIds=[1105])
        self.destroy_monster(spawnIds=[1106])
        self.destroy_monster(spawnIds=[1107])
        self.destroy_monster(spawnIds=[1108])
        self.destroy_monster(spawnIds=[1201])
        self.destroy_monster(spawnIds=[1202])
        self.destroy_monster(spawnIds=[1203])
        self.destroy_monster(spawnIds=[1204])
        self.destroy_monster(spawnIds=[1205])
        self.destroy_monster(spawnIds=[1206])
        self.destroy_monster(spawnIds=[1207])
        self.destroy_monster(spawnIds=[1208])
        self.destroy_monster(spawnIds=[1299])
        self.destroy_monster(spawnIds=[1301])
        self.destroy_monster(spawnIds=[1302])
        self.destroy_monster(spawnIds=[1303])
        self.destroy_monster(spawnIds=[1304])
        self.destroy_monster(spawnIds=[1305])
        self.destroy_monster(spawnIds=[1306])
        self.destroy_monster(spawnIds=[1307])
        self.destroy_monster(spawnIds=[1308])
        self.destroy_monster(spawnIds=[1401])
        self.destroy_monster(spawnIds=[1402])
        self.destroy_monster(spawnIds=[1403])
        self.destroy_monster(spawnIds=[1404])
        self.destroy_monster(spawnIds=[1601])
        self.destroy_monster(spawnIds=[1602])
        self.destroy_monster(spawnIds=[1603])
        self.destroy_monster(spawnIds=[1604])


class 차웨이브실패3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__15$', arg3='3000', arg4='0')
        self.destroy_monster(spawnIds=[902])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 실패(self.ctx)


class 차웨이브성공3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=7, arg2='$02000066_BF__MAIN__33$', arg3='3000', arg4='0')
        self.set_event_ui(type=0, arg2='0,0')
        self.set_effect(triggerIds=[6003], visible=True)
        self.show_guide_summary(entityId=20000662, textId=20000662)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_achievement(triggerId=103, type='trigger', achieve='EdgeofSpirits')
        self.destroy_monster(spawnIds=[902])
        self.set_mesh(triggerIds=[9001], visible=False)
        self.destroy_monster(spawnIds=[99])
        self.set_npc_emotion_loop(spawnId=99, sequenceName='Attack_Idle_A', duration=1E+12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_effect(triggerIds=[6003], visible=False)
            return 차승리연출랜덤3(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000662)


class 차승리연출랜덤3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 차승리연출01_3(self.ctx)
        if self.random_condition(rate=20):
            return 차승리연출02_3(self.ctx)
        if self.random_condition(rate=20):
            return 차승리연출03_3(self.ctx)
        if self.random_condition(rate=20):
            return 차승리연출04_3(self.ctx)
        if self.random_condition(rate=20):
            return 차승리연출05_3(self.ctx)


class 차승리연출01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__17$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차승리연출종료3(self.ctx)


class 차승리연출02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__18$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차승리연출종료3(self.ctx)


class 차승리연출03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__19$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차승리연출종료3(self.ctx)


class 차승리연출04_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__20$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 차승리연출종료3(self.ctx)


class 차승리연출05_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__21$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5982):
            return 차승리연출종료3(self.ctx)


class 차승리연출종료3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 분기점(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(triggerId=103, type='trigger', achieve='ClearAnosSOS')
        # ClearAnosSOS 퀘스트


class 분기점(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[612], visible=True)
        self.dungeon_clear()
        self.set_achievement(triggerId=103, type='trigger', achieve='ClearLifeForest')
        self.set_user_value(triggerId=10003067, key='woodsoflife', value=1)
        self.create_monster(spawnIds=[907], animationEffect=False)
        self.move_user(mapId=2000066, portalId=3, boxId=103)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.show_guide_summary(entityId=20000666, textId=20000666)
            self.set_effect(triggerIds=[620], visible=True)
            self.destroy_monster(spawnIds=[907])
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='woodsoflife', value=0)


"""
class 분기점01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[612], visible=True)
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__22$', arg3='10000')
        self.create_monster(spawnIds=[903], animationEffect=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='60', seconds=60, startDelay=0, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            self.destroy_monster(spawnIds=[903])
            self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
            self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
            return None # Missing State: 차어나운스01_4

"""


"""
class 차어나운스01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='4,6')
        self.set_event_ui(type=2, arg2='$02000066_BF__MAIN__23$', arg3='4,5')
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return None # Missing State: 차웨이브4

"""


"""
class 차웨이브4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120, startDelay=0, interval=1)
        self.create_monster(spawnIds=[99], animationEffect=False)
        self.create_monster(spawnIds=[904], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return None # Missing State: 차웨이브성공4
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패4

"""


"""
class 차웨이브실패4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__24$', arg3='3000', arg4='0')
        self.set_timer(timerId='3', seconds=3)
        self.destroy_monster(spawnIds=[904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 실패(self.ctx)

"""


"""
class 차웨이브성공4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20000662, textId=20000662)
        self.set_timer(timerId='5', seconds=5)
        self.destroy_monster(spawnIds=[904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패4
        if self.time_expired(timerId='5'):
            return None # Missing State: 차어나운스01_5

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000662)

"""


"""
class 차어나운스01_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__26$', arg3='7000', arg4='0')
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패4
        if self.time_expired(timerId='10'):
            return None # Missing State: 차어나운스02_5

"""


"""
class 차어나운스02_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='5,6')
        self.set_event_ui(type=2, arg2='$02000066_BF__MAIN__27$', arg3='5,5')
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return None # Missing State: 차웨이브5

"""


"""
class 차웨이브5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120, startDelay=0, interval=1)
        self.create_monster(spawnIds=[905], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return None # Missing State: 차웨이브성공5
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패5

"""


"""
class 차웨이브실패5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__28$', arg3='5000', arg4='0')
        self.set_timer(timerId='3', seconds=3)
        self.destroy_monster(spawnIds=[905])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 실패(self.ctx)

"""


"""
class 차웨이브성공5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20000662, textId=20000662)
        self.set_timer(timerId='5', seconds=5)
        self.destroy_monster(spawnIds=[905])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return None # Missing State: 차어나운스01_6
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패5

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000662)

"""


"""
class 차어나운스01_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__30$', arg3='7000', arg4='0')
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return None # Missing State: 차어나운스02_6
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패5

"""


"""
class 차어나운스02_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='6,6')
        self.set_event_ui(type=2, arg2='$02000066_BF__MAIN__31$', arg3='6,5')
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return None # Missing State: 차웨이브6
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패5

"""


"""
class 차웨이브6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='120', seconds=120, startDelay=0, interval=1)
        self.create_monster(spawnIds=[906], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='120'):
            return None # Missing State: 차웨이브성공6
        if self.monster_dead(boxIds=[99]):
            return None # Missing State: 차웨이브실패6

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[1001])
        self.destroy_monster(spawnIds=[1002])
        self.destroy_monster(spawnIds=[1003])
        self.destroy_monster(spawnIds=[1004])
        self.destroy_monster(spawnIds=[1005])
        self.destroy_monster(spawnIds=[1006])
        self.destroy_monster(spawnIds=[1007])
        self.destroy_monster(spawnIds=[1008])
        self.destroy_monster(spawnIds=[1101])
        self.destroy_monster(spawnIds=[1102])
        self.destroy_monster(spawnIds=[1103])
        self.destroy_monster(spawnIds=[1104])
        self.destroy_monster(spawnIds=[1105])
        self.destroy_monster(spawnIds=[1106])
        self.destroy_monster(spawnIds=[1107])
        self.destroy_monster(spawnIds=[1108])
        self.destroy_monster(spawnIds=[1201])
        self.destroy_monster(spawnIds=[1202])
        self.destroy_monster(spawnIds=[1203])
        self.destroy_monster(spawnIds=[1204])
        self.destroy_monster(spawnIds=[1205])
        self.destroy_monster(spawnIds=[1206])
        self.destroy_monster(spawnIds=[1207])
        self.destroy_monster(spawnIds=[1208])
        self.destroy_monster(spawnIds=[1299])
        self.destroy_monster(spawnIds=[1301])
        self.destroy_monster(spawnIds=[1302])
        self.destroy_monster(spawnIds=[1303])
        self.destroy_monster(spawnIds=[1304])
        self.destroy_monster(spawnIds=[1305])
        self.destroy_monster(spawnIds=[1306])
        self.destroy_monster(spawnIds=[1307])
        self.destroy_monster(spawnIds=[1308])
        self.destroy_monster(spawnIds=[1401])
        self.destroy_monster(spawnIds=[1402])
        self.destroy_monster(spawnIds=[1403])
        self.destroy_monster(spawnIds=[1404])
        self.destroy_monster(spawnIds=[1601])
        self.destroy_monster(spawnIds=[1602])
        self.destroy_monster(spawnIds=[1603])
        self.destroy_monster(spawnIds=[1604])

"""


"""
class 차웨이브실패6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__32$', arg3='3000', arg4='0')
        self.set_timer(timerId='3', seconds=3)
        self.destroy_monster(spawnIds=[906])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 실패(self.ctx)

"""


"""
class 차웨이브성공6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6003], visible=True)
        self.set_achievement(triggerId=103, type='trigger', achieve='EdgeofSpirits')
        self.show_guide_summary(entityId=20000662, textId=20000662)
        self.set_timer(timerId='5', seconds=5)
        self.destroy_monster(spawnIds=[906])
        self.destroy_monster(spawnIds=[99])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.set_effect(triggerIds=[6003], visible=False)
            return None # Missing State: 차승리연출랜덤6

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20000662)

"""


"""
class 차승리연출랜덤6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # Missing State: 차승리연출종료6
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return None # Missing State: 차승리연출01_6
        if self.random_condition(rate=20):
            return None # Missing State: 차승리연출02_6
        if self.random_condition(rate=20):
            return None # Missing State: 차승리연출03_6
        if self.random_condition(rate=20):
            return None # Missing State: 차승리연출04_6
        if self.random_condition(rate=20):
            return None # Missing State: 차승리연출05_6

"""


"""
class 차승리연출01_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[606], visible=True)
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__34$', arg4=3)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return None # Missing State: 차승리연출종료6

"""


"""
class 차승리연출02_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[607], visible=True)
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__35$', arg4=3)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return None # Missing State: 차승리연출종료6

"""


"""
class 차승리연출03_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[608], visible=True)
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__36$', arg4=3)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return None # Missing State: 차승리연출종료6

"""


"""
class 차승리연출04_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(visible=True)
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__37$', arg4=5)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return None # Missing State: 차승리연출종료6

"""


"""
class 차승리연출05_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[610], visible=True)
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__38$', arg4=3)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return None # Missing State: 차승리연출종료6

"""


"""
class 차승리연출종료6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return None # Missing State: 분기점03

"""


"""
class 분기점03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[612], visible=True)
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__39$', arg3='10000')
        self.create_monster(spawnIds=[907], animationEffect=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='60', seconds=60, startDelay=0, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            self.destroy_monster(spawnIds=[907])
            return 완료(self.ctx)

"""


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # self.set_skip(state=실패연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=15):
            return 실패연출01(self.ctx)
        if self.random_condition(rate=15):
            return 실패연출02(self.ctx)
        if self.random_condition(rate=14):
            return 실패연출03(self.ctx)
        if self.random_condition(rate=14):
            return 실패연출04(self.ctx)
        if self.random_condition(rate=14):
            return 실패연출05(self.ctx)
        if self.random_condition(rate=14):
            return 실패연출06(self.ctx)
        if self.random_condition(rate=14):
            return 실패연출07(self.ctx)


class 실패연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__40$', arg4=3)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 실패연출종료(self.ctx)


class 실패연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__41$', arg4=3)
        self.set_timer(timerId='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 실패연출종료(self.ctx)


class 실패연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__42$', arg4=5)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 실패연출종료(self.ctx)


class 실패연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__43$', arg4=5)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 실패연출종료(self.ctx)


class 실패연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__44$', arg4=5)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 실패연출종료(self.ctx)


class 실패연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__45$', arg4=6)
        self.set_timer(timerId='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='7'):
            return 실패연출종료(self.ctx)


class 실패연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000068, script='$02000066_BF__MAIN__46$', arg4=4)
        self.set_timer(timerId='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 실패연출종료(self.ctx)


class 실패연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 실패강제이동(self.ctx)


class 실패강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)
        self.move_user(mapId=0, portalId=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.move_user(mapId=0, portalId=0)
            return 대기(self.ctx)


initial_state = 대기
