""" trigger/52100302_qd/field_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000507], state=2)
        set_interact_object(triggerIds=[12000508], state=2)
        set_interact_object(triggerIds=[12000509], state=2)
        set_interact_object(triggerIds=[12000510], state=2)
        set_interact_object(triggerIds=[12000511], state=2)
        set_interact_object(triggerIds=[12000512], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900003, key='Block', value=0)
            return ArriveBlock_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900003, key='Block', value=0)
            return ArriveBlock_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900003, key='Block', value=0)
            return ArriveBlock_3()


class ArriveBlock_1(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            create_monster(spawnIds=[2001], arg2=False)
            return ArriveBlock_Delay_1()


class ArriveBlock_Delay_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__0$', duration=3000)
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__1$', duration=4000)
            return Block_1_01()
        if monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000001], arg2=False)
            destroy_monster(spawnIds=[1000002], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000507], state=1)
            set_interact_object(triggerIds=[12000508], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=103, isEnable=False)
            enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08()


class Block_1_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5167):
            create_monster(spawnIds=[1000001], arg2=False)
            return Block_1_02()
        if monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000001], arg2=False)
            destroy_monster(spawnIds=[1000002], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000507], state=1)
            set_interact_object(triggerIds=[12000508], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=103, isEnable=False)
            enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08()


class Block_1_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4067):
            create_monster(spawnIds=[1000002], arg2=False)
            return Block_1()
        if monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000001], arg2=False)
            destroy_monster(spawnIds=[1000002], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000507], state=1)
            set_interact_object(triggerIds=[12000508], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=103, isEnable=False)
            enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000001], arg2=False)
            destroy_monster(spawnIds=[1000002], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000507], state=1)
            set_interact_object(triggerIds=[12000508], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=103, isEnable=False)
            enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08()


class ArriveBlock_2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            create_monster(spawnIds=[2002], arg2=False)
            return ArriveBlock_Delay_2()


class ArriveBlock_Delay_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__2$', duration=3000)
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__3$', duration=4000)
            return Block_2_01()
        if monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000003], arg2=False)
            destroy_monster(spawnIds=[1000004], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000509], state=1)
            set_interact_object(triggerIds=[12000510], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=104, isEnable=False)
            enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10()


class Block_2_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5167):
            create_monster(spawnIds=[1000003], arg2=False)
            return Block_2_02()
        if monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000003], arg2=False)
            destroy_monster(spawnIds=[1000004], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000509], state=1)
            set_interact_object(triggerIds=[12000510], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=104, isEnable=False)
            enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10()


class Block_2_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4067):
            create_monster(spawnIds=[1000004], arg2=False)
            return Block_2()
        if monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000003], arg2=False)
            destroy_monster(spawnIds=[1000004], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000509], state=1)
            set_interact_object(triggerIds=[12000510], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=104, isEnable=False)
            enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000003], arg2=False)
            destroy_monster(spawnIds=[1000004], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000509], state=1)
            set_interact_object(triggerIds=[12000510], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=104, isEnable=False)
            enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10()


class ArriveBlock_3(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            create_monster(spawnIds=[2003], arg2=False)
            return ArriveBlock_Delay_3()


class ArriveBlock_Delay_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__4$', duration=3000)
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__5$', duration=4000)
            return Block_3_01()
        if monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000005], arg2=False)
            destroy_monster(spawnIds=[1000006], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000511], state=1)
            set_interact_object(triggerIds=[12000512], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=105, isEnable=False)
            enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12()


class Block_3_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5167):
            create_monster(spawnIds=[1000005], arg2=False)
            return Block_3_02()
        if monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000005], arg2=False)
            destroy_monster(spawnIds=[1000006], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000511], state=1)
            set_interact_object(triggerIds=[12000512], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=105, isEnable=False)
            enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12()


class Block_3_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4067):
            create_monster(spawnIds=[1000006], arg2=False)
            return Block_3()
        if monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000005], arg2=False)
            destroy_monster(spawnIds=[1000006], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000511], state=1)
            set_interact_object(triggerIds=[12000512], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=105, isEnable=False)
            enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000005], arg2=False)
            destroy_monster(spawnIds=[1000006], arg2=False)
            destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            set_interact_object(triggerIds=[12000511], state=1)
            set_interact_object(triggerIds=[12000512], state=1)
            create_monster(spawnIds=[1110], arg2=False)
            create_monster(spawnIds=[1111], arg2=False)
            create_monster(spawnIds=[1112], arg2=False)
            create_monster(spawnIds=[1113], arg2=False)
            create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], arg2=False)
            create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], arg2=False)
            create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], arg2=False)
            create_monster(spawnIds=[1331,1332], arg2=False)
            enable_spawn_point_pc(spawnId=105, isEnable=False)
            enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12()


class CableOn_07_08(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000507], arg2=0):
            set_interact_object(triggerIds=[12000507], state=0)
            set_interact_object(triggerIds=[12000508], state=0)
            create_monster(spawnIds=[30005], arg2=False)
            set_mesh(triggerIds=[1101001,1101002,1101003,1101004,1101005,1101006,1101007,1101008,1101009,1101010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_07()
        if object_interacted(interactIds=[12000508], arg2=0):
            set_interact_object(triggerIds=[12000507], state=0)
            set_interact_object(triggerIds=[12000508], state=0)
            create_monster(spawnIds=[30006,30007], arg2=False)
            set_mesh(triggerIds=[1102001,1102002,1102003,1102004,1102005,1102006,1102007,1102008,1102009,1102010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_08()


class CableOn_09_10(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000509], arg2=0):
            set_interact_object(triggerIds=[12000509], state=0)
            set_interact_object(triggerIds=[12000510], state=0)
            create_monster(spawnIds=[30008], arg2=False)
            set_mesh(triggerIds=[1103001,1103002,1103003,1103004,1103005,1103006,1103007,1103008,1103009,1103010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_09()
        if object_interacted(interactIds=[12000510], arg2=0):
            set_interact_object(triggerIds=[12000509], state=0)
            set_interact_object(triggerIds=[12000510], state=0)
            create_monster(spawnIds=[30009], arg2=False)
            set_mesh(triggerIds=[1104001,1104002,1104003,1104004,1104005,1104006,1104007,1104008,1104009,1104010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_10()


class CableOn_11_12(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000511], arg2=0):
            set_interact_object(triggerIds=[12000511], state=0)
            set_interact_object(triggerIds=[12000512], state=0)
            create_monster(spawnIds=[30010,30011], arg2=False)
            set_mesh(triggerIds=[1105001,1105002,1105003,1105004,1105005,1105006,1105007,1105008,1105009,1105010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_11()
        if object_interacted(interactIds=[12000512], arg2=0):
            set_interact_object(triggerIds=[12000511], state=0)
            set_interact_object(triggerIds=[12000512], state=0)
            create_monster(spawnIds=[30012], arg2=False)
            set_mesh(triggerIds=[1106001,1106002,1106003,1106004,1106005,1106006,1106007,1106008,1106009,1106010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_12()


class CableDelay_07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__6$', arg3='3000')
            return CableDelay_07_2()


class CableDelay_08(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__7$', arg3='3000')
            return CableDelay_08_2()


class CableDelay_09(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__8$', arg3='3000')
            return CableDelay_09_2()


class CableDelay_10(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__9$', arg3='3000')
            return CableDelay_10_2()


class CableDelay_11(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__10$', arg3='3000')
            return CableDelay_11_2()


class CableDelay_12(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__11$', arg3='3000')
            return CableDelay_12_2()


class CableDelay_07_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__12$', arg3='1000')
            return CableDelay_07_3()


class CableDelay_08_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__13$', arg3='1000')
            return CableDelay_08_3()


class CableDelay_09_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__14$', arg3='1000')
            return CableDelay_09_3()


class CableDelay_10_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__15$', arg3='1000')
            return CableDelay_10_3()


class CableDelay_11_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__16$', arg3='1000')
            return CableDelay_11_3()


class CableDelay_12_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__17$', arg3='1000')
            return CableDelay_12_3()


class CableDelay_07_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__18$', arg3='1000')
            return CableDelay_07_4()


class CableDelay_08_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__19$', arg3='1000')
            return CableDelay_08_4()


class CableDelay_09_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__20$', arg3='1000')
            return CableDelay_09_4()


class CableDelay_10_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__21$', arg3='1000')
            return CableDelay_10_4()


class CableDelay_11_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__22$', arg3='1000')
            return CableDelay_11_4()


class CableDelay_12_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__23$', arg3='1000')
            return CableDelay_12_4()


class CableDelay_07_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__24$', arg3='1000')
            return CableDelay_07_5()


class CableDelay_08_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__25$', arg3='1000')
            return CableDelay_08_5()


class CableDelay_09_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__26$', arg3='1000')
            return CableDelay_09_5()


class CableDelay_10_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__27$', arg3='1000')
            return CableDelay_10_5()


class CableDelay_11_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            move_npc(spawnId=30010, patrolName='MS2PatrolData_110')
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__28$', arg3='1000')
            return CableDelay_11_5()


class CableDelay_12_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__29$', arg3='1000')
            return CableDelay_12_5()


class CableDelay_07_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__30$', duration=6000)
            move_npc(spawnId=30005, patrolName='MS2PatrolData_105')
            set_breakable(triggerIds=[1007], enabled=True)
            return CableOff_07()


class CableDelay_08_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__31$', duration=6000)
            move_npc(spawnId=30006, patrolName='MS2PatrolData_106')
            move_npc(spawnId=30007, patrolName='MS2PatrolData_107')
            set_breakable(triggerIds=[1008], enabled=True)
            return CableOff_08()


class CableDelay_09_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__32$', duration=6000)
            move_npc(spawnId=30008, patrolName='MS2PatrolData_108')
            set_breakable(triggerIds=[1009], enabled=True)
            return CableOff_09()


class CableDelay_10_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__33$', duration=6000)
            move_npc(spawnId=30009, patrolName='MS2PatrolData_109')
            set_breakable(triggerIds=[1010], enabled=True)
            return CableOff_10()


class CableDelay_11_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__34$', duration=6000)
            move_npc(spawnId=30011, patrolName='MS2PatrolData_111')
            move_npc(spawnId=30011, patrolName='MS2PatrolData_111')
            set_breakable(triggerIds=[1011], enabled=True)
            return CableOff_11()


class CableDelay_12_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__35$', duration=6000)
            move_npc(spawnId=30012, patrolName='MS2PatrolData_112')
            set_breakable(triggerIds=[1012], enabled=True)
            return CableOff_12()


class CableOff_07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=1)
            return End_02()


class CableOff_08(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=2)
            return End_02()


class CableOff_09(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=2)
            return End_02()


class CableOff_10(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=3)
            return End_02()


class CableOff_11(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=4)
            return End_02()


class CableOff_12(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900004, key='Block', value=1)
            return End_02()


class End_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


