""" trigger/52000190_qd/52000190.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003420], questStates=[2]):
            return Wait_02()


class Wait_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000190, portalId=5001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='the_empress_of_a_dungeon.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=13000):
            return 영상재생_end()


class 영상재생_end(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 영상재생_end02()


class 영상재생_end02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


