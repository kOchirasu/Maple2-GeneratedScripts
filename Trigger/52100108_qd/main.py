""" trigger/52100108_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000360], questStates=[1]):
            return wait_01(self.ctx)


class wait_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(triggerIds=[6000], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_03(self.ctx)


class wait_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52100108, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 들어왔다(self.ctx)


class 들어왔다(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 들어왔다_02(self.ctx)


class 들어왔다_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4006,4005], returnView=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__0$', duration=3000)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 들어왔다_03(self.ctx)


class 들어왔다_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004,4003], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__1$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 제어기기(self.ctx)


class 제어기기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 들킴(self.ctx)


class 들킴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=[232,92,53])
        self.set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_effect(triggerIds=[6000], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')
        self.add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__4$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 들킴_02(self.ctx)


class 들킴_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.add_cinematic_talk(npcId=25022107, msg='$52100108_QD__MAIN__5$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 들킴_03(self.ctx)


class 들킴_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__7$', duration=3000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 정리_01(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_effect(triggerIds=[6000], visible=False)
        self.set_effect(triggerIds=[6000], visible=True)
        self.set_ambient_light(primary=[232,92,53])
        self.set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 정리_02(self.ctx)


class 정리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 경보끝_01(self.ctx)


class 경보끝_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6000], visible=False)
        self.set_ambient_light(primary=[131,160,209])
        self.set_directional_light(diffuseColor=[134,160,143], specularColor=[130,130,130])
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')


initial_state = Ready
