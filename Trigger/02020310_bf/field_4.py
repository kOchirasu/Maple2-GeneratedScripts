""" trigger/02020310_bf/field_4.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000319], state=2)
        self.set_interact_object(triggerIds=[12000320], state=2)
        self.set_interact_object(triggerIds=[12000321], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900005, key='Block', value=0)
            return ArriveBlock_1(self.ctx)
        if self.user_value(key='Block', value=2):
            self.set_user_value(triggerId=900005, key='Block', value=0)
            return ArriveBlock_2(self.ctx)
        if self.user_value(key='Block', value=3):
            self.set_user_value(triggerId=900005, key='Block', value=0)
            return ArriveBlock_3(self.ctx)


class ArriveBlock_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9008]):
            self.create_monster(spawnIds=[2008], animationEffect=False)
            return ArriveBlock_Delay_1(self.ctx)


class ArriveBlock_Delay_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Block_1_01(self.ctx)
        if self.monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000007], arg2=False)
            self.destroy_monster(spawnIds=[1000008], arg2=False)
            self.set_interact_object(triggerIds=[12000319], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=109, isEnable=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19(self.ctx)


class Block_1_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5167):
            self.create_monster(spawnIds=[1000007], animationEffect=False)
            return Block_1_02(self.ctx)
        if self.monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000007], arg2=False)
            self.destroy_monster(spawnIds=[1000008], arg2=False)
            self.set_interact_object(triggerIds=[12000319], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=109, isEnable=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19(self.ctx)


class Block_1_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4067):
            self.create_monster(spawnIds=[1000008], animationEffect=False)
            return Block_1(self.ctx)
        if self.monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000007], arg2=False)
            self.destroy_monster(spawnIds=[1000008], arg2=False)
            self.set_interact_object(triggerIds=[12000319], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=109, isEnable=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19(self.ctx)


class Block_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000007], arg2=False)
            self.destroy_monster(spawnIds=[1000008], arg2=False)
            self.set_interact_object(triggerIds=[12000319], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=109, isEnable=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=113, isEnable=True)
            return CableOn_19(self.ctx)


class ArriveBlock_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9009]):
            self.create_monster(spawnIds=[2009], animationEffect=False)
            return ArriveBlock_Delay_2(self.ctx)


class ArriveBlock_Delay_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Block_2_01(self.ctx)
        if self.monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000009], arg2=False)
            self.destroy_monster(spawnIds=[1000010], arg2=False)
            self.set_interact_object(triggerIds=[12000320], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20(self.ctx)


class Block_2_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5167):
            self.create_monster(spawnIds=[1000009], animationEffect=False)
            return Block_2_02(self.ctx)
        if self.monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000009], arg2=False)
            self.destroy_monster(spawnIds=[1000010], arg2=False)
            self.set_interact_object(triggerIds=[12000320], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20(self.ctx)


class Block_2_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4067):
            self.create_monster(spawnIds=[1000010], animationEffect=False)
            return Block_2(self.ctx)
        if self.monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000009], arg2=False)
            self.destroy_monster(spawnIds=[1000010], arg2=False)
            self.set_interact_object(triggerIds=[12000320], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20(self.ctx)


class Block_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000009], arg2=False)
            self.destroy_monster(spawnIds=[1000010], arg2=False)
            self.set_interact_object(triggerIds=[12000320], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=110, isEnable=False)
            self.enable_spawn_point_pc(spawnId=111, isEnable=False)
            self.enable_spawn_point_pc(spawnId=114, isEnable=True)
            return CableOn_20(self.ctx)


class ArriveBlock_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9010]):
            self.create_monster(spawnIds=[2010], animationEffect=False)
            return ArriveBlock_Delay_3(self.ctx)


class ArriveBlock_Delay_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Block_3_01(self.ctx)
        if self.monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000011], arg2=False)
            self.destroy_monster(spawnIds=[1000012], arg2=False)
            self.set_interact_object(triggerIds=[12000321], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=112, isEnable=False)
            self.enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21(self.ctx)


class Block_3_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5167):
            self.create_monster(spawnIds=[1000011], animationEffect=False)
            return Block_3_02(self.ctx)
        if self.monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000011], arg2=False)
            self.destroy_monster(spawnIds=[1000012], arg2=False)
            self.set_interact_object(triggerIds=[12000321], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=112, isEnable=False)
            self.enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21(self.ctx)


class Block_3_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4067):
            self.create_monster(spawnIds=[1000012], animationEffect=False)
            return Block_3(self.ctx)
        if self.monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000011], arg2=False)
            self.destroy_monster(spawnIds=[1000012], arg2=False)
            self.set_interact_object(triggerIds=[12000321], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=112, isEnable=False)
            self.enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21(self.ctx)


class Block_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000011], arg2=False)
            self.destroy_monster(spawnIds=[1000012], arg2=False)
            self.set_interact_object(triggerIds=[12000321], state=1)
            self.create_monster(spawnIds=[1117], animationEffect=False)
            self.create_monster(spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], animationEffect=False)
            self.create_monster(spawnIds=[1511,1512,1513], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=112, isEnable=False)
            self.enable_spawn_point_pc(spawnId=115, isEnable=True)
            return CableOn_21(self.ctx)


class CableOn_19(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000319], stateValue=0):
            self.set_interact_object(triggerIds=[12000319], state=0)
            self.set_mesh(triggerIds=[1210001,1210002,1210003,1210004,1210005,1210006,1210007,1210008,1210009,1210010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_19(self.ctx)


class CableOn_20(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000320], stateValue=0):
            self.set_interact_object(triggerIds=[12000320], state=0)
            self.set_mesh(triggerIds=[1310001,1310002,1310003,1310004,1310005,1310006,1310007,1310008,1310009,1310010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_20(self.ctx)


class CableOn_21(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000321], stateValue=0):
            self.set_interact_object(triggerIds=[12000321], state=0)
            self.set_mesh(triggerIds=[1410001,1410002,1410003,1410004,1410005,1410006,1410007,1410008,1410009,1410010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_21(self.ctx)


class CableDelay_19(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__0$', arg3='3000')
            return CableDelay_19_2(self.ctx)


class CableDelay_20(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__1$', arg3='3000')
            return CableDelay_20_2(self.ctx)


class CableDelay_21(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__2$', arg3='3000')
            return CableDelay_21_2(self.ctx)


class CableDelay_19_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__3$', arg3='1000')
            return CableDelay_19_3(self.ctx)


class CableDelay_20_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__4$', arg3='1000')
            return CableDelay_20_3(self.ctx)


class CableDelay_21_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__5$', arg3='1000')
            return CableDelay_21_3(self.ctx)


class CableDelay_19_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__6$', arg3='1000')
            return CableDelay_19_4(self.ctx)


class CableDelay_20_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__7$', arg3='1000')
            return CableDelay_20_4(self.ctx)


class CableDelay_21_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__8$', arg3='1000')
            return CableDelay_21_4(self.ctx)


class CableDelay_19_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__9$', arg3='1000')
            return CableDelay_19_5(self.ctx)


class CableDelay_20_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__10$', arg3='1000')
            return CableDelay_20_5(self.ctx)


class CableDelay_21_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_4__11$', arg3='1000')
            return CableDelay_21_5(self.ctx)


class CableDelay_19_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_4__12$', duration=5000)
            self.set_breakable(triggerIds=[1019], enable=True)
            return CableOff_19(self.ctx)


class CableDelay_20_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_4__13$', duration=5000)
            self.set_breakable(triggerIds=[1020], enable=True)
            return CableOff_20(self.ctx)


class CableDelay_21_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_4__14$', duration=5000)
            self.set_breakable(triggerIds=[1021], enable=True)
            return CableOff_21(self.ctx)


class CableOff_19(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900006, key='Block', value=1)
            return End_04(self.ctx)


class CableOff_20(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900006, key='Block', value=1)
            return End_04(self.ctx)


class CableOff_21(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900006, key='Block', value=1)
            return End_04(self.ctx)


class End_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


initial_state = 대기
