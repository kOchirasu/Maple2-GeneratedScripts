""" trigger/02020310_bf/field_1.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000304], state=2)
        self.set_interact_object(triggerIds=[12000305], state=2)
        self.set_interact_object(triggerIds=[12000306], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900002, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block', value=2):
            self.set_user_value(triggerId=900002, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block', value=3):
            self.set_user_value(triggerId=900002, key='Block', value=0)
            return Block_3(self.ctx)


class Block_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1104,1150,1151,1152,1157,1158,1159,1160,1161]):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_1__0$', duration=5000)
            self.set_interact_object(triggerIds=[12000304], state=1)
            self.create_monster(spawnIds=[1107], animationEffect=False)
            self.create_monster(spawnIds=[1108], animationEffect=False)
            self.create_monster(spawnIds=[1109], animationEffect=False)
            self.create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], animationEffect=False)
            self.create_monster(spawnIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], animationEffect=False)
            self.create_monster(spawnIds=[1221,1222,1223,1224], animationEffect=False)
            self.create_monster(spawnIds=[30001,30002,30003,30004], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=102, isEnable=False)
            self.enable_spawn_point_pc(spawnId=103, isEnable=True)
            return CableOn_04(self.ctx)


class Block_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1105,1153,1154,1162,1163,1164,1165,1166]):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_1__1$', duration=5000)
            self.set_interact_object(triggerIds=[12000305], state=1)
            self.create_monster(spawnIds=[1107], animationEffect=False)
            self.create_monster(spawnIds=[1108], animationEffect=False)
            self.create_monster(spawnIds=[1109], animationEffect=False)
            self.create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], animationEffect=False)
            self.create_monster(spawnIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], animationEffect=False)
            self.create_monster(spawnIds=[1221,1222,1223,1224], animationEffect=False)
            self.create_monster(spawnIds=[30001,30002,30003,30004], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=102, isEnable=False)
            self.enable_spawn_point_pc(spawnId=104, isEnable=True)
            return CableOn_05(self.ctx)


class Block_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1106,1155,1156,1167,1168,1169,1170,1171,1172]):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_1__2$', duration=5000)
            self.set_interact_object(triggerIds=[12000306], state=1)
            self.create_monster(spawnIds=[1107], animationEffect=False)
            self.create_monster(spawnIds=[1108], animationEffect=False)
            self.create_monster(spawnIds=[1109], animationEffect=False)
            self.create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], animationEffect=False)
            self.create_monster(spawnIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], animationEffect=False)
            self.create_monster(spawnIds=[1221,1222,1223,1224], animationEffect=False)
            self.create_monster(spawnIds=[30001,30002,30003,30004], animationEffect=False)
            self.enable_spawn_point_pc(spawnId=102, isEnable=False)
            self.enable_spawn_point_pc(spawnId=105, isEnable=True)
            return CableOn_06(self.ctx)


class CableOn_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000304], stateValue=0):
            self.set_interact_object(triggerIds=[12000304], state=0)
            self.destroy_monster(spawnIds=[30003,30004], arg2=False)
            self.set_mesh(triggerIds=[1100101,1100102,1100103,1100104,1100105,1100106,1100107,1100108,1100109,1100110], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_04(self.ctx)


class CableOn_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000305], stateValue=0):
            self.set_interact_object(triggerIds=[12000305], state=0)
            self.destroy_monster(spawnIds=[30001,30002,30004], arg2=False)
            self.set_mesh(triggerIds=[1100201,1100202,1100203,1100204,1100205,1100206,1100207,1100208,1100209,1100210], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_05(self.ctx)


class CableOn_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000306], stateValue=0):
            self.set_interact_object(triggerIds=[12000306], state=0)
            self.destroy_monster(spawnIds=[30001,30002,30003], arg2=False)
            self.set_mesh(triggerIds=[1100301,1100302,1100303,1100304,1100305,1100306,1100307,1100308,1100309,1100310], visible=False, arg3=0, delay=0, scale=0)
            return CableDelay_06(self.ctx)


class CableDelay_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__3$', arg3='3000')
            return CableDelay_04_2(self.ctx)


class CableDelay_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__4$', arg3='3000')
            return CableDelay_05_2(self.ctx)


class CableDelay_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__5$', arg3='3000')
            return CableDelay_06_2(self.ctx)


class CableDelay_04_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__6$', arg3='1000')
            return CableDelay_04_3(self.ctx)


class CableDelay_05_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__7$', arg3='1000')
            return CableDelay_05_3(self.ctx)


class CableDelay_06_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__8$', arg3='1000')
            return CableDelay_06_3(self.ctx)


class CableDelay_04_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__9$', arg3='1000')
            return CableDelay_04_4(self.ctx)


class CableDelay_05_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__10$', arg3='1000')
            return CableDelay_05_4(self.ctx)


class CableDelay_06_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__11$', arg3='1000')
            return CableDelay_06_4(self.ctx)


class CableDelay_04_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__12$', arg3='1000')
            return CableDelay_04_5(self.ctx)


class CableDelay_05_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__13$', arg3='1000')
            return CableDelay_05_5(self.ctx)


class CableDelay_06_4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__14$', arg3='1000')
            return CableDelay_06_5(self.ctx)


class CableDelay_04_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1004], enable=True)
            self.move_npc(spawnId=30001, patrolName='MS2PatrolData_101')
            self.move_npc(spawnId=30002, patrolName='MS2PatrolData_102')
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__15$', arg3='5000')
            return CableOff_04(self.ctx)


class CableDelay_05_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1005], enable=True)
            self.move_npc(spawnId=30003, patrolName='MS2PatrolData_103')
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__16$', arg3='5000')
            return CableOff_05(self.ctx)


class CableDelay_06_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1006], enable=True)
            self.move_npc(spawnId=30004, patrolName='MS2PatrolData_104')
            self.set_event_ui(type=1, arg2='$02020310_BF__FIELD_1__17$', arg3='5000')
            return CableOff_06(self.ctx)


class CableOff_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_mesh(triggerIds=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh_animation(triggerIds=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True, arg3=0, arg4=0)
            self.set_mesh_animation(triggerIds=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True, arg3=0, arg4=0)
            self.set_mesh_animation(triggerIds=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True, arg3=0, arg4=0)
            self.set_user_value(triggerId=900003, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_mesh(triggerIds=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh_animation(triggerIds=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True, arg3=0, arg4=0)
            self.set_mesh_animation(triggerIds=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True, arg3=0, arg4=0)
            self.set_mesh_animation(triggerIds=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True, arg3=0, arg4=0)
            self.set_user_value(triggerId=900003, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_mesh(triggerIds=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True, arg3=0, delay=0, scale=0)
            self.set_mesh_animation(triggerIds=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True, arg3=0, arg4=0)
            self.set_mesh_animation(triggerIds=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True, arg3=0, arg4=0)
            self.set_mesh_animation(triggerIds=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True, arg3=0, arg4=0)
            self.set_user_value(triggerId=900003, key='Block', value=3)
            return End_01(self.ctx)


class End_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


initial_state = 대기
