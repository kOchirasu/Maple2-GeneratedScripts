""" trigger/52010057_qd/main.xml """
from common import *
import state


class 연출01(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            visible_my_pc(isVisible=False)
            set_mesh_animation(triggerIds=[9002], visible=False, arg3=0, arg4=0)
            set_cinematic_ui(type=1)
            return 연출02()


class 연출02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출03()


class 연출03(state.State):
    def on_enter(self):
        set_time_scale(enable=True, startScale=0.8, endScale=0.8, duration=8, interpolator=1) # 2초간 느려지기 시작
        select_camera_path(pathIds=[2000,2001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출04_b()


class 연출04_b(state.State):
    def on_enter(self):
        set_mesh_animation(triggerIds=[9002], visible=True, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출04()


class 연출04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출05()


class 연출05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2002,2003,2004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출06()


class 연출06(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return quit()


class quit(state.State):
    def on_enter(self):
        move_user(mapId=2000422, portalId=3)


