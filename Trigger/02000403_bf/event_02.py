""" trigger/02000403_bf/event_02.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000030], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001], visible=False, arg3=0, arg4=200, arg5=15)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703]):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[101,102,103,104])
        select_camera_path(pathIds=[8001,8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        set_skip(state=scene_06_ready)
        set_conversation(type=2, spawnId=11001956, script='$02000403_BF__EVENT_02__0$', arg4=5)
        move_npc(spawnId=199, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_skip(state=scene_06_ready)
        set_conversation(type=2, spawnId=11001956, script='$02000403_BF__EVENT_02__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        set_skip(state=scene_06_ready)
        select_camera_path(pathIds=[8003,8004], returnView=False)
        set_mesh(triggerIds=[1002], visible=True, arg3=0, arg4=200, arg5=35)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199], visible=True, arg3=0, arg4=200, arg5=35)
        set_conversation(type=2, spawnId=11001956, script='$02000403_BF__EVENT_02__2$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_skip(state=scene_06_ready)
        select_camera_path(pathIds=[8005], returnView=False)
        set_npc_emotion_sequence(spawnId=199, sequenceName='Bore_B')
        set_conversation(type=2, spawnId=11001956, script='$02000403_BF__EVENT_02__3$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[199])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_06_ready()


class scene_06_ready(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000031], state=1)
        set_interact_object(triggerIds=[12000032], state=1)
        set_interact_object(triggerIds=[12000033], state=1)
        set_interact_object(triggerIds=[12000034], state=1)
        set_interact_object(triggerIds=[12000035], state=1)
        set_interact_object(triggerIds=[12000036], state=1)
        destroy_monster(spawnIds=[199])
        set_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_mesh(triggerIds=[1002], visible=True, arg3=0, arg4=200, arg5=35)
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199], visible=True, arg3=0, arg4=200, arg5=35)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        shadow_expedition(type='OpenBossGauge', title='$02000403_BF__EVENT_02__9$', maxGaugePoint=1000) # 진행 바 표기
        destroy_monster(spawnIds=[199])
        create_monster(spawnIds=[105,106,107,108,109,111,112,113,114,115,116,117,118,119], arg2=False)
        create_monster(spawnIds=[120,121,122,123,124,125,126,127,128,129], arg2=False)
        create_monster(spawnIds=[130,131,132,133,134,135,136], arg2=False)
        create_monster(spawnIds=[150,151,152,153,154,155,156], arg2=False)
        reset_camera(interpolationTime=0)
        set_event_ui(type=1, arg2='$02000403_BF__EVENT_02__4$', arg3='3000')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106,105,116,115]):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        set_achievement(triggerId=720, type='trigger', achieve='Hauntedmansion')
        create_monster(spawnIds=[181,182,183,184], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_09()


class scene_09(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=181, script='$02000403_BF__EVENT_02__5$', arg4=3, arg5=2)
        set_conversation(type=1, spawnId=182, script='$02000403_BF__EVENT_02__6$', arg4=3, arg5=4)
        set_conversation(type=1, spawnId=183, script='$02000403_BF__EVENT_02__7$', arg4=3, arg5=8)
        set_conversation(type=1, spawnId=184, script='$02000403_BF__EVENT_02__8$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return scene_10()


class scene_10(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[181,182,183,184])

