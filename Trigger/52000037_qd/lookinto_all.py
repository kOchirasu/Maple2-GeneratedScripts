""" trigger/52000037_qd/lookinto_all.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[60100070], questStates=[3]):
            # 초보자 넬프의 죽음 퀘스트 완료
            return Quit(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[60100070], questStates=[2]):
            # 초보자 넬프의 죽음 퀘스트 완료 가능
            return Quit(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[60100070], questStates=[1]):
            # 초보자 넬프의 죽음 퀘스트 수락
            return LoadingDelay02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[3]):
            # 초보자 랄프의 정보 퀘스트 완료
            return DefaultSetting02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[2]):
            # 초보자 랄프의 정보 퀘스트 완료 가능
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(triggerId=800, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk02(self.ctx)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk03(self.ctx)


class CameraWalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=801, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk04(self.ctx)


class CameraWalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraShot01(self.ctx)


class CameraShot01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=802, enable=True)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return CameraShot02(self.ctx)


class CameraShot02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=803, enable=True)
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return CameraShot03(self.ctx)


class CameraShot03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=804, enable=True)
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraFadeIn01(self.ctx)


class CameraFadeIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraFadeOut01(self.ctx)


class CameraFadeOut01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(triggerId=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefaultSetting02(self.ctx)


class DefaultSetting02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[101], animationEffect=False) # NelfDummyNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[60100070], questStates=[1]):
            # 초보자 넬프의 죽음 퀘스트 수락
            return LoadingDelay02(self.ctx)


class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[501], animationEffect=False) # 의문의남자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LoadingDelay03(self.ctx)


class LoadingDelay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000037, portalId=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FindDoor01(self.ctx)


class FindDoor01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='MS2PatrolData_1200')
        self.select_camera(triggerId=810, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FindDoor02(self.ctx)


class FindDoor02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True)
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_500') # 의문의남자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return FindDoor03(self.ctx)


class FindDoor03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=811, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Chase01(self.ctx)


class Chase01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=100, delay=200, scale=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Chase02(self.ctx)


class Chase02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_501') # 의문의남자

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9500, spawnIds=[501]):
            return Chase03(self.ctx)


class Chase03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=811, enable=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000037_QD__LOOKINTO_PRIEST_06__0$', arg3='3000', arg4='0')


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = Wait
