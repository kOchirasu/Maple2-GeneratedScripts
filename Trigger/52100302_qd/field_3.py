""" trigger/52100302_qd/field_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000513], state=2)
        set_interact_object(triggerIds=[12000514], state=2)
        set_interact_object(triggerIds=[12000515], state=2)
        set_interact_object(triggerIds=[12000516], state=2)
        set_interact_object(triggerIds=[12000517], state=2)
        set_interact_object(triggerIds=[12000518], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900004, key='Block', value=0)
            return ArriveBlock_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900004, key='Block', value=0)
            return ArriveBlock_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900004, key='Block', value=0)
            return ArriveBlock_3()
        if user_value(key='Block', value=4):
            set_user_value(triggerId=900004, key='Block', value=0)
            return ArriveBlock_4()


class ArriveBlock_1(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9004]):
            return ArriveBlock_Delay_1()


class ArriveBlock_Delay_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            create_monster(spawnIds=[2004], arg2=False)
            return Block_1()
        if monster_dead(boxIds=[1110,1303,1304,1309,1310,1311,1312,1313,1314]):
            set_ai_extra_data(key='BossDie', value=2)
            set_interact_object(triggerIds=[12000513], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=106, isEnable=False)
            enable_spawn_point_pc(spawnId=108, isEnable=False)
            enable_spawn_point_pc(spawnId=109, isEnable=True)
            return CableOn_13()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1110,1303,1304,1309,1310,1311,1312,1313,1314]):
            set_ai_extra_data(key='BossDie', value=2)
            set_interact_object(triggerIds=[12000513], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=106, isEnable=False)
            enable_spawn_point_pc(spawnId=108, isEnable=False)
            enable_spawn_point_pc(spawnId=109, isEnable=True)
            return CableOn_13()


class ArriveBlock_2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9005]):
            return ArriveBlock_Delay_2()


class ArriveBlock_Delay_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            create_monster(spawnIds=[2005], arg2=False)
            return Block_2()
        if monster_dead(boxIds=[1111,1301,1302,1321,1322,1323,1324,1325,1326]):
            set_ai_extra_data(key='BossDie', value=2)
            set_interact_object(triggerIds=[12000514], state=1)
            set_interact_object(triggerIds=[12000515], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=106, isEnable=False)
            enable_spawn_point_pc(spawnId=107, isEnable=False)
            enable_spawn_point_pc(spawnId=110, isEnable=True)
            return CableOn_14_15()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1111,1301,1302,1321,1322,1323,1324,1325,1326]):
            set_ai_extra_data(key='BossDie', value=2)
            set_interact_object(triggerIds=[12000514], state=1)
            set_interact_object(triggerIds=[12000515], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=106, isEnable=False)
            enable_spawn_point_pc(spawnId=107, isEnable=False)
            enable_spawn_point_pc(spawnId=110, isEnable=True)
            return CableOn_14_15()


class ArriveBlock_3(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9006]):
            return ArriveBlock_Delay_3()


class ArriveBlock_Delay_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            create_monster(spawnIds=[2006], arg2=False)
            return Block_3()
        if monster_dead(boxIds=[1112,1307,1308,1327,1328,1329,1330,1331,1332]):
            set_ai_extra_data(key='BossDie', value=2)
            set_interact_object(triggerIds=[12000516], state=1)
            set_interact_object(triggerIds=[12000517], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=107, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=True)
            return CableOn_16_17()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1112,1307,1308,1327,1328,1329,1330,1331,1332]):
            set_ai_extra_data(key='BossDie', value=2)
            set_interact_object(triggerIds=[12000516], state=1)
            set_interact_object(triggerIds=[12000517], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=107, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=True)
            return CableOn_16_17()


class ArriveBlock_4(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9007]):
            return ArriveBlock_Delay_4()


class ArriveBlock_Delay_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            create_monster(spawnIds=[2007], arg2=False)
            return Block_4()
        if monster_dead(boxIds=[1113,1305,1306,1315,1316,1317,1318,1319,1320]):
            set_ai_extra_data(key='BossDie', value=2)
            set_interact_object(triggerIds=[12000518], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=108, isEnable=False)
            enable_spawn_point_pc(spawnId=112, isEnable=True)
            return CableOn_18()


class Block_4(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1113,1305,1306,1315,1316,1317,1318,1319,1320]):
            destroy_monster(spawnIds=[2007], arg2=False)
            set_interact_object(triggerIds=[12000518], state=1)
            create_monster(spawnIds=[1114], arg2=False)
            create_monster(spawnIds=[1115], arg2=False)
            create_monster(spawnIds=[1116], arg2=False)
            create_monster(spawnIds=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], arg2=False)
            create_monster(spawnIds=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], arg2=False)
            create_monster(spawnIds=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], arg2=False)
            enable_spawn_point_pc(spawnId=108, isEnable=False)
            enable_spawn_point_pc(spawnId=112, isEnable=True)
            return CableOn_18()


class CableOn_13(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000513], arg2=0):
            set_interact_object(triggerIds=[12000513], state=0)
            set_mesh(triggerIds=[1110001,1110002,1110003,1110004,1110005,1110006,1110007,1110008,1110009,1110010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_13()


class CableOn_14_15(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000514], arg2=0):
            set_interact_object(triggerIds=[12000514], state=0)
            set_interact_object(triggerIds=[12000515], state=0)
            set_mesh(triggerIds=[1120001,1120002,1120003,1120004,1120005,1120006,1120007,1120008,1120009,1120010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_14()
        if object_interacted(interactIds=[12000515], arg2=0):
            set_visible_breakable_object(triggerIds=[1016], arg2=False)
            set_interact_object(triggerIds=[12000514], state=0)
            set_interact_object(triggerIds=[12000515], state=0)
            set_mesh(triggerIds=[1130001,1130002,1130003,1130004,1130005,1130006,1130007,1130008,1130009,1130010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_15()


class CableOn_16_17(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000516], arg2=0):
            set_interact_object(triggerIds=[12000516], state=0)
            set_interact_object(triggerIds=[12000517], state=0)
            set_mesh(triggerIds=[1140001,1140002,1140003,1140004,1140005,1140006,1140007,1140008,1140009,1140010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_16()
        if object_interacted(interactIds=[12000517], arg2=0):
            set_interact_object(triggerIds=[12000516], state=0)
            set_interact_object(triggerIds=[12000517], state=0)
            set_mesh(triggerIds=[1150001,1150002,1150003,1150004,1150005,1150006,1150007,1150008,1150009,1150010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_17()


class CableOn_18(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000518], arg2=0):
            set_interact_object(triggerIds=[12000518], state=0)
            set_mesh(triggerIds=[1160001,1160002,1160003,1160004,1160005,1160006,1160007,1160008,1160009,1160010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_18()


class CableDelay_13(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__0$', arg3='3000')
            return CableDelay_13_2()


class CableDelay_14(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__1$', arg3='3000')
            return CableDelay_14_2()


class CableDelay_15(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__2$', arg3='3000')
            return CableDelay_15_2()


class CableDelay_16(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__3$', arg3='3000')
            return CableDelay_16_2()


class CableDelay_17(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__4$', arg3='3000')
            return CableDelay_17_2()


class CableDelay_18(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__5$', arg3='3000')
            return CableDelay_18_2()


class CableDelay_13_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__6$', arg3='1000')
            return CableDelay_13_3()


class CableDelay_14_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__7$', arg3='1000')
            return CableDelay_14_3()


class CableDelay_15_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__8$', arg3='1000')
            return CableDelay_15_3()


class CableDelay_16_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__9$', arg3='1000')
            return CableDelay_16_3()


class CableDelay_17_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__10$', arg3='1000')
            return CableDelay_17_3()


class CableDelay_18_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__11$', arg3='1000')
            return CableDelay_18_3()


class CableDelay_13_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__12$', arg3='1000')
            return CableDelay_13_4()


class CableDelay_14_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__13$', arg3='1000')
            return CableDelay_14_4()


class CableDelay_15_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__14$', arg3='1000')
            return CableDelay_15_4()


class CableDelay_16_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__15$', arg3='1000')
            return CableDelay_16_4()


class CableDelay_17_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__16$', arg3='1000')
            return CableDelay_17_4()


class CableDelay_18_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__17$', arg3='1000')
            return CableDelay_18_4()


class CableDelay_13_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__18$', arg3='1000')
            return CableDelay_13_5()


class CableDelay_14_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__19$', arg3='1000')
            return CableDelay_14_5()


class CableDelay_15_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__20$', arg3='1000')
            return CableDelay_15_5()


class CableDelay_16_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__21$', arg3='1000')
            return CableDelay_16_5()


class CableDelay_17_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__22$', arg3='1000')
            return CableDelay_17_5()


class CableDelay_18_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_3__23$', arg3='1000')
            return CableDelay_18_5()


class CableDelay_13_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1013], enabled=True)
            return CableOff_13()


class CableDelay_14_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1014], enabled=True)
            return CableOff_14()


class CableDelay_15_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1015], enabled=True)
            return CableOff_15()


class CableDelay_16_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1016], enabled=True)
            return CableOff_16()


class CableDelay_17_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1017], enabled=True)
            return CableOff_17()


class CableDelay_18_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1018], enabled=True)
            return CableOff_18()


class CableOff_13(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=1)
            return End_03()


class CableOff_14(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=1)
            return End_03()


class CableOff_15(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=2)
            return End_03()


class CableOff_16(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=1)
            return End_03()


class CableOff_17(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=2)
            return End_03()


class CableOff_18(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900005, key='Block', value=3)
            return End_03()


class End_03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


