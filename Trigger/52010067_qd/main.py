""" trigger/52010067_qd/main.xml """
from common import *
import state


class 연출01(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            visible_my_pc(isVisible=False)
            set_cinematic_ui(type=1)
            set_effect(triggerIds=[9010], visible=False)
            return 연출브릿지()


class 연출브릿지(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[700], questIds=[20002290], questStates=[2]):
            return 조준씬01()
        if quest_user_detected(boxIds=[700], questIds=[20002290], questStates=[3]):
            return 피격씬01()


#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@포신정렬씬@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
class 조준씬01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False) # 인페르녹

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출02_b()


class 연출02_b(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1300):
            return 연출02_c()


class 연출02_c(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000,2001,2002,2003,2004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return 연출03()


class 연출03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2005,2006,2007,2008,2009,2010,2011], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3200):
            return 연출04()


class 연출04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2012], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출05()


class 연출05(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return quit()


class quit(state.State):
    def on_enter(self):
        move_user(mapId=2000422, portalId=3)


#  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@피격씬@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
class 피격씬01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 피격씬01_a()


class 피격씬01_a(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1300):
            return 피격씬02()


class 피격씬02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[9010], visible=True)
        select_camera_path(pathIds=[3004,3005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 피격씬03_a()


class 피격씬03_a(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3900):
            return 피격씬03()


class 피격씬03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3002,3003], returnView=False)
        set_time_scale(enable=True, startScale=0.1, endScale=0.1, duration=3.5, interpolator=1) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3600):
            return 피격씬04()


class 피격씬04(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return quit02()


class quit02(state.State):
    def on_enter(self):
        move_user(mapId=2000422, portalId=3)


