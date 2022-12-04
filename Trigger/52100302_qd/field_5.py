""" trigger/52100302_qd/field_5.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000322], state=2)
        self.set_interact_object(triggerIds=[12000600], state=0)
        self.set_interact_object(triggerIds=[12000601], state=0)
        self.set_interact_object(triggerIds=[12000602], state=0)
        self.set_interact_object(triggerIds=[12000603], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900006, key='Block', value=0)
            return Archeon_Ready(self.ctx)


class Archeon_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1117,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1512,1513]):
            self.side_npc_talk(type='talk', npcId=11004607, illust='Neirin_normal', script='$52100302_QD__FIELD_5__0$', duration=5000)
            self.set_interact_object(triggerIds=[12000600], state=1)
            self.enable_spawn_point_pc(spawnId=113, isEnable=False)
            self.enable_spawn_point_pc(spawnId=114, isEnable=False)
            self.enable_spawn_point_pc(spawnId=115, isEnable=False)
            self.enable_spawn_point_pc(spawnId=116, isEnable=True)
            return Archeon_On(self.ctx)


class Archeon_On(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000600], stateValue=0):
            return Archeon_Move1_0(self.ctx)


class Archeon_Move1_0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_portal(portalId=10001, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=10003, visible=False, enable=True, minimapVisible=False)
            self.patrol_condition_user(patrolName='MS2PatrolData_01', patrolIndex=1, additionalEffectId=73000005)
            self.create_monster(spawnIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010], animationEffect=False)
            self.create_monster(spawnIds=[10011,10012,10013,10014,10015,10016,10017,10018,10019,10020], animationEffect=False)
            self.create_monster(spawnIds=[10021,10022,10023,10024,10025,10026,10027,10028,10029], animationEffect=False)
            return Archeon_Arrive(self.ctx)


class Archeon_Arrive(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_5__1$', duration=6500) # 10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029]):
            self.side_npc_talk(type='talk', npcId=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_5__2$', duration=5000)
            self.patrol_condition_user(patrolName='MS2PatrolData_05', patrolIndex=5, additionalEffectId=73000005)
            self.enable_spawn_point_pc(spawnId=116, isEnable=False)
            self.enable_spawn_point_pc(spawnId=117, isEnable=True)
            self.set_portal(portalId=10000, visible=True, enable=True, minimapVisible=True)
            return Archeon_Move2_1(self.ctx)


class Archeon_Move2_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_portal(portalId=10005, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=10007, visible=False, enable=True, minimapVisible=False)
            return Archeon_Leave(self.ctx)


class Archeon_Leave(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9100]):
            return Archeon_OffDelay(self.ctx)


class Archeon_OffDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Archeon_Off(self.ctx)


class Archeon_Off(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9100], skillId=73000009, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마를레네_연출(self.ctx)


# 퀘스트연출시작
class 마를레네_연출(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[999], animationEffect=False)
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.move_user(mapId=52100302, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네_연출_02(self.ctx)


class 마를레네_연출_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네_연출_03(self.ctx)


class 마를레네_연출_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=999, patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=11004680, illustId='Eone_normal', align='right', msg='$52100302_QD__FIELD_5__3$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 마를레네_연출_04(self.ctx)


class 마를레네_연출_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.set_npc_emotion_loop(spawnId=999, sequenceName='Talk_A', duration=8000)
        self.add_cinematic_talk(npcId=11004680, illustId='Eone_normal', align='right', msg='$52100302_QD__FIELD_5__4$', duration=4000)
        self.add_cinematic_talk(npcId=11004680, illustId='Eone_normal', align='right', msg='$52100302_QD__FIELD_5__5$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네_연출_05(self.ctx)


class 마를레네_연출_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네_연출_06(self.ctx)


class 마를레네_연출_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.add_buff(boxIds=[9100], skillId=73000009, level=1, isPlayer=False, isSkillSet=False)


initial_state = 대기
