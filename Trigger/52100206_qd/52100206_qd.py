""" trigger/52100206_qd/52100206_qd.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            visible_my_pc(isVisible=False)
            create_monster(spawnIds=[2003], arg2=False)
            set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052,4053,4054,4055,4056,4057,4058,4059,4060,4061,4062,4063,4064,4065,4066,4067,4068,4069,4070,4071], visible=False, arg3=0, arg4=0, arg5=0)
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1006,1002,1005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return CameraEffect04()


class CameraEffect04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1005,1003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return CameraEffect05()


class CameraEffect05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1004], returnView=False)
        create_monster(spawnIds=[2002], arg2=False) # 더미 벨라

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraEffect06()


class CameraEffect06(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 버프부여()


class 버프부여(state.State):
    def on_enter(self):
        set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        visible_my_pc(isVisible=True) # 유저 투명 처리
        destroy_monster(spawnIds=[2002])
        add_buff(boxIds=[101], skillId=99910280, level=1, arg4=False, arg5=True) # 벨라 변신
        add_buff(boxIds=[101], skillId=99910280, level=1, arg4=False, arg5=False) # 벨라 변신
        show_guide_summary(entityId=25201503, textId=25201503, duration=10000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9010]):
            return 마법다리형성()


class 마법다리형성(state.State):
    def on_enter(self):
        set_local_camera(cameraId=1006, enable=True) # LocalTargetCamera
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052,4053,4054,4055,4056,4057,4058,4059,4060,4061,4062,4063,4064,4065,4066,4067,4068,4069,4070,4071], visible=True, arg3=1000, arg4=160, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9020]):
            return 검마걸어나오는연출01()


class 검마걸어나오는연출01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 검마걸어나오는연출02()


class 검마걸어나오는연출02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera(triggerId=1007, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 검마걸어나오는연출03()


class 검마걸어나오는연출03(state.State):
    def on_enter(self):
        move_npc(spawnId=2003, patrolName='MS2PatrolData_2000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 검마걸어나오는연출04()


class 검마걸어나오는연출04(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 검마걸어나오는연출05()


class 검마걸어나오는연출05(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_local_camera(cameraId=1005, enable=True) # LocalTargetCamera

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[10003390], questStates=[3]):
            return 완료연출01()


class 완료연출01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료연출02()


class 완료연출02(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        move_user(mapId=52000087, portalId=1)


