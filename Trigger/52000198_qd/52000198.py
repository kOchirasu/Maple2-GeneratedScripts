""" trigger/52000198_qd/52000198.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=5002, visible=False, enable=False)
        self.set_portal(portalId=2, visible=False, enable=False)
        self.set_portal(portalId=4, visible=False, enable=False)
        self.set_mesh(triggerIds=[8002], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[2]):
            return 도망쳐_12(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[1]):
            return CameraEffect01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[3]):
            return 도망쳐_26(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101]) # 에레브
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000198, portalId=5001)
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect04(self.ctx)


class CameraEffect04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 도망쳐_01(self.ctx)


class 도망쳐_01(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__0$', duration=4000)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__1$', align='left', illustId='Ereb_serious', duration=4500)
        self.add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__2$', duration=4000)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__3$', align='left', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=17000):
            return 도망쳐_01_02(self.ctx)


class 도망쳐_01_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__4$', duration=4000)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 도망쳐_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_02(self.ctx)


class 도망쳐_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$52000198_QD__52000198__5$', duration=4000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2002]):
            return 도망쳐_03(self.ctx)


class 도망쳐_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True)
        self.create_monster(spawnIds=[102]) # 에레브
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2003]):
            return 도망쳐_04(self.ctx)


class 도망쳐_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=102, msg='$52000198_QD__52000198__6$', duration=4000)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2004]):
            return 도망쳐_05(self.ctx)


class 도망쳐_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=True, enable=True)
        self.create_monster(spawnIds=[103]) # 에레브
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2005]):
            return 도망쳐_06(self.ctx)


class 도망쳐_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=103, msg='$52000198_QD__52000198__7$', duration=4000)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2006]):
            return 도망쳐_07(self.ctx)


class 도망쳐_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_08(self.ctx)


class 도망쳐_08(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000198, portalId=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 도망쳐_09(self.ctx)


class 도망쳐_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_10(self.ctx)


class 도망쳐_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__8$', align='right', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 도망쳐_10_01(self.ctx)


class 도망쳐_10_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__9$', duration=4000)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__10$', align='right', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return 도망쳐_10_02(self.ctx)


class 도망쳐_10_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4500)
        self.add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__11$', duration=4500)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__12$', align='right', illustId='Ereb_closeEye', duration=1800)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__13$', align='right', illustId='Ereb_serious', duration=4500)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10800):
            return 도망쳐_11(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_11(self.ctx)


class 도망쳐_11(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=103, msg='$52000198_QD__52000198__14$', duration=4000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2007], questIds=[10003422], questStates=[2]):
            return 도망쳐_12(self.ctx)


class 도망쳐_12(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_13(self.ctx)


class 도망쳐_13(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104]) # 바론
        self.move_user(mapId=52000198, portalId=5004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 도망쳐_14(self.ctx)


class 도망쳐_14(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_3, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_15(self.ctx)


class 도망쳐_15(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__15$', duration=4000)
        self.add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__16$', align='left', illustId='Baron_normal', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return 도망쳐_15_01(self.ctx)


class 도망쳐_15_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000198_QD__52000198__17$', duration=4500)
        self.add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__18$', align='left', illustId='Baron_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__19$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12500):
            return 도망쳐_16(self.ctx)


class 도망쳐_16(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_17(self.ctx)


class 도망쳐_17(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104]) # 아래층바론
        self.create_monster(spawnIds=[105]) # 바론
        self.move_user(mapId=52000198, portalId=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 도망쳐_19(self.ctx)


class 도망쳐_19(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_20(self.ctx)


class 도망쳐_20(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__20$', align='right', illustId='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npcId=11004787, msg='$52000198_QD__52000198__21$', align='left', illustId='Baron_normal', duration=4000)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__22$', align='right', illustId='Ereb_serious', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12500):
            return 도망쳐_21(self.ctx)


class 도망쳐_21(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 도망쳐_22(self.ctx)


class 도망쳐_22(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Object_React_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 도망쳐_23(self.ctx)


class 도망쳐_23(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_mesh(triggerIds=[8001], visible=False)
        self.set_mesh(triggerIds=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 도망쳐_24(self.ctx)


class 도망쳐_24(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.reset_camera(interpolationTime=0)
        self.add_cinematic_talk(npcId=11001302, msg='$52000198_QD__52000198__23$', align='right', illustId='Ereb_serious', duration=3000)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 도망쳐_25(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[104]) # 아래층바론
        self.destroy_monster(spawnIds=[105])
        self.create_monster(spawnIds=[105]) # 바론
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_mesh(triggerIds=[8001], visible=False)
        self.set_mesh(triggerIds=[8002], visible=True)
        self.move_user(mapId=52000198, portalId=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 도망쳐_25(self.ctx)


class 도망쳐_25(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawnIds=[103])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003422], questStates=[3]):
            return 도망쳐_26(self.ctx)


class 도망쳐_26(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=5002, visible=True, enable=True) # 불길 속으로 퀘스트 바론에게 완료하고 나면 포탈이 활성화 되게 수정
        self.destroy_monster(spawnIds=[105])


initial_state = start
