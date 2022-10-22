""" trigger/52000046_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[60100215], questStates=[2]):
            return ready()
        if quest_user_detected(boxIds=[199], questIds=[60100215], questStates=[3]):
            return scene_04()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False)
        destroy_monster(spawnIds=[1001,1002,2002])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return camera()


class camera(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002,4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='ChatUp_A')
        add_cinematic_talk(npcId=11003216, msg='$52000046_QD__MAIN__0$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        show_caption(scale=2.3, type='NameCaption', title='$52000046_QD__MAIN__1$', desc='$52000046_QD__MAIN__2$', align='centerLeft', offsetRateX=-0.15, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002,2002])
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=True)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return emd()


class emd(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


