""" trigger/52100302_qd/field_5.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000322], state=2)
        set_interact_object(triggerIds=[12000600], state=0)
        set_interact_object(triggerIds=[12000601], state=0)
        set_interact_object(triggerIds=[12000602], state=0)
        set_interact_object(triggerIds=[12000603], state=0)

    def on_tick(self) -> state.State:
        if user_value(key='Block', value=1):
            set_user_value(triggerId=900006, key='Block', value=0)
            return Archeon_Ready()


class Archeon_Ready(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1117,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1512,1513]):
            side_npc_talk(type='talk', npcId=11004607, illust='Neirin_normal', script='$52100302_QD__FIELD_5__0$', duration=5000)
            set_interact_object(triggerIds=[12000600], state=1)
            enable_spawn_point_pc(spawnId=113, isEnable=False)
            enable_spawn_point_pc(spawnId=114, isEnable=False)
            enable_spawn_point_pc(spawnId=115, isEnable=False)
            enable_spawn_point_pc(spawnId=116, isEnable=True)
            return Archeon_On()


class Archeon_On(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000600], arg2=0):
            return Archeon_Move1_0()


class Archeon_Move1_0(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_portal(portalId=10001, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=10003, visible=False, enabled=True, minimapVisible=False)
            patrol_condition_user(patrolName='MS2PatrolData_01', patrolIndex=1, additionalEffectId=73000005)
            create_monster(spawnIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010], arg2=False)
            create_monster(spawnIds=[10011,10012,10013,10014,10015,10016,10017,10018,10019,10020], arg2=False)
            create_monster(spawnIds=[10021,10022,10023,10024,10025,10026,10027,10028,10029], arg2=False)
            return Archeon_Arrive()


class Archeon_Arrive(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_5__1$', duration=6500) # 10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029]):
            side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_5__2$', duration=5000)
            patrol_condition_user(patrolName='MS2PatrolData_05', patrolIndex=5, additionalEffectId=73000005)
            enable_spawn_point_pc(spawnId=116, isEnable=False)
            enable_spawn_point_pc(spawnId=117, isEnable=True)
            set_portal(portalId=10000, visible=True, enabled=True, minimapVisible=True)
            return Archeon_Move2_1()


class Archeon_Move2_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            set_portal(portalId=10005, visible=True, enabled=True, minimapVisible=True)
            set_portal(portalId=10007, visible=False, enabled=True, minimapVisible=False)
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
            return 마를레네_연출()


# 퀘스트연출시작
class 마를레네_연출(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[999], arg2=False)
        select_camera_path(pathIds=[4001], returnView=False)
        move_user(mapId=52100302, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네_연출_02()


class 마를레네_연출_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네_연출_03()


class 마를레네_연출_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        move_npc(spawnId=999, patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=11004680, illustId='Eone_normal', align='right', msg='$52100302_QD__FIELD_5__3$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 마를레네_연출_04()


class 마를레네_연출_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        set_npc_emotion_loop(spawnId=999, sequenceName='Talk_A', duration=8000)
        add_cinematic_talk(npcId=11004680, illustId='Eone_normal', align='right', msg='$52100302_QD__FIELD_5__4$', duration=4000)
        add_cinematic_talk(npcId=11004680, illustId='Eone_normal', align='right', msg='$52100302_QD__FIELD_5__5$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네_연출_05()


class 마를레네_연출_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마를레네_연출_06()


class 마를레네_연출_06(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        add_buff(boxIds=[9100], skillId=73000009, level=1, arg4=False, arg5=False)


