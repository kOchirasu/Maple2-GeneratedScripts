""" trigger/52100105_qd/52100105_02.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[50101030], questStates=[3]):
            return wait_03()
        if quest_user_detected(boxIds=[2002], questIds=[50101020], questStates=[2]):
            return wait_03()


class wait_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출보러()


class 연출보러(state.State):
    def on_enter(self):
        move_user(mapId=52100105, portalId=4)


