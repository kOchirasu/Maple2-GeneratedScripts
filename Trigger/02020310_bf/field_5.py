""" trigger/02020310_bf/field_5.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000322], state=2)
        set_interact_object(triggerIds=[12000400], state=0)
        set_interact_object(triggerIds=[12000401], state=0)
        set_interact_object(triggerIds=[12000402], state=0)
        set_interact_object(triggerIds=[12000403], state=0)

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900006, key='Block', value=0)
            return Archeon_Ready()


class Archeon_Ready(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1117,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1512,1513]):
            side_npc_talk(type='talk', npcId=11004607, illust='Neirin_normal', script='$02020310_BF__FIELD_5__0$', duration=5000)
            set_interact_object(triggerIds=[12000400], state=1)
            set_interact_object(triggerIds=[12000401], state=1)
            set_interact_object(triggerIds=[12000402], state=1)
            set_interact_object(triggerIds=[12000403], state=1)
            enable_spawn_point_pc(spawnId=113, isEnable=False)
            enable_spawn_point_pc(spawnId=114, isEnable=False)
            enable_spawn_point_pc(spawnId=115, isEnable=False)
            enable_spawn_point_pc(spawnId=116, isEnable=True)
            return Archeon_On()


class Archeon_On(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000400,12000401,12000402,12000403], arg2=0):
            return Archeon_Move1_0()


class Archeon_Move1_0(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_portal(portalId=10001, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=10002, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=10003, visible=False, enabled=True, minimapVisible=False)
            set_portal(portalId=10004, visible=False, enabled=True, minimapVisible=False)
            patrol_condition_user(patrolName='MS2PatrolData_01', patrolIndex=1, additionalEffectId=73000005)
            patrol_condition_user(patrolName='MS2PatrolData_02', patrolIndex=2, additionalEffectId=73000006)
            patrol_condition_user(patrolName='MS2PatrolData_03', patrolIndex=3, additionalEffectId=73000007)
            patrol_condition_user(patrolName='MS2PatrolData_04', patrolIndex=4, additionalEffectId=73000008)
            create_monster(spawnIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010], arg2=False)
            create_monster(spawnIds=[10011,10012,10013,10014,10015,10016,10017,10018,10019,10020], arg2=False)
            create_monster(spawnIds=[10021,10022,10023,10024,10025,10026,10027,10028,10029], arg2=False)
            create_monster(spawnIds=[11001,11002,11003,11004,11005,11006,11007,11008,11009,11010], arg2=False)
            create_monster(spawnIds=[11011,11012,11013,11014,11015,11016,11017,11018,11019,11020], arg2=False)
            create_monster(spawnIds=[11021,11022,11023,11024,11025,11026,11027,11028,11029], arg2=False)
            return Archeon_Arrive()


class Archeon_Arrive(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_5__1$', duration=6500) # 10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014,11015,11016,11017,11018,11019,11020,11021,11022,11023,11024,11025,11026,11027,11028,11029]):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_5__2$', duration=5000)
            patrol_condition_user(patrolName='MS2PatrolData_05', patrolIndex=5, additionalEffectId=73000005)
            patrol_condition_user(patrolName='MS2PatrolData_06', patrolIndex=6, additionalEffectId=73000006)
            patrol_condition_user(patrolName='MS2PatrolData_07', patrolIndex=7, additionalEffectId=73000007)
            patrol_condition_user(patrolName='MS2PatrolData_08', patrolIndex=8, additionalEffectId=73000008)
            enable_spawn_point_pc(spawnId=116, isEnable=False)
            enable_spawn_point_pc(spawnId=117, isEnable=True)
            set_portal(portalId=10000, visible=True, enabled=True, minimapVisible=True)
            return Archeon_Move2_1()


class Archeon_Move2_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            set_portal(portalId=10005, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=10006, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=10007, visible=False, enabled=True, minimapVisible=False)
            set_portal(portalId=10008, visible=False, enabled=True, minimapVisible=False)
            return Archeon_Leave()


class Archeon_Leave(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return Archeon_OffDelay()


class Archeon_OffDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Archeon_Off()


class Archeon_Off(state.State):
    def on_enter(self):
        add_buff(boxIds=[9100], skillId=73000009, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Archeon_OffDelay()


