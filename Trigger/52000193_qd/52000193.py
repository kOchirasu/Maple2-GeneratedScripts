""" trigger/52000193_qd/52000193.xml """
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
        create_monster(spawnIds=[202])
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02_01()


class CameraEffect02_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003406], questStates=[2]):
            return CameraEffect02_02()
        if quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[3]):
            return 이동()
        if quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[2]):
            return 변신_02()
        if not quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[2]):
            return 변신_02()


class CameraEffect02_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000193_QD__52000193__0$')

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
        if wait_tick(waitTick=1000):
            return CameraEffect03_3()


class CameraEffect03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        show_caption(type='VerticalCaption', title='$52000193_QD__52000193__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraEffect03_4()


class CameraEffect03_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 변신_01()


class 변신_01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[201])
        visible_my_pc(isVisible=True) # 유저 투명 처리 품
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=True) # 에레브 변신
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=False) # 에레브 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraEffect03_6()


class 변신_02(state.State):
    def on_enter(self):
        move_user(mapId=52000193, portalId=5002)
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[201])
        visible_my_pc(isVisible=True) # 유저 투명 처리 품
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=True) # 에레브 변신
        add_buff(boxIds=[2001], skillId=99910402, level=1, arg4=False, arg5=False) # 에레브 변신

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraEffect03_6()


class CameraEffect03_6(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_8()


class CameraEffect03_8(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[3]):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        move_user(mapId=2000065, portalId=0)


