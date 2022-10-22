""" trigger/52000046_qd/main_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[60100220], questStates=[1]):
            return ready()


#  이벤트 시작 
class ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=scene_10, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        move_user(mapId=52000046, portalId=6001)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__0$', duration=3735, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__1$', duration=2000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__2$', duration=2000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003215, msg='$52000046_QD__MAIN_01__3$', duration=2000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$52000046_QD__MAIN_01__4$', duration=3000)
        create_monster(spawnIds=[201], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return scene_09()


class scene_09(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_10()

    def on_exit(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/Eff_jump_Landing.xml')


class scene_10(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='lenonn')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return warp()


class warp(state.State):
    def on_enter(self):
        move_user(mapId=52000127, portalId=1)


