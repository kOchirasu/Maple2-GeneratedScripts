""" trigger/52000202_qd/52000202.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003431], questStates=[1]):
            return CameraEffect01(self.ctx)
        if not self.quest_user_detected(boxIds=[2001], questIds=[10003431], questStates=[1]):
            return 고마해_04(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000202, portalId=5001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3001')
        self.show_caption(type='VerticalCaption', title='$52000202_QD__52000202__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시공의균열(self.ctx)


class 시공의균열(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003,4004], returnView=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__1$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__2$', duration=5000)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__3$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=14000):
            return 시공의균열_02_01(self.ctx)


class 시공의균열_02_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_long.xml')
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=11000)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시공의균열_02_02(self.ctx)


class 시공의균열_02_02(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__5$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__6$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 시공의균열_03(self.ctx)


class 시공의균열_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_long.xml')
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.create_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202])
        self.set_portal(portalId=8001, visible=False, enable=False)
        self.set_portal(portalId=8002, visible=False, enable=False)
        self.move_user(mapId=52000202, portalId=5002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 시공의균열_03_02(self.ctx)


class 시공의균열_03_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.create_monster(spawnIds=[203])
        self.create_monster(spawnIds=[204])
        self.set_portal(portalId=8003, visible=False, enable=False)
        self.set_portal(portalId=8004, visible=False, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 시공의균열_04(self.ctx)


class 시공의균열_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4007,4008], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__7$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__8$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 전투준비(self.ctx)


class 전투준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=4500)
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__9$', duration=4500)
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[203])
        self.destroy_monster(spawnIds=[204])
        self.create_monster(spawnIds=[205])
        self.create_monster(spawnIds=[206])
        self.create_monster(spawnIds=[207])
        self.create_monster(spawnIds=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return UI테스트(self.ctx)


class UI테스트(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 몰려온다(self.ctx)


class 몰려온다(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3006') # 뛰어가기
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=207, patrolName='MS2PatrolData_3004')
        self.move_npc(spawnId=208, patrolName='MS2PatrolData_3005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몰려온다_02(self.ctx)


class 몰려온다_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.1, endScale=0.5, duration=5, interpolator=1)
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몰려온다_03(self.ctx)


class 몰려온다_03(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[205])
        self.destroy_monster(spawnIds=[206])
        self.destroy_monster(spawnIds=[207])
        self.destroy_monster(spawnIds=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 고마해(self.ctx)


class 고마해(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_cinematic_ui(type=1)
        self.select_camera_path(pathIds=[4011], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 고마해_02(self.ctx)


class 고마해_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__10$', duration=2500)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__11$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__12$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9500):
            return 고마해_03(self.ctx)


class 고마해_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=9000)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_long.xml')
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__13$', duration=4500)
        self.add_cinematic_talk(npcId=0, msg='$52000202_QD__52000202__14$', duration=4000)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return 고마해_04(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 고마해_04(self.ctx)


class 고마해_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(triggerId=2001, achieve='illusionaryAttack')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 이동시키기(self.ctx)


class 이동시키기(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000201, portalId=5001)


initial_state = start
