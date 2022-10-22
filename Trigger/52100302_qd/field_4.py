""" trigger/52100302_qd/field_4.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000519], state=2)
        set_interact_object(triggerIds=[12000520], state=2)
        set_interact_object(triggerIds=[12000521], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900005, key='Block', value=0)
            return ArriveBlock_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900005, key='Block', value=0)
            return ArriveBlock_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900005, key='Block', value=0)
            return ArriveBlock_3()


class ArriveBlock_1(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9008]):
            create_monster(spawnIds=[2008], arg2=False)
            return ArriveBlock_Delay_1()


class ArriveBlock_Delay_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Block_1_01()
        if monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000007], arg2=False)
            destroy_monster(spawnIds=[1000008], arg2=False)
            set_interact_object(triggerIds=[12000519], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=109, isEnable=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19()


class Block_1_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5167):
            create_monster(spawnIds=[1000007], arg2=False)
            return Block_1_02()
        if monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000007], arg2=False)
            destroy_monster(spawnIds=[1000008], arg2=False)
            set_interact_object(triggerIds=[12000519], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=109, isEnable=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19()


class Block_1_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4067):
            create_monster(spawnIds=[1000008], arg2=False)
            return Block_1()
        if monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000007], arg2=False)
            destroy_monster(spawnIds=[1000008], arg2=False)
            set_interact_object(triggerIds=[12000519], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=109, isEnable=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000007], arg2=False)
            destroy_monster(spawnIds=[1000008], arg2=False)
            set_interact_object(triggerIds=[12000519], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=109, isEnable=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19()


class ArriveBlock_2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9009]):
            create_monster(spawnIds=[2009], arg2=False)
            return ArriveBlock_Delay_2()


class ArriveBlock_Delay_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Block_2_01()
        if monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000009], arg2=False)
            destroy_monster(spawnIds=[1000010], arg2=False)
            set_interact_object(triggerIds=[12000520], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20()


class Block_2_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5167):
            create_monster(spawnIds=[1000009], arg2=False)
            return Block_2_02()
        if monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000009], arg2=False)
            destroy_monster(spawnIds=[1000010], arg2=False)
            set_interact_object(triggerIds=[12000520], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20()


class Block_2_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4067):
            create_monster(spawnIds=[1000010], arg2=False)
            return Block_2()
        if monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000009], arg2=False)
            destroy_monster(spawnIds=[1000010], arg2=False)
            set_interact_object(triggerIds=[12000520], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000009], arg2=False)
            destroy_monster(spawnIds=[1000010], arg2=False)
            set_interact_object(triggerIds=[12000520], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=110, isEnable=False)
            enable_spawn_point_pc(spawnId=111, isEnable=False)
            enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20()


class ArriveBlock_3(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9010]):
            create_monster(spawnIds=[2010], arg2=False)
            return ArriveBlock_Delay_3()


class ArriveBlock_Delay_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Block_3_01()
        if monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000011], arg2=False)
            destroy_monster(spawnIds=[1000012], arg2=False)
            set_interact_object(triggerIds=[12000521], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=112, isEnable=False)
            enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21()


class Block_3_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5167):
            create_monster(spawnIds=[1000011], arg2=False)
            return Block_3_02()
        if monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000011], arg2=False)
            destroy_monster(spawnIds=[1000012], arg2=False)
            set_interact_object(triggerIds=[12000521], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=112, isEnable=False)
            enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21()


class Block_3_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4067):
            create_monster(spawnIds=[1000012], arg2=False)
            return Block_3()
        if monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000011], arg2=False)
            destroy_monster(spawnIds=[1000012], arg2=False)
            set_interact_object(triggerIds=[12000521], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=112, isEnable=False)
            enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            set_ai_extra_data(key='BossDie', value=2)
            destroy_monster(spawnIds=[1000011], arg2=False)
            destroy_monster(spawnIds=[1000012], arg2=False)
            set_interact_object(triggerIds=[12000521], state=1)
            create_monster(spawnIds=[1117], arg2=False)
            create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], arg2=False)
            create_monster(spawnIds=[1511,1512,1513], arg2=False)
            enable_spawn_point_pc(spawnId=112, isEnable=False)
            enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21()


class CableOn_19(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000519], arg2=0):
            set_interact_object(triggerIds=[12000519], state=0)
            set_mesh(triggerIds=[1210001,1210002,1210003,1210004,1210005,1210006,1210007,1210008,1210009,1210010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_19()


class CableOn_20(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000520], arg2=0):
            set_interact_object(triggerIds=[12000520], state=0)
            set_mesh(triggerIds=[1310001,1310002,1310003,1310004,1310005,1310006,1310007,1310008,1310009,1310010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_20()


class CableOn_21(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000521], arg2=0):
            set_interact_object(triggerIds=[12000521], state=0)
            set_mesh(triggerIds=[1410001,1410002,1410003,1410004,1410005,1410006,1410007,1410008,1410009,1410010], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_21()


class CableDelay_19(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__0$', arg3='3000')
            return CableDelay_19_2()


class CableDelay_20(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__1$', arg3='3000')
            return CableDelay_20_2()


class CableDelay_21(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__2$', arg3='3000')
            return CableDelay_21_2()


class CableDelay_19_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__3$', arg3='1000')
            return CableDelay_19_3()


class CableDelay_20_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__4$', arg3='1000')
            return CableDelay_20_3()


class CableDelay_21_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__5$', arg3='1000')
            return CableDelay_21_3()


class CableDelay_19_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__6$', arg3='1000')
            return CableDelay_19_4()


class CableDelay_20_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__7$', arg3='1000')
            return CableDelay_20_4()


class CableDelay_21_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__8$', arg3='1000')
            return CableDelay_21_4()


class CableDelay_19_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__9$', arg3='1000')
            return CableDelay_19_5()


class CableDelay_20_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__10$', arg3='1000')
            return CableDelay_20_5()


class CableDelay_21_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_4__11$', arg3='1000')
            return CableDelay_21_5()


class CableDelay_19_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_4__12$', duration=5000)
            set_breakable(triggerIds=[1019], enabled=True)
            return CableOff_19()


class CableDelay_20_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_4__13$', duration=5000)
            set_breakable(triggerIds=[1020], enabled=True)
            return CableOff_20()


class CableDelay_21_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_4__14$', duration=5000)
            set_breakable(triggerIds=[1021], enabled=True)
            return CableOff_21()


class CableOff_19(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900006, key='Block', value=1)
            return End_04()


class CableOff_20(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900006, key='Block', value=1)
            return End_04()


class CableOff_21(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900006, key='Block', value=1)
            return End_04()


class End_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


