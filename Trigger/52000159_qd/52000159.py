""" trigger/52000159_qd/52000159.xml """
import common


class wait_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002735], questStates=[2]):
            return 정리_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002736], questStates=[2]):
            return 정리_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002737], questStates=[2]):
            return 정리_01(self.ctx)
        if self.user_detected(boxIds=[2001], jobCode=0):
            return wait_01_1(self.ctx)


class wait_01_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000159, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 어쌔신과거_01(self.ctx)


class 어쌔신과거_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 어쌔신과거_02(self.ctx)


class 어쌔신과거_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 어쌔신과거_03(self.ctx)


class 어쌔신과거_03(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.show_caption(type='VerticalCaption', title='$52000159_QD__52000159__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어쌔신과거_04(self.ctx)


class 어쌔신과거_04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__1$', duration=4000)
        self.move_user_path(patrolName='MS2PatrolData_3001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어쌔신과거_05(self.ctx)


class 어쌔신과거_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__2$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__3$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__4$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__5$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return 어쌔신과거_06(self.ctx)


class 어쌔신과거_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__6$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__7$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 어쌔신과거_07(self.ctx)


class 어쌔신과거_07(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__8$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52000159_QD__52000159__9$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 암전(self.ctx)


class 암전(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도클로_01(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도클로_01(self.ctx)


class 쉐도클로_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.set_effect(triggerIds=[5001], visible=True)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.set_effect(triggerIds=[5002], visible=True)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.set_effect(triggerIds=[5003], visible=True)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.set_effect(triggerIds=[5004], visible=True)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.set_effect(triggerIds=[5005], visible=True)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_effect(triggerIds=[5006], visible=True)
        self.move_user(mapId=52000159, portalId=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 쉐도클로_02(self.ctx)


class 쉐도클로_02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_01(self.ctx)


class 정리_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 정리_02(self.ctx)


class 정리_02(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)
        self.destroy_monster(spawnIds=[101], arg2=False)
        self.destroy_monster(spawnIds=[103], arg2=False)
        self.destroy_monster(spawnIds=[105], arg2=False)
        self.destroy_monster(spawnIds=[106], arg2=False)
        self.destroy_monster(spawnIds=[107], arg2=False)
        self.destroy_monster(spawnIds=[108], arg2=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002735], questStates=[2]):
            return 남자의죽음_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002736], questStates=[2]):
            return 남자의죽음_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002737], questStates=[2]):
            return 남자의죽음_01(self.ctx)


class 남자의죽음_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 남자의죽음_01_02(self.ctx)


class 남자의죽음_01_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.select_camera_path(pathIds=[4007], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 남자의죽음_02(self.ctx)


class 남자의죽음_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 남자의죽음_03(self.ctx)


class 남자의죽음_03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Attack_01_B')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Dead_B', duration=9E+12)
        self.set_effect(triggerIds=[5007], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 남자의죽음_03_01(self.ctx)


class 남자의죽음_03_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 남자의죽음_04(self.ctx)


class Skip_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 남자의죽음_04(self.ctx)


class 남자의죽음_04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102], arg2=False)
        self.create_monster(spawnIds=[114], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=114, sequenceName='Dead_B', duration=9E+12)
        self.create_monster(spawnIds=[115], animationEffect=False)
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 남자의죽음_05(self.ctx)


class 남자의죽음_05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002737], questStates=[2]):
            return 쉐도클로표창_01(self.ctx)


class 쉐도클로표창_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도클로표창_01_01(self.ctx)


class 쉐도클로표창_01_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.visible_my_pc(isVisible=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도클로표창_02(self.ctx)


class 쉐도클로표창_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawnId=104, sequenceName='Attack_Idle_A', duration=4000)
        self.set_scene_skip(state=Skip_3, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 쉐도클로표창_03(self.ctx)


class 쉐도클로표창_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_npc_emotion_loop(spawnId=104, sequenceName='Attack_01_B', duration=80000)
        self.set_time_scale(enable=True, startScale=0.1, endScale=0.1, duration=10, interpolator=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 쉐도클로표창_03_01(self.ctx)


class 쉐도클로표창_03_01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=115, sequenceName='Dead_A', duration=80000)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 쉐도클로표창_04(self.ctx)


class Skip_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도클로표창_04(self.ctx)


class 쉐도클로표창_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 쉐도클로표창_05(self.ctx)


class 쉐도클로표창_05(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=52000158, portalId=6001)


initial_state = wait_01
