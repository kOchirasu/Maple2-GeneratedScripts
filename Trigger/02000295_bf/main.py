""" trigger/02000295_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[3000], visible=False, animationEffect=False)
        set_ladder(triggerIds=[3001], visible=False, animationEffect=False)
        set_ladder(triggerIds=[3002], visible=False, animationEffect=False)
        set_ladder(triggerIds=[3003], visible=False, animationEffect=False)
        set_ladder(triggerIds=[3004], visible=False, animationEffect=False)
        destroy_monster(spawnIds=[910,911,912,913,914,915,916,917])
        create_monster(spawnIds=[4100], arg2=False) # BossActor
        destroy_monster(spawnIds=[4101]) # BossBattle
        create_monster(spawnIds=[900,901,902], arg2=True) # MobEnterance
        create_monster(spawnIds=[800,801,802,803,804], arg2=True) # LuminaBattle
        create_monster(spawnIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331], arg2=True) # SlaveNpc
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_agent(triggerIds=[8011], visible=True)
        set_agent(triggerIds=[8012], visible=True)
        set_effect(triggerIds=[5000], visible=False) # TargetGuide
        set_effect(triggerIds=[5001], visible=False) # TargetGuide
        set_effect(triggerIds=[5002], visible=False) # TargetGuide
        set_effect(triggerIds=[5100], visible=False) # Wheel
        set_effect(triggerIds=[5101], visible=False) # MetalDoorOpen
        set_effect(triggerIds=[5102], visible=False) # MetalDoorClose
        set_effect(triggerIds=[5103], visible=False) # BossAct
        set_breakable(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], enabled=False) # Jail_Mid
        set_breakable(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], enabled=False) # Jail_Under
        set_visible_breakable_object(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], arg2=False) # Jail_Mid
        set_visible_breakable_object(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], arg2=False) # Jail_Under
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[95001,95002,95003,95004,95005,95006], visible=True, arg3=0, arg4=0, arg5=0) # Stairs
        set_mesh(triggerIds=[2000], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleEnteranceBarrier
        set_mesh(triggerIds=[2001,2002], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleJailBlock_alwaysON
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045], visible=False, arg3=0, arg4=0, arg5=0) # Deck01_ClearOn
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246], visible=False, arg3=0, arg4=0, arg5=0) # Deck02_ClearOn
        set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159], visible=True, arg3=0, arg4=0, arg5=0) # Jail
        set_user_value(key='LuminaArmyJoin', value=0)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcMonologue01()


#  연출 시작 
class NpcMonologue01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        set_skip(state=CameraWalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcMonologue02()


class NpcMonologue02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=1, spawnId=201, script='$02000295_BF__MAIN__0$', arg4=3, arg5=0)
        set_skip(state=CameraWalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraWalk01()


#  철창 안 노예 말풍선 연출 
class CameraWalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)
        set_skip(state=CameraWalk02)
        add_balloon_talk(spawnId=301, msg='$02000295_BF__MAIN__1$', duration=3000, delayTick=2000) # Right
        add_balloon_talk(spawnId=310, msg='$02000295_BF__MAIN__2$', duration=3000, delayTick=2000) # Right
        add_balloon_talk(spawnId=318, msg='$02000295_BF__MAIN__3$', duration=3000, delayTick=3000) # Right
        add_balloon_talk(spawnId=316, msg='$02000295_BF__MAIN__4$', duration=3000, delayTick=3000) # Right
        add_balloon_talk(spawnId=307, msg='$02000295_BF__MAIN__5$', duration=3000, delayTick=4000) # Right
        add_balloon_talk(spawnId=312, msg='$02000295_BF__MAIN__6$', duration=3000, delayTick=4000) # Right
        add_balloon_talk(spawnId=305, msg='$02000295_BF__MAIN__7$', duration=3000, delayTick=5000) # Right
        add_balloon_talk(spawnId=314, msg='$02000295_BF__MAIN__8$', duration=3000, delayTick=5000) # Right
        add_balloon_talk(spawnId=325, msg='$02000295_BF__MAIN__9$', duration=3000, delayTick=2000) # Left
        add_balloon_talk(spawnId=323, msg='$02000295_BF__MAIN__10$', duration=3000, delayTick=2000) # Left
        add_balloon_talk(spawnId=323, msg='$02000295_BF__MAIN__11$', duration=3000, delayTick=3000) # Left
        add_balloon_talk(spawnId=327, msg='$02000295_BF__MAIN__12$', duration=3000, delayTick=4000) # Left
        add_balloon_talk(spawnId=330, msg='$02000295_BF__MAIN__13$', duration=3000, delayTick=5000) # Left

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return CameraWalk02()


class CameraWalk02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=False)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202], arg2=False)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraWalk03()


class CameraWalk03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_ladder(triggerIds=[3000], visible=True, animationEffect=True, animationDelay=10)
        set_ladder(triggerIds=[3001], visible=True, animationEffect=True, animationDelay=12)
        set_mesh(triggerIds=[2000], visible=False, arg3=0, arg4=0, arg5=0) # InvisibleEnteranceBarrier
        select_camera(triggerId=600, enable=True)
        set_skip(state=CameraWalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk04()


class CameraWalk04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=1, spawnId=202, script='$02000295_BF__MAIN__14$', arg4=3, arg5=1)
        set_skip(state=CameraWalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CameraWalk05()


class CameraWalk05(state.State):
    def on_enter(self):
        set_skip()
        move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        set_conversation(type=1, spawnId=202, script='$02000295_BF__MAIN__15$', arg4=5, arg5=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=600, enable=False)
        play_system_sound_in_box(boxIds=[9000], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002952, textId=20002952, duration=3000) # 투기장 안으로 이동하세요.
        set_effect(triggerIds=[5000], visible=True) # TargetGuide
        set_effect(triggerIds=[5001], visible=True) # TargetGuide
        set_effect(triggerIds=[5002], visible=True) # TargetGuide

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return BattleReady01()


#  연출 종료 
class BattleReady01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9000], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002951, textId=20002951, duration=5000) # 투기장의 포악한 야수들이 몰려옵니다. 모두 처치하세요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리거01웨이브()


class 트리거01웨이브(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # TargetGuide
        set_effect(triggerIds=[5001], visible=False) # TargetGuide
        set_effect(triggerIds=[5002], visible=False) # TargetGuide
        set_mesh(triggerIds=[95001,95002,95003,95004,95005,95006], visible=False, arg3=0, arg4=0, arg5=2) # Stairs
        create_monster(spawnIds=[910,911], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리거02웨이브()


class 트리거02웨이브(state.State):
    def on_enter(self):
        create_monster(spawnIds=[912,913], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 트리거03웨이브()


class 트리거03웨이브(state.State):
    def on_enter(self):
        create_monster(spawnIds=[914,915], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 트리거04웨이브()


class 트리거04웨이브(state.State):
    def on_enter(self):
        create_monster(spawnIds=[916,917], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[910,911,912,913,914,915,916,917]):
            return BossAct01()


class BossAct01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossAct02()


class BossAct02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=603, enable=True)
        set_effect(triggerIds=[5103], visible=True) # BossAct
        set_skip(state=BossAct03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return BossAct03()


class BossAct03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=603, enable=False)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossBattle01()


#  보스 전투 돌입 
class BossBattle01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[4100]) # BossActor
        create_monster(spawnIds=[4101], arg2=True) # BossBattle

    def on_tick(self) -> state.State:
        if user_value(key='LuminaArmyJoin', value=1):
            return BossBattle02()
        if monster_dead(boxIds=[4101]):
            return BossBattle02()


#  보스 체력 30% 루미나 해방군 전투 합류
class BossBattle02(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        destroy_monster(spawnIds=[900,901,902])
        change_monster(removeSpawnId=800, addSpawnId=810)
        change_monster(removeSpawnId=801, addSpawnId=811)
        change_monster(removeSpawnId=802, addSpawnId=812)
        change_monster(removeSpawnId=803, addSpawnId=813)
        change_monster(removeSpawnId=804, addSpawnId=814)
        change_monster(removeSpawnId=202, addSpawnId=203)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BossBattle03()


class BossBattle03(state.State):
    def on_enter(self):
        move_npc(spawnId=810, patrolName='MS2PatrolData_800')
        move_npc(spawnId=811, patrolName='MS2PatrolData_801')
        move_npc(spawnId=812, patrolName='MS2PatrolData_802')
        move_npc(spawnId=813, patrolName='MS2PatrolData_803')
        move_npc(spawnId=814, patrolName='MS2PatrolData_804')
        move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        set_conversation(type=1, spawnId=203, script='$02000295_BF__MAIN__16$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=203, script='$02000295_BF__MAIN__17$', arg4=4, arg5=7)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4101]):
            return BattleEnd01()


class BattleEnd01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_mesh(triggerIds=[95001,95002,95003,95004,95005,95006], visible=True, arg3=0, arg4=0, arg5=2) # Stairs
        move_npc(spawnId=203, patrolName='MS2PatrolData_204')
        set_conversation(type=1, spawnId=203, script='$02000295_BF__MAIN__18$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BattleEnd02()


class BattleEnd02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BattleEnd03()


class BattleEnd03(state.State):
    def on_enter(self):
        move_user(mapId=2000295, portalId=3, boxId=9000) # 반경 150 영역

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ReleaseSlaves01()


class ReleaseSlaves01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReleaseSlaves02()


class ReleaseSlaves02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045], visible=True, arg3=0, arg4=0, arg5=2) # Deck01_ClearOn
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246], visible=True, arg3=200, arg4=30, arg5=2) # Deck02_ClearOn
        set_effect(triggerIds=[5100], visible=True) # Wheel
        set_effect(triggerIds=[5101], visible=True) # MetalDoorOpen

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReleaseSlaves03()


class ReleaseSlaves03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159], visible=False, arg3=100, arg4=0, arg5=0) # Jail
        set_breakable(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], enabled=True) # Jail_Mid
        set_breakable(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], enabled=True) # Jail_Under
        set_visible_breakable_object(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], arg2=True) # Jail_Mid
        set_visible_breakable_object(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], arg2=True) # Jail_Under
        change_monster(removeSpawnId=301, addSpawnId=401)
        change_monster(removeSpawnId=302, addSpawnId=402)
        change_monster(removeSpawnId=303, addSpawnId=403)
        change_monster(removeSpawnId=304, addSpawnId=404)
        change_monster(removeSpawnId=305, addSpawnId=405)
        change_monster(removeSpawnId=306, addSpawnId=406)
        change_monster(removeSpawnId=307, addSpawnId=407)
        change_monster(removeSpawnId=308, addSpawnId=408)
        change_monster(removeSpawnId=309, addSpawnId=409)
        change_monster(removeSpawnId=310, addSpawnId=410)
        change_monster(removeSpawnId=311, addSpawnId=411)
        change_monster(removeSpawnId=312, addSpawnId=412)
        change_monster(removeSpawnId=313, addSpawnId=413)
        change_monster(removeSpawnId=314, addSpawnId=414)
        change_monster(removeSpawnId=315, addSpawnId=415)
        change_monster(removeSpawnId=316, addSpawnId=416)
        change_monster(removeSpawnId=317, addSpawnId=417)
        change_monster(removeSpawnId=318, addSpawnId=418)
        change_monster(removeSpawnId=320, addSpawnId=420)
        change_monster(removeSpawnId=321, addSpawnId=421)
        change_monster(removeSpawnId=322, addSpawnId=422)
        change_monster(removeSpawnId=323, addSpawnId=423)
        change_monster(removeSpawnId=324, addSpawnId=424)
        change_monster(removeSpawnId=325, addSpawnId=425)
        change_monster(removeSpawnId=326, addSpawnId=426)
        change_monster(removeSpawnId=327, addSpawnId=427)
        change_monster(removeSpawnId=328, addSpawnId=428)
        change_monster(removeSpawnId=329, addSpawnId=429)
        change_monster(removeSpawnId=330, addSpawnId=430)
        change_monster(removeSpawnId=331, addSpawnId=431)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ReleaseSlaves04()


class ReleaseSlaves04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # MetalDoorClose
        set_effect(triggerIds=[5100], visible=False) # Wheel
        move_npc(spawnId=401, patrolName='MS2PatrolData_301')
        move_npc(spawnId=402, patrolName='MS2PatrolData_302')
        move_npc(spawnId=403, patrolName='MS2PatrolData_303')
        move_npc(spawnId=404, patrolName='MS2PatrolData_304')
        move_npc(spawnId=405, patrolName='MS2PatrolData_305')
        move_npc(spawnId=406, patrolName='MS2PatrolData_306')
        move_npc(spawnId=407, patrolName='MS2PatrolData_307')
        move_npc(spawnId=408, patrolName='MS2PatrolData_308')
        move_npc(spawnId=409, patrolName='MS2PatrolData_309')
        move_npc(spawnId=410, patrolName='MS2PatrolData_310')
        move_npc(spawnId=411, patrolName='MS2PatrolData_311')
        move_npc(spawnId=412, patrolName='MS2PatrolData_312')
        move_npc(spawnId=413, patrolName='MS2PatrolData_313')
        move_npc(spawnId=414, patrolName='MS2PatrolData_314')
        move_npc(spawnId=415, patrolName='MS2PatrolData_315')
        move_npc(spawnId=416, patrolName='MS2PatrolData_316')
        move_npc(spawnId=417, patrolName='MS2PatrolData_317')
        move_npc(spawnId=418, patrolName='MS2PatrolData_318')
        move_npc(spawnId=420, patrolName='MS2PatrolData_320')
        move_npc(spawnId=421, patrolName='MS2PatrolData_321')
        move_npc(spawnId=422, patrolName='MS2PatrolData_322')
        move_npc(spawnId=423, patrolName='MS2PatrolData_323')
        move_npc(spawnId=424, patrolName='MS2PatrolData_324')
        move_npc(spawnId=425, patrolName='MS2PatrolData_325')
        move_npc(spawnId=426, patrolName='MS2PatrolData_326')
        move_npc(spawnId=427, patrolName='MS2PatrolData_327')
        move_npc(spawnId=428, patrolName='MS2PatrolData_328')
        move_npc(spawnId=429, patrolName='MS2PatrolData_329')
        move_npc(spawnId=430, patrolName='MS2PatrolData_330')
        move_npc(spawnId=431, patrolName='MS2PatrolData_331')
        set_conversation(type=1, spawnId=402, script='$02000295_BF__MAIN__19$', arg4=2, arg5=0) # Right
        set_conversation(type=1, spawnId=410, script='$02000295_BF__MAIN__20$', arg4=3, arg5=0) # Right
        set_conversation(type=1, spawnId=418, script='$02000295_BF__MAIN__21$', arg4=3, arg5=1) # Right
        set_conversation(type=1, spawnId=416, script='$02000295_BF__MAIN__22$', arg4=2, arg5=2) # Right
        set_conversation(type=1, spawnId=407, script='$02000295_BF__MAIN__23$', arg4=3, arg5=2) # Right
        set_conversation(type=1, spawnId=412, script='$02000295_BF__MAIN__24$', arg4=3, arg5=3) # Right
        set_conversation(type=1, spawnId=405, script='$02000295_BF__MAIN__25$', arg4=3, arg5=3) # Right
        set_conversation(type=1, spawnId=414, script='$02000295_BF__MAIN__26$', arg4=3, arg5=3) # Right
        set_conversation(type=1, spawnId=425, script='$02000295_BF__MAIN__27$', arg4=2, arg5=0) # Left
        set_conversation(type=1, spawnId=421, script='$02000295_BF__MAIN__28$', arg4=3, arg5=1) # Left
        set_conversation(type=1, spawnId=424, script='$02000295_BF__MAIN__29$', arg4=3, arg5=2) # Left
        set_conversation(type=1, spawnId=427, script='$02000295_BF__MAIN__30$', arg4=3, arg5=2) # Left
        set_conversation(type=1, spawnId=430, script='$02000295_BF__MAIN__31$', arg4=3, arg5=3) # Left
        set_skip(state=ReleaseSlaves05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return ReleaseSlaves05()


class ReleaseSlaves05(state.State):
    def on_enter(self):
        set_skip()
        create_monster(spawnIds=[200], arg2=True)
        move_npc(spawnId=200, patrolName='MS2PatrolData_199')
        select_camera(triggerId=602, enable=False)
        select_camera(triggerId=603, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return ToBeContinued01()


class ToBeContinued01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000006, script='$02000295_BF__MAIN__32$', arg4=4)
        set_skip(state=Quit01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_skip()
        remove_balloon_talk(spawnId=200)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=603, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        set_achievement(triggerId=9000, type='trigger', achieve='ReleaseTheSlaves')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit03()


class Quit03(state.State):
    def on_enter(self):
        set_achievement(triggerId=9000, type='trigger', achieve='ClearKatramusfirst')
        set_ladder(triggerIds=[3002], visible=True, animationEffect=True, animationDelay=10)
        set_ladder(triggerIds=[3003], visible=True, animationEffect=True, animationDelay=12)
        set_ladder(triggerIds=[3004], visible=True, animationEffect=True, animationDelay=14)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        dungeon_clear()


