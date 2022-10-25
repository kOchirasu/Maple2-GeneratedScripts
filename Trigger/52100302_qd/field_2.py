""" trigger/52100302_qd/field_2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000507], state=2)
        self.set_interact_object(triggerIds=[12000508], state=2)
        self.set_interact_object(triggerIds=[12000509], state=2)
        self.set_interact_object(triggerIds=[12000510], state=2)
        self.set_interact_object(triggerIds=[12000511], state=2)
        self.set_interact_object(triggerIds=[12000512], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900003, key='Block', value=0)
            return ArriveBlock_1(self.ctx)
        if self.user_value(key='Block', value=2):
            self.set_user_value(triggerId=900003, key='Block', value=0)
            return ArriveBlock_2(self.ctx)
        if self.user_value(key='Block', value=3):
            self.set_user_value(triggerId=900003, key='Block', value=0)
            return ArriveBlock_3(self.ctx)


class ArriveBlock_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            self.create_monster(spawnIds=[2001], animationEffect=False)
            return ArriveBlock_Delay_1(self.ctx)


class ArriveBlock_Delay_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__0$', duration=3000)
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__1$', duration=4000)
            return Block_1_01(self.ctx)
        if self.monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000001], arg2=False)
            self.destroy_monster(spawnIds=[1000002], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000507], state=1)
            self.set_interact_object(triggerIds=[12000508], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=103, isEnable=False)
            self.enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08(self.ctx)


class Block_1_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5167):
            self.create_monster(spawnIds=[1000001], animationEffect=False)
            return Block_1_02(self.ctx)
        if self.monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000001], arg2=False)
            self.destroy_monster(spawnIds=[1000002], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000507], state=1)
            self.set_interact_object(triggerIds=[12000508], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=103, isEnable=False)
            self.enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08(self.ctx)


class Block_1_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4067):
            self.create_monster(spawnIds=[1000002], animationEffect=False)
            return Block_1(self.ctx)
        if self.monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000001], arg2=False)
            self.destroy_monster(spawnIds=[1000002], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000507], state=1)
            self.set_interact_object(triggerIds=[12000508], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=103, isEnable=False)
            self.enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08(self.ctx)


class Block_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000001], arg2=False)
            self.destroy_monster(spawnIds=[1000002], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000507], state=1)
            self.set_interact_object(triggerIds=[12000508], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=103, isEnable=False)
            self.enable_spawn_point_pc(spawnId=106, isEnable=True)
            return CableOn_07_08(self.ctx)


class ArriveBlock_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9002]):
            self.create_monster(spawnIds=[2002], animationEffect=False)
            return ArriveBlock_Delay_2(self.ctx)


class ArriveBlock_Delay_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__2$', duration=3000)
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__3$', duration=4000)
            return Block_2_01(self.ctx)
        if self.monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000003], arg2=False)
            self.destroy_monster(spawnIds=[1000004], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000509], state=1)
            self.set_interact_object(triggerIds=[12000510], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=104, isEnable=False)
            self.enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10(self.ctx)


class Block_2_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5167):
            self.create_monster(spawnIds=[1000003], animationEffect=False)
            return Block_2_02(self.ctx)
        if self.monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000003], arg2=False)
            self.destroy_monster(spawnIds=[1000004], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000509], state=1)
            self.set_interact_object(triggerIds=[12000510], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=104, isEnable=False)
            self.enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10(self.ctx)


class Block_2_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4067):
            self.create_monster(spawnIds=[1000004], animationEffect=False)
            return Block_2(self.ctx)
        if self.monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000003], arg2=False)
            self.destroy_monster(spawnIds=[1000004], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000509], state=1)
            self.set_interact_object(triggerIds=[12000510], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=104, isEnable=False)
            self.enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10(self.ctx)


class Block_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000003], arg2=False)
            self.destroy_monster(spawnIds=[1000004], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000509], state=1)
            self.set_interact_object(triggerIds=[12000510], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=104, isEnable=False)
            self.enable_spawn_point_pc(spawnId=107, isEnable=True)
            return CableOn_09_10(self.ctx)


class ArriveBlock_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9003]):
            self.create_monster(spawnIds=[2003], animationEffect=False)
            return ArriveBlock_Delay_3(self.ctx)


class ArriveBlock_Delay_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__4$', duration=3000)
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_2__5$', duration=4000)
            return Block_3_01(self.ctx)
        if self.monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000005], arg2=False)
            self.destroy_monster(spawnIds=[1000006], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000511], state=1)
            self.set_interact_object(triggerIds=[12000512], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=105, isEnable=False)
            self.enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12(self.ctx)


class Block_3_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5167):
            self.create_monster(spawnIds=[1000005], animationEffect=False)
            return Block_3_02(self.ctx)
        if self.monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000005], arg2=False)
            self.destroy_monster(spawnIds=[1000006], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000511], state=1)
            self.set_interact_object(triggerIds=[12000512], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=105, isEnable=False)
            self.enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12(self.ctx)


class Block_3_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4067):
            self.create_monster(spawnIds=[1000006], animationEffect=False)
            return Block_3(self.ctx)
        if self.monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000005], arg2=False)
            self.destroy_monster(spawnIds=[1000006], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000511], state=1)
            self.set_interact_object(triggerIds=[12000512], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=105, isEnable=False)
            self.enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12(self.ctx)


class Block_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawnIds=[1000005], arg2=False)
            self.destroy_monster(spawnIds=[1000006], arg2=False)
            self.destroy_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(triggerIds=[12000511], state=1)
            self.set_interact_object(triggerIds=[12000512], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            self.create_monster(spawnIds=[1301,1302,1304,1305,1306,1307,1308,1309,1310], animationEffect=False)
            self.create_monster(spawnIds=[1311,1312,1314,1315,1316,1317,1318,1319,1320], animationEffect=False)
            self.create_monster(spawnIds=[1321,1322,1324,1325,1326,1327,1328,1329,1330], animationEffect=False)
            self.create_monster(spawnIds=[1331,1332], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=105, isEnable=False)
            self.enable_spawn_point_pc(spawnId=108, isEnable=True)
            return CableOn_11_12(self.ctx)


class CableOn_07_08(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000507], stateValue=0):
            self.set_interact_object(triggerIds=[12000507], state=0)
            self.set_interact_object(triggerIds=[12000508], state=0)
            self.create_monster(spawnIds=[30005], animationEffect=False)
            self.set_mesh(triggerIds=[1101001,1101002,1101003,1101004,1101005,1101006,1101007,1101008,1101009,1101010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_07(self.ctx)
        if self.object_interacted(interactIds=[12000508], stateValue=0):
            self.set_interact_object(triggerIds=[12000507], state=0)
            self.set_interact_object(triggerIds=[12000508], state=0)
            self.create_monster(spawnIds=[30006,30007], animationEffect=False)
            self.set_mesh(triggerIds=[1102001,1102002,1102003,1102004,1102005,1102006,1102007,1102008,1102009,1102010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_08(self.ctx)


class CableOn_09_10(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000509], stateValue=0):
            self.set_interact_object(triggerIds=[12000509], state=0)
            self.set_interact_object(triggerIds=[12000510], state=0)
            self.create_monster(spawnIds=[30008], animationEffect=False)
            self.set_mesh(triggerIds=[1103001,1103002,1103003,1103004,1103005,1103006,1103007,1103008,1103009,1103010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_09(self.ctx)
        if self.object_interacted(interactIds=[12000510], stateValue=0):
            self.set_interact_object(triggerIds=[12000509], state=0)
            self.set_interact_object(triggerIds=[12000510], state=0)
            self.create_monster(spawnIds=[30009], animationEffect=False)
            self.set_mesh(triggerIds=[1104001,1104002,1104003,1104004,1104005,1104006,1104007,1104008,1104009,1104010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_10(self.ctx)


class CableOn_11_12(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000511], stateValue=0):
            self.set_interact_object(triggerIds=[12000511], state=0)
            self.set_interact_object(triggerIds=[12000512], state=0)
            self.create_monster(spawnIds=[30010,30011], animationEffect=False)
            self.set_mesh(triggerIds=[1105001,1105002,1105003,1105004,1105005,1105006,1105007,1105008,1105009,1105010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_11(self.ctx)
        if self.object_interacted(interactIds=[12000512], stateValue=0):
            self.set_interact_object(triggerIds=[12000511], state=0)
            self.set_interact_object(triggerIds=[12000512], state=0)
            self.create_monster(spawnIds=[30012], animationEffect=False)
            self.set_mesh(triggerIds=[1106001,1106002,1106003,1106004,1106005,1106006,1106007,1106008,1106009,1106010], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_12(self.ctx)


class CableDelay_07(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__6$', arg3='3000')
            return CableDelay_07_2(self.ctx)


class CableDelay_08(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__7$', arg3='3000')
            return CableDelay_08_2(self.ctx)


class CableDelay_09(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__8$', arg3='3000')
            return CableDelay_09_2(self.ctx)


class CableDelay_10(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__9$', arg3='3000')
            return CableDelay_10_2(self.ctx)


class CableDelay_11(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__10$', arg3='3000')
            return CableDelay_11_2(self.ctx)


class CableDelay_12(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__11$', arg3='3000')
            return CableDelay_12_2(self.ctx)


class CableDelay_07_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__12$', arg3='1000')
            return CableDelay_07_3(self.ctx)


class CableDelay_08_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__13$', arg3='1000')
            return CableDelay_08_3(self.ctx)


class CableDelay_09_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__14$', arg3='1000')
            return CableDelay_09_3(self.ctx)


class CableDelay_10_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__15$', arg3='1000')
            return CableDelay_10_3(self.ctx)


class CableDelay_11_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__16$', arg3='1000')
            return CableDelay_11_3(self.ctx)


class CableDelay_12_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__17$', arg3='1000')
            return CableDelay_12_3(self.ctx)


class CableDelay_07_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__18$', arg3='1000')
            return CableDelay_07_4(self.ctx)


class CableDelay_08_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__19$', arg3='1000')
            return CableDelay_08_4(self.ctx)


class CableDelay_09_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__20$', arg3='1000')
            return CableDelay_09_4(self.ctx)


class CableDelay_10_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__21$', arg3='1000')
            return CableDelay_10_4(self.ctx)


class CableDelay_11_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__22$', arg3='1000')
            return CableDelay_11_4(self.ctx)


class CableDelay_12_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__23$', arg3='1000')
            return CableDelay_12_4(self.ctx)


class CableDelay_07_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__24$', arg3='1000')
            return CableDelay_07_5(self.ctx)


class CableDelay_08_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__25$', arg3='1000')
            return CableDelay_08_5(self.ctx)


class CableDelay_09_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__26$', arg3='1000')
            return CableDelay_09_5(self.ctx)


class CableDelay_10_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__27$', arg3='1000')
            return CableDelay_10_5(self.ctx)


class CableDelay_11_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.move_npc(spawnId=30010, patrolName='MS2PatrolData_110')
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__28$', arg3='1000')
            return CableDelay_11_5(self.ctx)


class CableDelay_12_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$52100302_QD__FIELD_2__29$', arg3='1000')
            return CableDelay_12_5(self.ctx)


class CableDelay_07_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__30$', duration=6000)
            self.move_npc(spawnId=30005, patrolName='MS2PatrolData_105')
            self.set_breakable(triggerIds=[1007], enable=True)
            return CableOff_07(self.ctx)


class CableDelay_08_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__31$', duration=6000)
            self.move_npc(spawnId=30006, patrolName='MS2PatrolData_106')
            self.move_npc(spawnId=30007, patrolName='MS2PatrolData_107')
            self.set_breakable(triggerIds=[1008], enable=True)
            return CableOff_08(self.ctx)


class CableDelay_09_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__32$', duration=6000)
            self.move_npc(spawnId=30008, patrolName='MS2PatrolData_108')
            self.set_breakable(triggerIds=[1009], enable=True)
            return CableOff_09(self.ctx)


class CableDelay_10_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__33$', duration=6000)
            self.move_npc(spawnId=30009, patrolName='MS2PatrolData_109')
            self.set_breakable(triggerIds=[1010], enable=True)
            return CableOff_10(self.ctx)


class CableDelay_11_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__34$', duration=6000)
            self.move_npc(spawnId=30011, patrolName='MS2PatrolData_111')
            self.move_npc(spawnId=30011, patrolName='MS2PatrolData_111')
            self.set_breakable(triggerIds=[1011], enable=True)
            return CableOff_11(self.ctx)


class CableDelay_12_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$52100302_QD__FIELD_2__35$', duration=6000)
            self.move_npc(spawnId=30012, patrolName='MS2PatrolData_112')
            self.set_breakable(triggerIds=[1012], enable=True)
            return CableOff_12(self.ctx)


class CableOff_07(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=1)
            return End_02(self.ctx)


class CableOff_08(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_09(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_10(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=3)
            return End_02(self.ctx)


class CableOff_11(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=4)
            return End_02(self.ctx)


class CableOff_12(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=1)
            return End_02(self.ctx)


class End_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


initial_state = 대기
