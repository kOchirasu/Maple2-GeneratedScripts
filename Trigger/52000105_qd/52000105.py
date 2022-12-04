""" trigger/52000105_qd/52000105.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False) # 텐

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002320], questStates=[1]):
            return 몬스터처치훈련01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002321], questStates=[1]):
            return 몬스터처치훈련02(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[1]):
            return 할아버지대련01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[2]):
            return 대련종료씬시작01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[3]):
            return 대련종료씬시작01(self.ctx)


# ########################씬2 몬스터 소환 교육01~02########################
class 몬스터처치훈련01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[300,301,302], animationEffect=False)
        self.show_guide_summary(entityId=25201051, textId=25201051, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002321], questStates=[1]):
            return 몬스터처치훈련02(self.ctx)


class 몬스터처치훈련02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[400,401,402], animationEffect=False)
        self.show_guide_summary(entityId=25201052, textId=25201052, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[1]):
            return 할아버지대련01(self.ctx)


# ########################씬3 할아버지 대련########################
class 할아버지대련01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000105, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 할아버지대련02_b(self.ctx)


class 할아버지대련02_b(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_ten_comeFront')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1000,1001,1002,1003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return 할아버지대련03(self.ctx)


class 할아버지대련03(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=1, endScale=0.5, duration=2, interpolator=2) # 2초간 느려지기 시작
        self.set_npc_emotion_loop(spawnId=200, sequenceName='Attack_Idle_A', duration=15000)
        self.select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 할아버지대련04(self.ctx)


class 할아버지대련04(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        self.select_camera_path(pathIds=[1006,1007], returnView=False)
        self.add_balloon_talk(spawnId=0, msg='$52000105_QD__52000105__0$', duration=6000, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 할아버지대련05_B(self.ctx)


class 할아버지대련05_B(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_PC_Run_0')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 할아버지대련05(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 할아버지대련05(self.ctx)


class 할아버지대련05(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawnIds=[200])
        self.create_monster(spawnIds=[500], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.5)
        self.show_guide_summary(entityId=25201053, textId=25201053, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[2]):
            return 대련종료씬시작01(self.ctx)


class 대련종료씬시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawnIds=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대련종료씬시작02(self.ctx)


# ########################대련 종료씬########################
class 대련종료씬시작02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[200])
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.move_user(mapId=52000105, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 대련종료씬시작02_01(self.ctx)


class 대련종료씬시작02_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 대련종료씬시작03(self.ctx)


class 대련종료씬시작03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Attack_Idle_A', duration=5000)
        self.move_user_path(patrolName='MS2PatrolData_PC_Run_0')
        self.select_camera_path(pathIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2012,2013], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 대련종료씬시작04(self.ctx)


class 대련종료씬시작04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2014,2015], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대련종료씬시작06(self.ctx)


class 대련종료씬시작06(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.3, endScale=0.3, duration=2.5, interpolator=3) # 2초간 느려지기 시작
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Attack_01_B')
        self.select_camera_path(pathIds=[2016,2017], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return 대련종료씬시작07(self.ctx)


class 대련종료씬시작07(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Dead_A'])
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 대련종료씬시작07_b(self.ctx)


class 대련종료씬시작07_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 대련종료씬시작08(self.ctx)


class 대련종료씬시작08(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=100, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_pc_emotion_sequence(sequenceNames=['Stuck_A'])
        self.select_camera_path(pathIds=[2018,2019], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대련종료씬시작09(self.ctx)


class 대련종료씬시작09(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대련종료씬시작10(self.ctx)


class 대련종료씬시작10(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolationTime=1)
        self.set_pc_emotion_loop(sequenceName='Stun_A', duration=6500)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_ririn_go')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대련종료씬시작11(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolationTime=1)
        self.set_pc_emotion_loop(sequenceName='Stun_A', duration=6500)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_ririn_go')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대련종료씬시작11(self.ctx)


class 대련종료씬시작11(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002322], questStates=[3]):
            return 떠나는할아버지01(self.ctx)


# ########################씬4 떠나는할아버지01########################
class 떠나는할아버지01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=떠나는할아버지07, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 떠나는할아버지02(self.ctx)


class 떠나는할아버지02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_ten_exit_0')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_ririn_Turn')
        self.move_user_path(patrolName='MS2PatrolData_PC_Turn')
        self.select_camera_path(pathIds=[1008,1009], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 떠나는할아버지03(self.ctx)


class 떠나는할아버지03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003175, illustId='Ten_normal', msg='$52000105_QD__52000105__1$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 떠나는할아버지04(self.ctx)


class 떠나는할아버지04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_tenExit_1')
        self.add_balloon_talk(spawnId=0, msg='$52000105_QD__52000105__2$', duration=6000, delayTick=1000)
        self.add_balloon_talk(spawnId=201, msg='$52000105_QD__52000105__3$', duration=6000, delayTick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 떠나는할아버지05(self.ctx)


class 떠나는할아버지05(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 떠나는할아버지06(self.ctx)


class 떠나는할아버지06(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52000105_QD__52000105__4$', desc='$52000105_QD__52000105__5$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 떠나는할아버지07(self.ctx)


class 떠나는할아버지07(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=52000106, portalId=1)


initial_state = Wait
