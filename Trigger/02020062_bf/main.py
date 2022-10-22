""" trigger/02020062_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True) # <시작 위치 세팅>
        enable_spawn_point_pc(spawnId=1, isEnable=True)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        enable_spawn_point_pc(spawnId=3, isEnable=False)
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        reset_timer(timerId='3')
        set_effect(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=True)
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048], visible=True) # <가두기 트리거 메쉬_spawnpoin0>
        set_effect(triggerIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116], visible=True)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148], visible=True) # <가두기 트리거 메쉬_spawnpoin1>
        set_actor(triggerId=1901, visible=True, initialSequence='Idle_A') # <연출용 액터>
        shadow_expedition(type='CloseBossGauge')
        set_user_value(triggerId=99990002, key='SpawnStart', value=0)
        set_user_value(triggerId=99990003, key='ObjectPhase', value=0)
        set_user_value(triggerId=99990008, key='BossPhase', value=0)
        set_user_value(triggerId=99990024, key='MovePanel01', value=0)
        set_user_value(triggerId=99990025, key='MovePanel02', value=0)
        set_user_value(triggerId=99990026, key='MovePanel03', value=0)
        set_user_value(triggerId=99990027, key='MovePanel04', value=0)
        set_mesh(triggerIds=[40000,40001,40002,40003,40004,40005,40006,40007,40008,40009,40010,40011,40012,40013,40014,40015,40016,40017,40018,40019,40020,40021], visible=False) # 허공에 배치된 몬스터용 발판

    def on_tick(self) -> state.State:
        if any_one():
            return 유저카운트()


class 유저카운트(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='FieldGameStart', value=1):
            return 딜레이()
        if user_value(key='FieldGameStart', value=2):
            return 방폭()


class 딜레이(state.State):
    def on_enter(self):
        set_achievement(triggerId=9002, type='trigger', achieve='corps_battle')
        set_event_ui(type=1, arg2='$02020062_BF__MAIN__0$', arg3='5000')
        select_camera(triggerId=999, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작()


class 방폭(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020062_BF__MAIN__1$', arg3='10000')

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
        set_effect(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=False)
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048], visible=False)
        set_effect(triggerIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116], visible=False)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148], visible=False) # <가두기 트리거 메쉬 제거>
        reset_camera(interpolationTime=1)
        set_event_ui(type=0, arg2='1,3')
        set_event_ui(type=1, arg2='$02020062_BF__MAIN__2$', arg3='5000')
        set_timer(timerId='1', seconds=180, clearAtZero=True, display=True, arg5=60) # 군단전 제한시간
        shadow_expedition(type='OpenBossGauge', maxGaugePoint=750)
        set_user_value(triggerId=99990002, key='SpawnStart', value=1)
        set_actor(triggerId=1901, visible=False, initialSequence='Idle_A')
        create_monster(spawnIds=[701], arg2=False) # <무적 오브젝트 생성>

    def on_tick(self) -> state.State:
        if user_value(key='GaugeClear', value=1):
            return 오브젝트페이즈()
        if time_expired(timerId='1'):
            return 실패_세팅()


class 오브젝트페이즈(state.State):
    def on_enter(self):
        give_reward_content(rewardId=31000001)
        set_event_ui(type=1, arg2='$02020062_BF__MAIN__3$', arg3='5000')
        shadow_expedition(type='CloseBossGauge')
        set_event_ui(type=0, arg2='2,3')
        reset_timer(timerId='1')
        set_user_value(triggerId=99990003, key='ObjectPhase', value=1)
        set_timer(timerId='2', seconds=180, clearAtZero=True, display=True, arg5=60) # <2라운드 게임 플레이 타임 설정>
        enable_spawn_point_pc(spawnId=0, isEnable=False) # <부활 지점 세팅>
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=True)
        enable_spawn_point_pc(spawnId=3, isEnable=True)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectClear', value=1):
            return 보스페이즈()
        if time_expired(timerId='2'):
            return 실패_세팅()


class 보스페이즈(state.State):
    def on_enter(self):
        give_reward_content(rewardId=31000002)
        destroy_monster(spawnIds=[-1])
        set_event_ui(type=1, arg2='$02020062_BF__MAIN__4$', arg3='5000')
        reset_timer(timerId='2')
        set_event_ui(type=0, arg2='3,3')
        set_user_value(triggerId=99990008, key='BossPhase', value=1)
        set_timer(timerId='3', seconds=180, clearAtZero=True, display=True, arg5=60) # <3라운드 게임 플레이 타임 설정>

    def on_tick(self) -> state.State:
        if user_value(key='BossClear', value=1):
            return 성공_세팅()
        if time_expired(timerId='3'):
            return 실패_세팅()


class 성공_세팅(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020062_BF__MAIN__5$')
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        reset_timer(timerId='3')
        set_user_value(triggerId=99990002, key='SpawnStart', value=2)
        set_user_value(triggerId=99990003, key='ObjectPhase', value=2)
        set_user_value(triggerId=99990004, key='BossPhase', value=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 성공_추가대사()


class 성공_추가대사(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_smile', duration=5000, script='$02020062_BF__MAIN__6$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 성공()


class 실패_세팅(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020062_BF__MAIN__7$')
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        reset_timer(timerId='3')
        set_user_value(triggerId=99990002, key='SpawnStart', value=2)
        set_user_value(triggerId=99990003, key='ObjectPhase', value=2)
        set_user_value(triggerId=99990004, key='BossPhase', value=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 실패_추가대사()


class 실패_추가대사(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020062_BF__MAIN__8$')

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


