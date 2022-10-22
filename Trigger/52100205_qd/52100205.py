""" trigger/52100205_qd/52100205.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201])
        select_camera_path(pathIds=[4001], returnView=False)
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)
        move_user(mapId=52100205, portalId=5001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02_02()


class CameraEffect02_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52100205_QD__52100205__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect03_2()


class CameraEffect03_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CameraEffect03_3()


class CameraEffect03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        show_caption(type='VerticalCaption', title='$52100205_QD__52100205__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraEffect03_4()


class CameraEffect03_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_5()


class CameraEffect03_5(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[201])
        visible_my_pc(isVisible=True) # 유저 투명 처리 품
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        add_buff(boxIds=[2001], skillId=99910400, level=1, arg4=False, arg5=True) # 클라디아 변신
        add_buff(boxIds=[2001], skillId=99910400, level=1, arg4=False, arg5=False) # 클라디아 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_6()


class CameraEffect03_6(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_7()


class CameraEffect03_7(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004612, msg='$52100205_QD__52100205__2$', align='left', illustId='cladia_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CameraEffect03_8()


class CameraEffect03_8(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2002]):
            return 제시카_01()


class 제시카_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 제시카_02()


class 제시카_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        create_monster(spawnIds=[101]) # 제시카

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 제시카_03()


class 제시카_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제시카_04()


class 제시카_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 제시카_05()


class 제시카_05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11004575, msg='$52100205_QD__52100205__3$', align='left', illustId='Jessica_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 제시카_06()


class 제시카_06(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 제시카_07()


class 제시카_07(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)


