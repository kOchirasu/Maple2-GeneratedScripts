""" trigger/02020310_bf/field_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000313], state=2)
        self.set_interact_object(trigger_ids=[12000314], state=2)
        self.set_interact_object(trigger_ids=[12000315], state=2)
        self.set_interact_object(trigger_ids=[12000316], state=2)
        self.set_interact_object(trigger_ids=[12000317], state=2)
        self.set_interact_object(trigger_ids=[12000318], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], visible=False)
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], visible=False)
        # self.set_visible_breakable_object(trigger_ids=[1021,1022], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') >= 1:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return ArriveBlock_1(self.ctx)
        if self.user_value(key='Block') >= 2:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return ArriveBlock_2(self.ctx)
        if self.user_value(key='Block') >= 3:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return ArriveBlock_3(self.ctx)
        if self.user_value(key='Block') >= 4:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return ArriveBlock_4(self.ctx)


class ArriveBlock_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9004]):
            return ArriveBlock_Delay_1(self.ctx)


class ArriveBlock_Delay_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.spawn_monster(spawn_ids=[2004], auto_target=False)
            return Block_1(self.ctx)
        if self.monster_dead(spawn_ids=[1110,1303,1304,1309,1310,1311,1312,1313,1314]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000313], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=109, is_enable=True)
            return CableOn_13(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1110,1303,1304,1309,1310,1311,1312,1313,1314]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000313], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=109, is_enable=True)
            return CableOn_13(self.ctx)


class ArriveBlock_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9005]):
            return ArriveBlock_Delay_2(self.ctx)


class ArriveBlock_Delay_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.spawn_monster(spawn_ids=[2005], auto_target=False)
            return Block_2(self.ctx)
        if self.monster_dead(spawn_ids=[1111,1301,1302,1321,1322,1323,1324,1325,1326]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000314], state=1)
            self.set_interact_object(trigger_ids=[12000315], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=110, is_enable=True)
            return CableOn_14_15(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1111,1301,1302,1321,1322,1323,1324,1325,1326]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000314], state=1)
            self.set_interact_object(trigger_ids=[12000315], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=110, is_enable=True)
            return CableOn_14_15(self.ctx)


class ArriveBlock_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9006]):
            return ArriveBlock_Delay_3(self.ctx)


class ArriveBlock_Delay_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.spawn_monster(spawn_ids=[2006], auto_target=False)
            return Block_3(self.ctx)
        if self.monster_dead(spawn_ids=[1112,1307,1308,1327,1328,1329,1330,1331,1332]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000316], state=1)
            self.set_interact_object(trigger_ids=[12000317], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=111, is_enable=True)
            return CableOn_16_17(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1112,1307,1308,1327,1328,1329,1330,1331,1332]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000316], state=1)
            self.set_interact_object(trigger_ids=[12000317], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=111, is_enable=True)
            return CableOn_16_17(self.ctx)


class ArriveBlock_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9007]):
            return ArriveBlock_Delay_4(self.ctx)


class ArriveBlock_Delay_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.spawn_monster(spawn_ids=[2007], auto_target=False)
            return Block_4(self.ctx)
        if self.monster_dead(spawn_ids=[1113,1305,1306,1315,1316,1317,1318,1319,1320]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000318], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=112, is_enable=True)
            return CableOn_18(self.ctx)


class Block_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1113,1305,1306,1315,1316,1317,1318,1319,1320]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.set_interact_object(trigger_ids=[12000318], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410], auto_target=False)
            self.spawn_monster(spawn_ids=[1411,1412,1413,1414,1415,1416,1417,1418,1419,1420], auto_target=False)
            self.spawn_monster(spawn_ids=[1421,1422,1423,1424,1425,1426,1427,1428,1429,1430], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=False)
            self.enable_spawn_point_pc(spawn_id=112, is_enable=True)
            return CableOn_18(self.ctx)


class CableOn_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000313], state=0):
            self.set_interact_object(trigger_ids=[12000313], state=0)
            self.set_mesh(trigger_ids=[1110001,1110002,1110003,1110004,1110005,1110006,1110007,1110008,1110009,1110010], visible=False, start_delay=0, interval=0, fade=0)
            return CableDelay_13(self.ctx)


class CableOn_14_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000314], state=0):
            self.set_interact_object(trigger_ids=[12000314], state=0)
            self.set_interact_object(trigger_ids=[12000315], state=0)
            self.set_mesh(trigger_ids=[1120001,1120002,1120003,1120004,1120005,1120006,1120007,1120008,1120009,1120010], visible=False, start_delay=0, interval=0, fade=0)
            return CableDelay_14(self.ctx)
        if self.object_interacted(interact_ids=[12000315], state=0):
            self.set_visible_breakable_object(trigger_ids=[1016], visible=False)
            self.set_interact_object(trigger_ids=[12000314], state=0)
            self.set_interact_object(trigger_ids=[12000315], state=0)
            self.set_mesh(trigger_ids=[1130001,1130002,1130003,1130004,1130005,1130006,1130007,1130008,1130009,1130010], visible=False, start_delay=0, interval=0, fade=0)
            return CableDelay_15(self.ctx)


class CableOn_16_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000316], state=0):
            self.set_interact_object(trigger_ids=[12000316], state=0)
            self.set_interact_object(trigger_ids=[12000317], state=0)
            self.set_mesh(trigger_ids=[1140001,1140002,1140003,1140004,1140005,1140006,1140007,1140008,1140009,1140010], visible=False, start_delay=0, interval=0, fade=0)
            return CableDelay_16(self.ctx)
        if self.object_interacted(interact_ids=[12000317], state=0):
            self.set_interact_object(trigger_ids=[12000316], state=0)
            self.set_interact_object(trigger_ids=[12000317], state=0)
            self.set_mesh(trigger_ids=[1150001,1150002,1150003,1150004,1150005,1150006,1150007,1150008,1150009,1150010], visible=False, start_delay=0, interval=0, fade=0)
            return CableDelay_17(self.ctx)


class CableOn_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000318], state=0):
            self.set_interact_object(trigger_ids=[12000318], state=0)
            self.set_mesh(trigger_ids=[1160001,1160002,1160003,1160004,1160005,1160006,1160007,1160008,1160009,1160010], visible=False, start_delay=0, interval=0, fade=0)
            return CableDelay_18(self.ctx)


class CableDelay_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__0$', arg3='3000')
            return CableDelay_13_2(self.ctx)


class CableDelay_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__1$', arg3='3000')
            return CableDelay_14_2(self.ctx)


class CableDelay_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__2$', arg3='3000')
            return CableDelay_15_2(self.ctx)


class CableDelay_16(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__3$', arg3='3000')
            return CableDelay_16_2(self.ctx)


class CableDelay_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__4$', arg3='3000')
            return CableDelay_17_2(self.ctx)


class CableDelay_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__5$', arg3='3000')
            return CableDelay_18_2(self.ctx)


class CableDelay_13_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__6$', arg3='1000')
            return CableDelay_13_3(self.ctx)


class CableDelay_14_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__7$', arg3='1000')
            return CableDelay_14_3(self.ctx)


class CableDelay_15_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__8$', arg3='1000')
            return CableDelay_15_3(self.ctx)


class CableDelay_16_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__9$', arg3='1000')
            return CableDelay_16_3(self.ctx)


class CableDelay_17_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__10$', arg3='1000')
            return CableDelay_17_3(self.ctx)


class CableDelay_18_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__11$', arg3='1000')
            return CableDelay_18_3(self.ctx)


class CableDelay_13_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__12$', arg3='1000')
            return CableDelay_13_4(self.ctx)


class CableDelay_14_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__13$', arg3='1000')
            return CableDelay_14_4(self.ctx)


class CableDelay_15_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__14$', arg3='1000')
            return CableDelay_15_4(self.ctx)


class CableDelay_16_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__15$', arg3='1000')
            return CableDelay_16_4(self.ctx)


class CableDelay_17_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__16$', arg3='1000')
            return CableDelay_17_4(self.ctx)


class CableDelay_18_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__17$', arg3='1000')
            return CableDelay_18_4(self.ctx)


class CableDelay_13_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__18$', arg3='1000')
            return CableDelay_13_5(self.ctx)


class CableDelay_14_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__19$', arg3='1000')
            return CableDelay_14_5(self.ctx)


class CableDelay_15_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__20$', arg3='1000')
            return CableDelay_15_5(self.ctx)


class CableDelay_16_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__21$', arg3='1000')
            return CableDelay_16_5(self.ctx)


class CableDelay_17_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__22$', arg3='1000')
            return CableDelay_17_5(self.ctx)


class CableDelay_18_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_3__23$', arg3='1000')
            return CableDelay_18_5(self.ctx)


class CableDelay_13_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1013], enable=True)
            return CableOff_13(self.ctx)


class CableDelay_14_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1014], enable=True)
            return CableOff_14(self.ctx)


class CableDelay_15_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1015], enable=True)
            return CableOff_15(self.ctx)


class CableDelay_16_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1016], enable=True)
            return CableOff_16(self.ctx)


class CableDelay_17_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1017], enable=True)
            return CableOff_17(self.ctx)


class CableDelay_18_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1018], enable=True)
            return CableOff_18(self.ctx)


class CableOff_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900005, key='Block', value=2)
            return End_03(self.ctx)


class CableOff_16(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900005, key='Block', value=2)
            return End_03(self.ctx)


class CableOff_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900005, key='Block', value=3)
            return End_03(self.ctx)


class End_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)


initial_state = 대기
