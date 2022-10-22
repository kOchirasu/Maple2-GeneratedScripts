""" trigger/52000037_qd/lookinto_knight_03.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        set_onetime_effect(id=5, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[60100070], questStates=[3], jobCode=10):
            return Quit()
        if quest_user_detected(boxIds=[9900], questIds=[60100070], questStates=[2], jobCode=10):
            return Quit()
        if quest_user_detected(boxIds=[9900], questIds=[60100070], questStates=[1], jobCode=10):
            return LoadingDelay02()
        if quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[3], jobCode=10):
            return DefaultSetting02()
        if quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[2], jobCode=10):
            return LoadingDelay01()


class LoadingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk01()


class CameraWalk01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera(triggerId=800, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk02()


class CameraWalk02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk03()


class CameraWalk03(state.State):
    def on_enter(self):
        select_camera(triggerId=801, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk04()


class CameraWalk04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraShot01()


class CameraShot01(state.State):
    def on_enter(self):
        select_camera(triggerId=802, enable=True)
        set_onetime_effect(id=3, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return CameraShot02()


class CameraShot02(state.State):
    def on_enter(self):
        select_camera(triggerId=803, enable=True)
        set_onetime_effect(id=4, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return CameraShot03()


class CameraShot03(state.State):
    def on_enter(self):
        select_camera(triggerId=804, enable=True)
        set_onetime_effect(id=5, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraFadeIn01()


class CameraFadeIn01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraFadeOut01()


class CameraFadeOut01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera(triggerId=804, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefaultSetting02()


class DefaultSetting02(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[101], arg2=False) # NelfDummyNPC

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[60100070], questStates=[1]):
            return LoadingDelay02()


class LoadingDelay02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[501], arg2=False) # 의문의남자

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LoadingDelay03()


class LoadingDelay03(state.State):
    def on_enter(self):
        move_user(mapId=52000037, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FindDoor01()


class FindDoor01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_1200')
        select_camera(triggerId=810, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FindDoor02()


class FindDoor02(state.State):
    def on_enter(self):
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)
        move_npc(spawnId=501, patrolName='MS2PatrolData_500') # 의문의남자

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FindDoor03()


class FindDoor03(state.State):
    def on_enter(self):
        select_camera(triggerId=811, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Chase01()


class Chase01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=100, arg4=200, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Chase02()


class Chase02(state.State):
    def on_enter(self):
        move_npc(spawnId=501, patrolName='MS2PatrolData_501') # 의문의남자

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9500, spawnIds=[501]):
            return Chase03()


class Chase03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[501])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=811, enable=False)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000037_QD__LOOKINTO_KNIGHT_03__0$', arg3='3000', arg4='0')


class Quit(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


