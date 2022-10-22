""" trigger/52020030_qd/main30000332.xml """
from common import *
import state


#  천공의 탑 입장 
class 입장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[30000332], questStates=[1]):
            return 천공의탑전경보여주기()


class 천공의탑전경보여주기(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 천공의탑전경보여주기02()


class 천공의탑전경보여주기02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4008,4010], returnView=False)
        show_caption(type='VerticalCaption', title='천공의 탑', desc='크리티아스 마법 연구소', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 천공의탑전경보여주기03()


class 천공의탑전경보여주기03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52020030, portalId=6006)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 천공의탑전경보여주기04()


class 천공의탑전경보여주기04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


