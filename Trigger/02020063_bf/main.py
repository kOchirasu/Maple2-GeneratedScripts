""" trigger/02020063_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032], visible=True)
        set_effect(triggerIds=[10001], visible=False)
        set_effect(triggerIds=[10002], visible=False)
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096], visible=True) # <가두기 트리거 메쉬>
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True) # <시작 위치 세팅>
        enable_spawn_point_pc(spawnId=1, isEnable=True)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        set_user_value(triggerId=99990002, key='Battle_1_SpawnStart', value=0)
        set_user_value(triggerId=99990003, key='Battle_2_Start', value=0)
        set_user_value(triggerId=99990004, key='Battle_3_Start', value=0)
        set_user_value(triggerId=99990005, key='Battle_2_SpawnStart', value=0)
        set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
        set_actor(triggerId=4002, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if any_one():
            return 유저카운트()


class 유저카운트(state.State):
    def on_enter(self):
        set_actor(triggerId=4002, visible=True, initialSequence='ks_quest_fusiondevice_A01_on')
        set_effect(triggerIds=[10001], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='FieldGameStart', value=1):
            return 딜레이()
        if user_value(key='FieldGameStart', value=2):
            return 방폭()


class 딜레이(state.State):
    def on_enter(self):
        set_achievement(triggerId=9002, type='trigger', achieve='corps_battle')
        set_event_ui(type=1, arg2='$02020063_BF__MAIN__0$', arg3='5000')
        select_camera(triggerId=998, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작()


class 방폭(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020063_BF__MAIN__1$', arg3='10000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 내보내기()


class 내보내기(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032], visible=False)
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096], visible=False)
        create_monster(spawnIds=[801], arg2=False) # <무적 오브젝트 생성>
        reset_camera(interpolationTime=1)
        set_event_ui(type=0, arg2='1,3')
        set_event_ui(type=1, arg2='$02020063_BF__MAIN__2$', arg3='5000')
        set_user_value(triggerId=99990002, key='Battle_1_SpawnStart', value=1) # <웨이브 시작>
        enable_spawn_point_pc(spawnId=0, isEnable=False) # <부활 위치 세팅, 다시 살아날때는 나무에서 살아남>
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=True)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_1_Clear', value=1):
            set_user_value(triggerId=99990002, key='Battle_1_SpawnStart', value=0)
            return 포탑페이즈()
        if monster_dead(boxIds=[801]):
            set_actor(triggerId=4002, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
            set_effect(triggerIds=[10001], visible=False)
            set_effect(triggerIds=[10002], visible=True)
            return 실패_세팅()


class 포탑페이즈(state.State):
    def on_enter(self):
        give_reward_content(rewardId=31000001)
        set_user_value(triggerId=99990003, key='Battle_2_Start', value=1) # <포탑 생성>
        set_user_value(triggerId=99990005, key='Battle_2_SpawnStart', value=1)
        set_event_ui(type=0, arg2='2,3')
        set_event_ui(type=1, arg2='$02020063_BF__MAIN__3$', arg3='5000')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_Clear', value=1):
            set_user_value(triggerId=99990005, key='Battle_2_SpawnStart', value=0)
            return 보스페이즈()
        if monster_dead(boxIds=[801]):
            set_actor(triggerId=4002, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
            set_effect(triggerIds=[10001], visible=False)
            set_effect(triggerIds=[10002], visible=True)
            return 실패_세팅()


class 보스페이즈(state.State):
    def on_enter(self):
        give_reward_content(rewardId=31000002)
        set_event_ui(type=0, arg2='3,3')
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__MAIN__4$')
        set_user_value(triggerId=99990004, key='Battle_3_Start', value=1)
        set_timer(timerId='1', seconds=180, clearAtZero=True, display=True, arg5=60) # <3라운드 게임 플레이 타임 설정>

    def on_tick(self) -> state.State:
        if user_value(key='Battle_3_Clear', value=1):
            return 성공_세팅()
        if monster_dead(boxIds=[801]):
            set_actor(triggerId=4002, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
            set_effect(triggerIds=[10001], visible=False)
            set_effect(triggerIds=[10002], visible=True)
            return 실패_세팅()
        if time_expired(timerId='1'):
            set_actor(triggerId=4002, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
            return 실패_세팅()


class 성공_세팅(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__MAIN__5$')
        set_user_value(triggerId=99990002, key='Battle_1_SpawnStart', value=0)
        set_user_value(triggerId=99990003, key='Battle_2_Start', value=0)
        set_user_value(triggerId=99990004, key='Battle_3_Start', value=0)
        set_user_value(triggerId=99990005, key='Battle_2_SpawnStart', value=0)
        set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
        reset_timer(timerId='1')
        reset_timer(timerId='2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 성공_추가대사()


class 성공_추가대사(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_smile', duration=5000, script='$02020063_BF__MAIN__6$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 성공()


class 실패_세팅(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__MAIN__7$')
        set_user_value(triggerId=99990002, key='Battle_1_SpawnStart', value=0)
        set_user_value(triggerId=99990003, key='Battle_2_Start', value=0)
        set_user_value(triggerId=99990004, key='Battle_3_Start', value=0)
        set_user_value(triggerId=99990005, key='Battle_2_SpawnStart', value=0)
        set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        set_mesh(triggerIds=[4001], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 실패()


class 실패_추가대사(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020063_BF__MAIN__8$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 실패()


class 성공(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        field_war_end(isClear=True)
        set_achievement(type='trigger', achieve='FieldwarAchieve_2')

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 실패(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        field_war_end(isClear=False)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)


