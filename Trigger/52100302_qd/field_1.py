""" trigger/52100302_qd/field_1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000504], state=2)
        set_interact_object(triggerIds=[12000505], state=2)
        set_interact_object(triggerIds=[12000506], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900002, key='Block', value=0)
            return Block_1()
        if user_value(key='Block', value=2):
            set_user_value(triggerId=900002, key='Block', value=0)
            return Block_2()
        if user_value(key='Block', value=3):
            set_user_value(triggerId=900002, key='Block', value=0)
            return Block_3()


class Block_1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1104,1150,1151,1152,1157,1158,1159,1160,1161]):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_1__0$', duration=5000)
            set_interact_object(triggerIds=[12000504], state=1)
            create_monster(spawnIds=[1107], arg2=False)
            create_monster(spawnIds=[1108], arg2=False)
            create_monster(spawnIds=[1109], arg2=False)
            create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], arg2=False)
            create_monster(spawnIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], arg2=False)
            create_monster(spawnIds=[1221,1222,1223,1224], arg2=False)
            create_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            enable_spawn_point_pc(spawnId=102, isEnable=False)
            enable_spawn_point_pc(spawnId=103, isEnable=True)
            return CableOn_04()


class Block_2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1105,1153,1154,1162,1163,1164,1165,1166]):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_1__1$', duration=5000)
            set_interact_object(triggerIds=[12000505], state=1)
            create_monster(spawnIds=[1107], arg2=False)
            create_monster(spawnIds=[1108], arg2=False)
            create_monster(spawnIds=[1109], arg2=False)
            create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], arg2=False)
            create_monster(spawnIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], arg2=False)
            create_monster(spawnIds=[1221,1222,1223,1224], arg2=False)
            create_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            enable_spawn_point_pc(spawnId=102, isEnable=False)
            enable_spawn_point_pc(spawnId=104, isEnable=True)
            return CableOn_05()


class Block_3(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1106,1155,1156,1167,1168,1169,1170,1171,1172]):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_1__2$', duration=5000)
            set_interact_object(triggerIds=[12000506], state=1)
            create_monster(spawnIds=[1107], arg2=False)
            create_monster(spawnIds=[1108], arg2=False)
            create_monster(spawnIds=[1109], arg2=False)
            create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], arg2=False)
            create_monster(spawnIds=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], arg2=False)
            create_monster(spawnIds=[1221,1222,1223,1224], arg2=False)
            create_monster(spawnIds=[30001,30002,30003,30004], arg2=False)
            enable_spawn_point_pc(spawnId=102, isEnable=False)
            enable_spawn_point_pc(spawnId=105, isEnable=True)
            return CableOn_06()


class CableOn_04(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000504], arg2=0):
            set_interact_object(triggerIds=[12000504], state=0)
            destroy_monster(spawnIds=[30003,30004], arg2=False)
            set_mesh(triggerIds=[1100101,1100102,1100103,1100104,1100105,1100106,1100107,1100108,1100109,1100110], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_04()


class CableOn_05(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000505], arg2=0):
            set_interact_object(triggerIds=[12000505], state=0)
            destroy_monster(spawnIds=[30001,30002,30004], arg2=False)
            set_mesh(triggerIds=[1100201,1100202,1100203,1100204,1100205,1100206,1100207,1100208,1100209,1100210], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_05()


class CableOn_06(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000506], arg2=0):
            set_interact_object(triggerIds=[12000506], state=0)
            destroy_monster(spawnIds=[30001,30002,30003], arg2=False)
            set_mesh(triggerIds=[1100301,1100302,1100303,1100304,1100305,1100306,1100307,1100308,1100309,1100310], visible=False, arg3=0, arg4=0, arg5=0)
            return CableDelay_06()


class CableDelay_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__3$', arg3='3000')
            return CableDelay_04_2()


class CableDelay_05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__4$', arg3='3000')
            return CableDelay_05_2()


class CableDelay_06(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__5$', arg3='3000')
            return CableDelay_06_2()


class CableDelay_04_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__6$', arg3='1000')
            return CableDelay_04_3()


class CableDelay_05_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__7$', arg3='1000')
            return CableDelay_05_3()


class CableDelay_06_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__8$', arg3='1000')
            return CableDelay_06_3()


class CableDelay_04_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__9$', arg3='1000')
            return CableDelay_04_4()


class CableDelay_05_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__10$', arg3='1000')
            return CableDelay_05_4()


class CableDelay_06_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__11$', arg3='1000')
            return CableDelay_06_4()


class CableDelay_04_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__12$', arg3='1000')
            return CableDelay_04_5()


class CableDelay_05_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__13$', arg3='1000')
            return CableDelay_05_5()


class CableDelay_06_4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_event_ui(type=1, arg2='$52100302_QD__FIELD_1__14$', arg3='1000')
            return CableDelay_06_5()


class CableDelay_04_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1004], enabled=True)
            move_npc(spawnId=30001, patrolName='MS2PatrolData_101')
            move_npc(spawnId=30002, patrolName='MS2PatrolData_102')
            return CableOff_04()


class CableDelay_05_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1005], enabled=True)
            move_npc(spawnId=30003, patrolName='MS2PatrolData_103')
            return CableOff_05()


class CableDelay_06_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_breakable(triggerIds=[1006], enabled=True)
            move_npc(spawnId=30004, patrolName='MS2PatrolData_104')
            return CableOff_06()


class CableOff_04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900003, key='Block', value=1)
            return End_01()


class CableOff_05(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900003, key='Block', value=2)
            return End_01()


class CableOff_06(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_user_value(triggerId=900003, key='Block', value=3)
            return End_01()


class End_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


