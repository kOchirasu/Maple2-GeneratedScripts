""" trigger/52100041_qd/main.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.shadow_expedition(type='CloseBossGauge')
        self.set_interact_object(triggerIds=[10002071], state=1)
        self.set_interact_object(triggerIds=[10002072], state=1)
        self.set_interact_object(triggerIds=[10002073], state=1)
        self.set_interact_object(triggerIds=[10002074], state=1)
        self.set_interact_object(triggerIds=[10002075], state=1)
        self.set_interact_object(triggerIds=[10002076], state=1)
        self.set_interact_object(triggerIds=[10002077], state=1)
        self.set_mesh(triggerIds=[1001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1002], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1801,1802], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[101,102,103,104], animationEffect=False)
        self.create_monster(spawnIds=[199], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return DungeonStart(self.ctx)


# <import path="./Data/Xml/Trigger/Dungeon_Common/CheckUserCount.xml" />
class DungeonStart(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=start)
        self.select_camera_path(pathIds=[8100,8101,8102], returnView=False)
        self.set_ambient_light(primary=[120,120,120])
        self.set_directional_light(diffuseColor=[10,10,10], specularColor=[0,0,0])
        self.add_buff(boxIds=[701], skillId=71000009, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return start(self.ctx)
        if self.shadow_expedition_reach_point(point=1000):
            self.shadow_expedition(type='CloseBossGauge')
            return boss_scene(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1801,1802], visible=False, arg3=0, delay=0, scale=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=1000):
            self.shadow_expedition(type='CloseBossGauge')
            return boss_scene(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[105,106,107,108,109,111,112,113,114,115,116,117,118,119])
        self.destroy_monster(spawnIds=[120,121,122,123,124,125,126,127,128,129])
        self.destroy_monster(spawnIds=[130,131,132,133,134,135,136])
        self.destroy_monster(spawnIds=[150,151,152,153,154,155,156])


class boss_scene(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7999], visible=True)
        self.create_monster(spawnIds=[1999], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=boss)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return boss_scene_02(self.ctx)


class boss_scene_02(common.Trigger):
    def on_enter(self):
        self.set_skip(state=boss)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8006,8007], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return boss_scene_03(self.ctx)


class boss_scene_03(common.Trigger):
    def on_enter(self):
        self.set_skip(state=boss)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return boss_scene_04(self.ctx)


class boss_scene_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_skip(state=boss)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return boss(self.ctx)

    def on_exit(self):
        self.reset_camera(interpolationTime=0)


class boss(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_event_ui(type=1, arg2='$52100041_QD__MAIN__0$', arg3='3000')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return dungeonClear_ready(self.ctx)


class dungeonClear_ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return dungeonClear(self.ctx)


class dungeonClear(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010068, portalId=6001)
        # <action name="포탈을설정한다" arg1="1" arg2="1" arg3="1" arg4="1"/>
        self.set_effect(triggerIds=[7999], visible=False)
        self.set_effect(triggerIds=[7998], visible=True)
        self.dungeon_clear()


initial_state = idle
