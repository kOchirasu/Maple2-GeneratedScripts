""" trigger/02000471_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040314, key='TimerStart', value=0)
        set_user_value(triggerId=2040322, key='Boss', value=0)
        set_user_value(triggerId=2040324, key='respawn', value=0)
        set_interact_object(triggerIds=[10002018], state=1)
        set_interact_object(triggerIds=[10002019], state=1)
        set_interact_object(triggerIds=[10002020], state=1)
        set_interact_object(triggerIds=[10002021], state=1)
        set_interact_object(triggerIds=[10002022], state=1)
        set_interact_object(triggerIds=[10002023], state=1)
        set_interact_object(triggerIds=[10002024], state=1)
        set_interact_object(triggerIds=[10002106], state=0)
        set_interact_object(triggerIds=[10002107], state=0)
        set_mesh(triggerIds=[1001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1002], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1801,1802], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[101,102,103,104], arg2=False)
        create_monster(spawnIds=[199], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return Ready()

state.DungeonStart = DungeonStart


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=start)
        select_camera_path(pathIds=[8100,8101,8102], returnView=False)
        set_ambient_light(primary=[120,120,120])
        set_directional_light(diffuseColor=[10,10,10], specularColor=[0,0,0])
        add_buff(boxIds=[701], skillId=71000009, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return start()


class start(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1801,1802], visible=False, arg3=0, arg4=0, arg5=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if user_value(key='TimerEnd', value=1):
            return dungeonfail()
        if user_value(key='InteractClear', value=1):
            return boss_scene()

    def on_exit(self):
        destroy_monster(spawnIds=[105,106,107,108,109,111,112,113,114,115,116,117,118,119])
        destroy_monster(spawnIds=[120,121,122,123,124,125,126,127,128,129])
        destroy_monster(spawnIds=[130,131,132,133,134,135,136])
        destroy_monster(spawnIds=[150,151,152,153,154,155,156])


class dungeonfail(state.State):
    def on_enter(self):
        dungeon_fail()
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)


class boss_scene(state.State):
    def on_enter(self):
        set_scene_skip(state=boss, arg2='exit')
        set_sound(triggerId=9900, arg2=True) # 보스 등장하면 보스용 BGM으로 교체하기
        destroy_monster(spawnIds=[201,202,203,204,205,206])
        set_effect(triggerIds=[7999], visible=False)
        create_monster(spawnIds=[311,312,313,314,315,316,2000], arg2=False)
        set_user_value(triggerId=2040316, key='SpawnCheck', value=1)
        set_user_value(triggerId=2040317, key='SpawnCheck', value=1)
        set_user_value(triggerId=2040318, key='SpawnCheck', value=1)
        set_user_value(triggerId=2040319, key='SpawnCheck', value=1)
        set_user_value(triggerId=2040320, key='SpawnCheck', value=1)
        set_user_value(triggerId=2040321, key='SpawnCheck', value=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return boss_scene_02()


class boss_scene_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8006,8007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return boss_scene_03()


class boss_scene_03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return boss_scene_04()


class boss_scene_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return boss()

    def on_exit(self):
        reset_camera(interpolationTime=0)


class boss(state.State):
    def on_enter(self):
        set_scene_skip()
        destroy_monster(spawnIds=[311,312,313,314,315,316,2000])
        create_monster(spawnIds=[1999], arg2=False)
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False)
        set_user_value(triggerId=2040324, key='respawn', value=1)
        set_user_value(triggerId=2040316, key='Buff', value=1)
        set_user_value(triggerId=2040317, key='Buff', value=1)
        set_user_value(triggerId=2040318, key='Buff', value=1)
        set_user_value(triggerId=2040319, key='Buff', value=1)
        set_user_value(triggerId=2040320, key='Buff', value=1)
        set_user_value(triggerId=2040321, key='Buff', value=1)
        set_user_value(triggerId=2040322, key='Boss', value=1)
        set_interact_object(triggerIds=[10002018], state=2)
        set_interact_object(triggerIds=[10002019], state=2)
        set_interact_object(triggerIds=[10002020], state=2)
        set_interact_object(triggerIds=[10002021], state=2)
        set_interact_object(triggerIds=[10002022], state=2)
        set_interact_object(triggerIds=[10002023], state=2)
        set_interact_object(triggerIds=[10002024], state=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_event_ui(type=1, arg2='$02000471_BF__MAIN__0$', arg3='3000')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return dungeonClear_ready()


class dungeonClear_ready(state.State):
    def on_enter(self):
        set_sound(triggerId=9900, arg2=False)
        set_user_value(triggerId=2040324, key='respawn', value=2)
        destroy_monster(spawnIds=[301,302,303,304,305,306])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return dungeonClear()


class dungeonClear(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[7999], visible=False)
        set_effect(triggerIds=[7998], visible=True)


