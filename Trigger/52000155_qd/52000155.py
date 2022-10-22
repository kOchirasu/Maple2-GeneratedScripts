""" trigger/52000155_qd/52000155.xml """
from common import *
import state


class wait_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001,5002], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002728], questStates=[3]):
            return 전직하러_01()
        if quest_user_detected(boxIds=[2002], questIds=[40002725], questStates=[3]):
            return 가이드_01()
        if user_detected(boxIds=[2002]):
            return wait_02()


class wait_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_03()


class wait_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        move_user(mapId=52000155, portalId=6001)
        select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 빅스제시_01()


class 빅스제시_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 정리_01()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 밝아짐()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class 밝아짐(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002725], questStates=[2]):
            return 만취상태()


class 만취상태(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000155_QD__52000155__0$', arg3=False)
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 만취상태_01()


class 만취상태_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        destroy_monster(spawnIds=[108])
        destroy_monster(spawnIds=[109])
        set_npc_emotion_loop(spawnId=105, sequenceName='Down_Idle_A', duration=90000000)
        set_npc_emotion_loop(spawnId=106, sequenceName='Down_Idle_A', duration=90000000)
        move_user(mapId=52000155, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 정리2_02()


class 정리2_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리2_03()


class 정리2_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002726], questStates=[2]):
            return 가이드_01()


class 가이드_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001,5002], visible=True)
        destroy_monster(spawnIds=[110])
        create_monster(spawnIds=[107], arg2=False)
        show_guide_summary(entityId=25201551, textId=25201551, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002727], questStates=[2]):
            return 가이드_02()


class 가이드_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001,5002], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[40002728], questStates=[2]):
            return 전직하러_01()


class 전직하러_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 전직하러_02()


class 전직하러_02(state.State):
    def on_enter(self):
        move_user(mapId=52000157, portalId=6003)


