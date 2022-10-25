""" trigger/52000061_qd/playmusic01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # PlayPiano
        self.set_effect(triggerIds=[5001], visible=False) # PlayGuitar
        self.set_effect(triggerIds=[5002], visible=False) # PlayClarinet
        self.set_effect(triggerIds=[5003], visible=False) # PlayCello
        self.set_effect(triggerIds=[5004], visible=False) # PlayViolin
        self.set_effect(triggerIds=[5100], visible=False) # SpotLight
        self.set_effect(triggerIds=[5200], visible=False) # Applause
        self.set_sound(triggerId=10000, enable=False) # PlayMusic
        self.create_monster(spawnIds=[101,201,202,203,204], animationEffect=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000550], questStates=[1]):
            return LodingDelay01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000550], questStates=[2]):
            return Quit(self.ctx)


class LodingDelay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCWalkInStage01(self.ctx)


class PCWalkInStage01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000061, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PCWalkInStage02(self.ctx)


class PCWalkInStage02(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1000')
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PCWalkInStage03(self.ctx)


class PCWalkInStage03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[601,602], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return PCWalkInStage04(self.ctx)


class PCWalkInStage04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=603, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PCBow01(self.ctx)


class PCBow01(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Chin_Chin_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return PCBow02(self.ctx)


class PCBow02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCBow03(self.ctx)


class PCBow03(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1)
        self.select_camera(triggerId=610, enable=True)
        self.move_user(mapId=52000061, portalId=20)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCReadyToPlayThePiano01(self.ctx)


class PCReadyToPlayThePiano01(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Music_Piano_Idle_A', duration=31500)
        self.set_effect(triggerIds=[5100], visible=True) # SpotLight

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PCPlayMusic01(self.ctx)


class PCPlayMusic01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_sound(triggerId=10000, enable=True) # PlayMusic

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PCPlayMusic02(self.ctx)


class PCPlayMusic02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # PlayPiano
        self.set_effect(triggerIds=[5001], visible=True) # PlayGuitar
        self.set_effect(triggerIds=[5002], visible=True) # PlayClarinet
        self.set_effect(triggerIds=[5003], visible=True) # PlayCello
        self.set_effect(triggerIds=[5004], visible=True) # PlayViolin
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Play_A', duration=30500)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Play_A', duration=30500)
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Play_A', duration=30500)
        self.set_npc_emotion_loop(spawnId=204, sequenceName='Play_A', duration=30500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30500):
            return PCPlayMusic03(self.ctx)


class PCPlayMusic03(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=10000, enable=False) # PlayMusic
        self.set_effect(triggerIds=[5000], visible=False) # PlayPiano
        self.set_effect(triggerIds=[5001], visible=False) # PlayGuitar
        self.set_effect(triggerIds=[5002], visible=False) # PlayClarinet
        self.set_effect(triggerIds=[5003], visible=False) # PlayCello
        self.set_effect(triggerIds=[5004], visible=False) # PlayViolin
        self.set_effect(triggerIds=[5200], visible=True) # Applause

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PCPlayQuit01(self.ctx)


class PCPlayQuit01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[5100], visible=False) # SpotLight

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return PCPlayQuit02(self.ctx)


class PCPlayQuit02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000061, portalId=30)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCPlayQuit03(self.ctx)


class PCPlayQuit03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.set_achievement(triggerId=9900, type='trigger', achieve='PerformanceWithNPC')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000550], questStates=[3]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
