""" trigger/52000157_qd/52000157.xml """
from common import *
import state


class wait_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001,5002], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[2]):
            return 이별준비()
        if quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[3]):
            return 프론티아재단으로_01()
        if user_detected(boxIds=[2002]):
            return 전직컷씬01()


class 전직컷씬01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='jobChange_thief.swf', movieId=1)
        create_monster(spawnIds=[107], arg2=False)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 정산끝()
        if wait_tick(waitTick=8000):
            return 정산끝()


class 정산끝(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002728], questStates=[3]):
            return 전직이펙트_01()


class 전직이펙트_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전직이펙트_02()


class 전직이펙트_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 떠나기전준비()


class 떠나기전준비(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[2]):
            return 이별준비()


class 이별준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이별준비_01()


class 이별준비_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        destroy_monster(spawnIds=[107])
        destroy_monster(spawnIds=[105])
        destroy_monster(spawnIds=[106])
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        move_user(mapId=52000157, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이별준비_02()


class 이별준비_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이별준비_03()


class 이별준비_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002731], questStates=[3]):
            return 프론티아재단으로_01()


class 프론티아재단으로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 프론티아재단으로_02()


class 프론티아재단으로_02(state.State):
    def on_enter(self):
        move_user(mapId=52000186, portalId=1)


