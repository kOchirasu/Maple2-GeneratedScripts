""" trigger/52000061_qd/playmusic01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # PlayPiano
        set_effect(triggerIds=[5001], visible=False) # PlayGuitar
        set_effect(triggerIds=[5002], visible=False) # PlayClarinet
        set_effect(triggerIds=[5003], visible=False) # PlayCello
        set_effect(triggerIds=[5004], visible=False) # PlayViolin
        set_effect(triggerIds=[5100], visible=False) # SpotLight
        set_effect(triggerIds=[5200], visible=False) # Applause
        set_sound(triggerId=10000, arg2=False) # PlayMusic
        create_monster(spawnIds=[101,201,202,203,204], arg2=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000550], questStates=[1]):
            return LodingDelay01()
        if quest_user_detected(boxIds=[9900], questIds=[90000550], questStates=[2]):
            return Quit()


class LodingDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LodingDelay02()


class LodingDelay02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCWalkInStage01()


class PCWalkInStage01(state.State):
    def on_enter(self):
        move_user(mapId=52000061, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCWalkInStage02()


class PCWalkInStage02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCWalkInStage03()


class PCWalkInStage03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[601,602], returnView=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return PCWalkInStage04()


class PCWalkInStage04(state.State):
    def on_enter(self):
        select_camera(triggerId=603, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCBow01()


class PCBow01(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Chin_Chin_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return PCBow02()


class PCBow02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCBow03()


class PCBow03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        select_camera(triggerId=610, enable=True)
        move_user(mapId=52000061, portalId=20)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCReadyToPlayThePiano01()


class PCReadyToPlayThePiano01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Music_Piano_Idle_A', duration=31500)
        set_effect(triggerIds=[5100], visible=True) # SpotLight

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCPlayMusic01()


class PCPlayMusic01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_sound(triggerId=10000, arg2=True) # PlayMusic

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCPlayMusic02()


class PCPlayMusic02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # PlayPiano
        set_effect(triggerIds=[5001], visible=True) # PlayGuitar
        set_effect(triggerIds=[5002], visible=True) # PlayClarinet
        set_effect(triggerIds=[5003], visible=True) # PlayCello
        set_effect(triggerIds=[5004], visible=True) # PlayViolin
        set_npc_emotion_loop(spawnId=201, sequenceName='Play_A', duration=30500)
        set_npc_emotion_loop(spawnId=202, sequenceName='Play_A', duration=30500)
        set_npc_emotion_loop(spawnId=203, sequenceName='Play_A', duration=30500)
        set_npc_emotion_loop(spawnId=204, sequenceName='Play_A', duration=30500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30500):
            return PCPlayMusic03()


class PCPlayMusic03(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=False) # PlayMusic
        set_effect(triggerIds=[5000], visible=False) # PlayPiano
        set_effect(triggerIds=[5001], visible=False) # PlayGuitar
        set_effect(triggerIds=[5002], visible=False) # PlayClarinet
        set_effect(triggerIds=[5003], visible=False) # PlayCello
        set_effect(triggerIds=[5004], visible=False) # PlayViolin
        set_effect(triggerIds=[5200], visible=True) # Applause

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCPlayQuit01()


class PCPlayQuit01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5100], visible=False) # SpotLight

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PCPlayQuit02()


class PCPlayQuit02(state.State):
    def on_enter(self):
        move_user(mapId=52000061, portalId=30)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCPlayQuit03()


class PCPlayQuit03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        set_achievement(triggerId=9900, type='trigger', achieve='PerformanceWithNPC')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000550], questStates=[3]):
            return Quit()


class Quit(state.State):
    pass


