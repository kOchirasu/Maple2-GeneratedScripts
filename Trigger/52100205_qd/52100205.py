""" trigger/52100205_qd/52100205.xml """
import common


class start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2001]):
            return CameraEffect01(self.ctx)


class CameraEffect01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201])
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52100205, portalId=5001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02_02(self.ctx)


class CameraEffect02_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52100205_QD__52100205__0$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraEffect03(self.ctx)


class CameraEffect03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraEffect03_2(self.ctx)


class CameraEffect03_2(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52100205_QD__52100205__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraEffect03_4(self.ctx)


class CameraEffect03_4(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_5(self.ctx)


class CameraEffect03_5(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[201])
        self.visible_my_pc(isVisible=True) # 유저 투명 처리 품
        self.set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        self.add_buff(boxIds=[2001], skillId=99910400, level=1, isPlayer=False, isSkillSet=True) # 클라디아 변신
        self.add_buff(boxIds=[2001], skillId=99910400, level=1, isPlayer=False, isSkillSet=False) # 클라디아 변신

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_6(self.ctx)


class CameraEffect03_6(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_7(self.ctx)


class CameraEffect03_7(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004612, msg='$52100205_QD__52100205__2$', align='left', illustId='cladia_normal', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return CameraEffect03_8(self.ctx)


class CameraEffect03_8(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2002]):
            return 제시카_01(self.ctx)


class 제시카_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제시카_02(self.ctx)


class 제시카_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.create_monster(spawnIds=[101]) # 제시카

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 제시카_03(self.ctx)


class 제시카_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 제시카_04(self.ctx)


class 제시카_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 제시카_05(self.ctx)


class 제시카_05(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11004575, msg='$52100205_QD__52100205__3$', align='left', illustId='Jessica_normal', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 제시카_06(self.ctx)


class 제시카_06(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제시카_07(self.ctx)


class 제시카_07(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)


initial_state = start
