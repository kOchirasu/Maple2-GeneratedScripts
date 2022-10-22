""" trigger/52100108_qd/main.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000360], questStates=[1]):
            return wait_01()


class wait_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_effect(triggerIds=[6000], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_03()


class wait_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        move_user(mapId=52100108, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 들어왔다()


class 들어왔다(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 들어왔다_02()


class 들어왔다_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006,4005], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__0$', duration=3000)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 들어왔다_03()


class 들어왔다_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004,4003], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__1$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 제어기기()


class 제어기기(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__2$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 들킴()


class 들킴(state.State):
    def on_enter(self):
        set_ambient_light(primary=[232,92,53])
        set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        create_monster(spawnIds=[101], arg2=False)
        set_effect(triggerIds=[6000], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')
        add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__4$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 들킴_02()


class 들킴_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        add_cinematic_talk(npcId=25022107, msg='$52100108_QD__MAIN__5$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 들킴_03()


class 들킴_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52100108_QD__MAIN__7$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리_01()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[101], arg2=False)
        set_effect(triggerIds=[6000], visible=False)
        set_effect(triggerIds=[6000], visible=True)
        set_ambient_light(primary=[232,92,53])
        set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 정리_02()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class 밝아짐(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 경보끝_01()


class 경보끝_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=False)
        set_ambient_light(primary=[131,160,209])
        set_directional_light(diffuseColor=[134,160,143], specularColor=[130,130,130])
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')


