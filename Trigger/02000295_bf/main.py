""" trigger/02000295_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[3000], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[3001], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[3002], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[3003], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[3004], visible=False, animationEffect=False)
        self.destroy_monster(spawnIds=[910,911,912,913,914,915,916,917])
        self.create_monster(spawnIds=[4100], animationEffect=False) # BossActor
        self.destroy_monster(spawnIds=[4101]) # BossBattle
        self.create_monster(spawnIds=[900,901,902], animationEffect=True) # MobEnterance
        self.create_monster(spawnIds=[800,801,802,803,804], animationEffect=True) # LuminaBattle
        self.create_monster(spawnIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331], animationEffect=True) # SlaveNpc
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_agent(triggerIds=[8009], visible=True)
        self.set_agent(triggerIds=[8010], visible=True)
        self.set_agent(triggerIds=[8011], visible=True)
        self.set_agent(triggerIds=[8012], visible=True)
        self.set_effect(triggerIds=[5000], visible=False) # TargetGuide
        self.set_effect(triggerIds=[5001], visible=False) # TargetGuide
        self.set_effect(triggerIds=[5002], visible=False) # TargetGuide
        self.set_effect(triggerIds=[5100], visible=False) # Wheel
        self.set_effect(triggerIds=[5101], visible=False) # MetalDoorOpen
        self.set_effect(triggerIds=[5102], visible=False) # MetalDoorClose
        self.set_effect(triggerIds=[5103], visible=False) # BossAct
        self.set_breakable(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], enable=False) # Jail_Mid
        self.set_breakable(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], enable=False) # Jail_Under
        self.set_visible_breakable_object(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=False) # Jail_Mid
        self.set_visible_breakable_object(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], visible=False) # Jail_Under
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[95001,95002,95003,95004,95005,95006], visible=True, arg3=0, delay=0, scale=0) # Stairs
        self.set_mesh(triggerIds=[2000], visible=True, arg3=0, delay=0, scale=0) # InvisibleEnteranceBarrier
        self.set_mesh(triggerIds=[2001,2002], visible=True, arg3=0, delay=0, scale=0) # InvisibleJailBlock_alwaysON
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045], visible=False, arg3=0, delay=0, scale=0) # Deck01_ClearOn
        self.set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246], visible=False, arg3=0, delay=0, scale=0) # Deck02_ClearOn
        self.set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159], visible=True, arg3=0, delay=0, scale=0) # Jail
        self.set_user_value(key='LuminaArmyJoin', value=0)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcMonologue01(self.ctx)


# 연출 시작
class NpcMonologue01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.set_skip(state=CameraWalk02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=1, spawnId=201, script='$02000295_BF__MAIN__0$', arg4=3, arg5=0)
        self.set_skip(state=CameraWalk02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraWalk01(self.ctx)


# 철창 안 노예 말풍선 연출
class CameraWalk01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=True)
        self.set_skip(state=CameraWalk02)
        self.add_balloon_talk(spawnId=301, msg='$02000295_BF__MAIN__1$', duration=3000, delayTick=2000) # Right
        self.add_balloon_talk(spawnId=310, msg='$02000295_BF__MAIN__2$', duration=3000, delayTick=2000) # Right
        self.add_balloon_talk(spawnId=318, msg='$02000295_BF__MAIN__3$', duration=3000, delayTick=3000) # Right
        self.add_balloon_talk(spawnId=316, msg='$02000295_BF__MAIN__4$', duration=3000, delayTick=3000) # Right
        self.add_balloon_talk(spawnId=307, msg='$02000295_BF__MAIN__5$', duration=3000, delayTick=4000) # Right
        self.add_balloon_talk(spawnId=312, msg='$02000295_BF__MAIN__6$', duration=3000, delayTick=4000) # Right
        self.add_balloon_talk(spawnId=305, msg='$02000295_BF__MAIN__7$', duration=3000, delayTick=5000) # Right
        self.add_balloon_talk(spawnId=314, msg='$02000295_BF__MAIN__8$', duration=3000, delayTick=5000) # Right
        self.add_balloon_talk(spawnId=325, msg='$02000295_BF__MAIN__9$', duration=3000, delayTick=2000) # Left
        self.add_balloon_talk(spawnId=323, msg='$02000295_BF__MAIN__10$', duration=3000, delayTick=2000) # Left
        self.add_balloon_talk(spawnId=323, msg='$02000295_BF__MAIN__11$', duration=3000, delayTick=3000) # Left
        self.add_balloon_talk(spawnId=327, msg='$02000295_BF__MAIN__12$', duration=3000, delayTick=4000) # Left
        self.add_balloon_talk(spawnId=330, msg='$02000295_BF__MAIN__13$', duration=3000, delayTick=5000) # Left

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return CameraWalk02(self.ctx)


class CameraWalk02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=False)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraWalk03(self.ctx)


class CameraWalk03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_ladder(triggerIds=[3000], visible=True, animationEffect=True, animationDelay=10)
        self.set_ladder(triggerIds=[3001], visible=True, animationEffect=True, animationDelay=12)
        self.set_mesh(triggerIds=[2000], visible=False, arg3=0, delay=0, scale=0) # InvisibleEnteranceBarrier
        self.select_camera(triggerId=600, enable=True)
        self.set_skip(state=CameraWalk05)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk04(self.ctx)


class CameraWalk04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=1, spawnId=202, script='$02000295_BF__MAIN__14$', arg4=3, arg5=1)
        self.set_skip(state=CameraWalk05)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return CameraWalk05(self.ctx)


class CameraWalk05(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        self.set_conversation(type=1, spawnId=202, script='$02000295_BF__MAIN__15$', arg4=5, arg5=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=600, enable=False)
        self.play_system_sound_in_box(boxIds=[9000], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002952, textId=20002952, duration=3000) # 투기장 안으로 이동하세요.
        self.set_effect(triggerIds=[5000], visible=True) # TargetGuide
        self.set_effect(triggerIds=[5001], visible=True) # TargetGuide
        self.set_effect(triggerIds=[5002], visible=True) # TargetGuide

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return BattleReady01(self.ctx)


# 연출 종료
class BattleReady01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9000], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002951, textId=20002951, duration=5000) # 투기장의 포악한 야수들이 몰려옵니다. 모두 처치하세요.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트리거01웨이브(self.ctx)


class 트리거01웨이브(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # TargetGuide
        self.set_effect(triggerIds=[5001], visible=False) # TargetGuide
        self.set_effect(triggerIds=[5002], visible=False) # TargetGuide
        self.set_mesh(triggerIds=[95001,95002,95003,95004,95005,95006], visible=False, arg3=0, delay=0, scale=2) # Stairs
        self.create_monster(spawnIds=[910,911], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거02웨이브(self.ctx)


class 트리거02웨이브(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[912,913], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 트리거03웨이브(self.ctx)


class 트리거03웨이브(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[914,915], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 트리거04웨이브(self.ctx)


class 트리거04웨이브(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[916,917], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[910,911,912,913,914,915,916,917]):
            return BossAct01(self.ctx)


class BossAct01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossAct02(self.ctx)


class BossAct02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=603, enable=True)
        self.set_effect(triggerIds=[5103], visible=True) # BossAct
        self.set_skip(state=BossAct03)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return BossAct03(self.ctx)


class BossAct03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=603, enable=False)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossBattle01(self.ctx)


# 보스 전투 돌입
class BossBattle01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[4100]) # BossActor
        self.create_monster(spawnIds=[4101], animationEffect=True) # BossBattle

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='LuminaArmyJoin', value=1):
            return BossBattle02(self.ctx)
        if self.monster_dead(boxIds=[4101]):
            return BossBattle02(self.ctx)


# 보스 체력 30% 루미나 해방군 전투 합류
class BossBattle02(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_agent(triggerIds=[8011], visible=False)
        self.set_agent(triggerIds=[8012], visible=False)
        self.destroy_monster(spawnIds=[900,901,902])
        self.change_monster(removeSpawnId=800, addSpawnId=810)
        self.change_monster(removeSpawnId=801, addSpawnId=811)
        self.change_monster(removeSpawnId=802, addSpawnId=812)
        self.change_monster(removeSpawnId=803, addSpawnId=813)
        self.change_monster(removeSpawnId=804, addSpawnId=814)
        self.change_monster(removeSpawnId=202, addSpawnId=203)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BossBattle03(self.ctx)


class BossBattle03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=810, patrolName='MS2PatrolData_800')
        self.move_npc(spawnId=811, patrolName='MS2PatrolData_801')
        self.move_npc(spawnId=812, patrolName='MS2PatrolData_802')
        self.move_npc(spawnId=813, patrolName='MS2PatrolData_803')
        self.move_npc(spawnId=814, patrolName='MS2PatrolData_804')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        self.set_conversation(type=1, spawnId=203, script='$02000295_BF__MAIN__16$', arg4=3, arg5=3)
        self.set_conversation(type=1, spawnId=203, script='$02000295_BF__MAIN__17$', arg4=4, arg5=7)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4101]):
            return BattleEnd01(self.ctx)


class BattleEnd01(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_mesh(triggerIds=[95001,95002,95003,95004,95005,95006], visible=True, arg3=0, delay=0, scale=2) # Stairs
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_204')
        self.set_conversation(type=1, spawnId=203, script='$02000295_BF__MAIN__18$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return BattleEnd02(self.ctx)


class BattleEnd02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleEnd03(self.ctx)


class BattleEnd03(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000295, portalId=3, boxId=9000) # 반경 150 영역

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return ReleaseSlaves01(self.ctx)


class ReleaseSlaves01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReleaseSlaves02(self.ctx)


class ReleaseSlaves02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045], visible=True, arg3=0, delay=0, scale=2) # Deck01_ClearOn
        self.set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246], visible=True, arg3=200, delay=30, scale=2) # Deck02_ClearOn
        self.set_effect(triggerIds=[5100], visible=True) # Wheel
        self.set_effect(triggerIds=[5101], visible=True) # MetalDoorOpen

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReleaseSlaves03(self.ctx)


class ReleaseSlaves03(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159], visible=False, arg3=100, delay=0, scale=0) # Jail
        self.set_breakable(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], enable=True) # Jail_Mid
        self.set_breakable(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], enable=True) # Jail_Under
        self.set_visible_breakable_object(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=True) # Jail_Mid
        self.set_visible_breakable_object(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], visible=True) # Jail_Under
        self.change_monster(removeSpawnId=301, addSpawnId=401)
        self.change_monster(removeSpawnId=302, addSpawnId=402)
        self.change_monster(removeSpawnId=303, addSpawnId=403)
        self.change_monster(removeSpawnId=304, addSpawnId=404)
        self.change_monster(removeSpawnId=305, addSpawnId=405)
        self.change_monster(removeSpawnId=306, addSpawnId=406)
        self.change_monster(removeSpawnId=307, addSpawnId=407)
        self.change_monster(removeSpawnId=308, addSpawnId=408)
        self.change_monster(removeSpawnId=309, addSpawnId=409)
        self.change_monster(removeSpawnId=310, addSpawnId=410)
        self.change_monster(removeSpawnId=311, addSpawnId=411)
        self.change_monster(removeSpawnId=312, addSpawnId=412)
        self.change_monster(removeSpawnId=313, addSpawnId=413)
        self.change_monster(removeSpawnId=314, addSpawnId=414)
        self.change_monster(removeSpawnId=315, addSpawnId=415)
        self.change_monster(removeSpawnId=316, addSpawnId=416)
        self.change_monster(removeSpawnId=317, addSpawnId=417)
        self.change_monster(removeSpawnId=318, addSpawnId=418)
        self.change_monster(removeSpawnId=320, addSpawnId=420)
        self.change_monster(removeSpawnId=321, addSpawnId=421)
        self.change_monster(removeSpawnId=322, addSpawnId=422)
        self.change_monster(removeSpawnId=323, addSpawnId=423)
        self.change_monster(removeSpawnId=324, addSpawnId=424)
        self.change_monster(removeSpawnId=325, addSpawnId=425)
        self.change_monster(removeSpawnId=326, addSpawnId=426)
        self.change_monster(removeSpawnId=327, addSpawnId=427)
        self.change_monster(removeSpawnId=328, addSpawnId=428)
        self.change_monster(removeSpawnId=329, addSpawnId=429)
        self.change_monster(removeSpawnId=330, addSpawnId=430)
        self.change_monster(removeSpawnId=331, addSpawnId=431)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return ReleaseSlaves04(self.ctx)


class ReleaseSlaves04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # MetalDoorClose
        self.set_effect(triggerIds=[5100], visible=False) # Wheel
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_301')
        self.move_npc(spawnId=402, patrolName='MS2PatrolData_302')
        self.move_npc(spawnId=403, patrolName='MS2PatrolData_303')
        self.move_npc(spawnId=404, patrolName='MS2PatrolData_304')
        self.move_npc(spawnId=405, patrolName='MS2PatrolData_305')
        self.move_npc(spawnId=406, patrolName='MS2PatrolData_306')
        self.move_npc(spawnId=407, patrolName='MS2PatrolData_307')
        self.move_npc(spawnId=408, patrolName='MS2PatrolData_308')
        self.move_npc(spawnId=409, patrolName='MS2PatrolData_309')
        self.move_npc(spawnId=410, patrolName='MS2PatrolData_310')
        self.move_npc(spawnId=411, patrolName='MS2PatrolData_311')
        self.move_npc(spawnId=412, patrolName='MS2PatrolData_312')
        self.move_npc(spawnId=413, patrolName='MS2PatrolData_313')
        self.move_npc(spawnId=414, patrolName='MS2PatrolData_314')
        self.move_npc(spawnId=415, patrolName='MS2PatrolData_315')
        self.move_npc(spawnId=416, patrolName='MS2PatrolData_316')
        self.move_npc(spawnId=417, patrolName='MS2PatrolData_317')
        self.move_npc(spawnId=418, patrolName='MS2PatrolData_318')
        self.move_npc(spawnId=420, patrolName='MS2PatrolData_320')
        self.move_npc(spawnId=421, patrolName='MS2PatrolData_321')
        self.move_npc(spawnId=422, patrolName='MS2PatrolData_322')
        self.move_npc(spawnId=423, patrolName='MS2PatrolData_323')
        self.move_npc(spawnId=424, patrolName='MS2PatrolData_324')
        self.move_npc(spawnId=425, patrolName='MS2PatrolData_325')
        self.move_npc(spawnId=426, patrolName='MS2PatrolData_326')
        self.move_npc(spawnId=427, patrolName='MS2PatrolData_327')
        self.move_npc(spawnId=428, patrolName='MS2PatrolData_328')
        self.move_npc(spawnId=429, patrolName='MS2PatrolData_329')
        self.move_npc(spawnId=430, patrolName='MS2PatrolData_330')
        self.move_npc(spawnId=431, patrolName='MS2PatrolData_331')
        self.set_conversation(type=1, spawnId=402, script='$02000295_BF__MAIN__19$', arg4=2, arg5=0) # Right
        self.set_conversation(type=1, spawnId=410, script='$02000295_BF__MAIN__20$', arg4=3, arg5=0) # Right
        self.set_conversation(type=1, spawnId=418, script='$02000295_BF__MAIN__21$', arg4=3, arg5=1) # Right
        self.set_conversation(type=1, spawnId=416, script='$02000295_BF__MAIN__22$', arg4=2, arg5=2) # Right
        self.set_conversation(type=1, spawnId=407, script='$02000295_BF__MAIN__23$', arg4=3, arg5=2) # Right
        self.set_conversation(type=1, spawnId=412, script='$02000295_BF__MAIN__24$', arg4=3, arg5=3) # Right
        self.set_conversation(type=1, spawnId=405, script='$02000295_BF__MAIN__25$', arg4=3, arg5=3) # Right
        self.set_conversation(type=1, spawnId=414, script='$02000295_BF__MAIN__26$', arg4=3, arg5=3) # Right
        self.set_conversation(type=1, spawnId=425, script='$02000295_BF__MAIN__27$', arg4=2, arg5=0) # Left
        self.set_conversation(type=1, spawnId=421, script='$02000295_BF__MAIN__28$', arg4=3, arg5=1) # Left
        self.set_conversation(type=1, spawnId=424, script='$02000295_BF__MAIN__29$', arg4=3, arg5=2) # Left
        self.set_conversation(type=1, spawnId=427, script='$02000295_BF__MAIN__30$', arg4=3, arg5=2) # Left
        self.set_conversation(type=1, spawnId=430, script='$02000295_BF__MAIN__31$', arg4=3, arg5=3) # Left
        self.set_skip(state=ReleaseSlaves05)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return ReleaseSlaves05(self.ctx)


class ReleaseSlaves05(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.create_monster(spawnIds=[200], animationEffect=True)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_199')
        self.select_camera(triggerId=602, enable=False)
        self.select_camera(triggerId=603, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return ToBeContinued01(self.ctx)


class ToBeContinued01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000006, script='$02000295_BF__MAIN__32$', arg4=4)
        self.set_skip(state=Quit01)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit01(self.ctx)


class Quit01(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_balloon_talk(spawnId=200)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=603, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9000, type='trigger', achieve='ReleaseTheSlaves')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit03(self.ctx)


class Quit03(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9000, type='trigger', achieve='ClearKatramusfirst')
        self.set_ladder(triggerIds=[3002], visible=True, animationEffect=True, animationDelay=10)
        self.set_ladder(triggerIds=[3003], visible=True, animationEffect=True, animationDelay=12)
        self.set_ladder(triggerIds=[3004], visible=True, animationEffect=True, animationDelay=14)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.dungeon_clear()


initial_state = 대기
