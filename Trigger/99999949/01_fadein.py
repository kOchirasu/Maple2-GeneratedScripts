""" trigger/99999949/01_fadein.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # mask_black

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return Guide()


class Guide(state.State):
    def on_enter(self):
        debug_string(string='1번 영역에 들어가면 화면 페이드인 트리거가 시작됩니다.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        debug_string(string='fadein')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5000], visible=True) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        debug_string(string='fadeout')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[5000], visible=False) # mask_black

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        debug_string(string='3초 후에 트리거가 리셋됩니다. 1번 영역 밖으로 나가세요.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


