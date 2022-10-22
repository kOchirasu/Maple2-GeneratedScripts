""" trigger/52010037_qd/52010037.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=False) # 콘대르
        create_monster(spawnIds=[202], arg2=False) # 샤텐
        create_monster(spawnIds=[203], arg2=False) # 네이린
        create_monster(spawnIds=[204], arg2=False) # 메이슨
        create_monster(spawnIds=[205], arg2=False) # 블랙아이
        create_monster(spawnIds=[206], arg2=False) # 알론
        create_monster(spawnIds=[207], arg2=False) # 프레이
        create_monster(spawnIds=[208], arg2=False) # 오스칼
        set_actor(triggerId=501, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=502, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=503, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=504, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=505, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=506, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=507, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=508, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=509, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=510, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=511, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=512, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=513, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=514, visible=True, initialSequence='sf_quest_light_A01_Off')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000003], questStates=[2]):
            return 지하기지전경씬01()
        if quest_user_detected(boxIds=[9001], questIds=[91000013], questStates=[1]):
            move_user(mapId=52010038, portalId=1)
            return None
        if quest_user_detected(boxIds=[9001], questIds=[91000013], questStates=[2]):
            move_user(mapId=52010039, portalId=1)
            return None
        if quest_user_detected(boxIds=[9001], questIds=[91000004], questStates=[2]):
            create_monster(spawnIds=[200], arg2=False)
            return 블리체와대장들이동()
        if quest_user_detected(boxIds=[9001], questIds=[91000010], questStates=[3]):
            return 긴급상황발동01()
        if quest_user_detected(boxIds=[9001], questIds=[91000004], questStates=[3]):
            create_monster(spawnIds=[200], arg2=False)
            return 블리체와대장들이동()
        if quest_user_detected(boxIds=[9001], questIds=[91000003], questStates=[3]):
            return 블리체함장등장()


#  ########################지하기지 전경씬########################
class 지하기지전경씬01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 지하기지전경씬02()


class 지하기지전경씬02(state.State):
    def on_enter(self):
        set_scene_skip(state=Quit01, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 지하기지전경씬02_b()


class 지하기지전경씬02_b(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3002,3003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 지하기지전경씬02_c()


class 지하기지전경씬02_c(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3004,3005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 지하기지전경씬03()


class 지하기지전경씬03(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52010037_QD__52010037__0$', desc='$52010037_QD__52010037__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)
        select_camera_path(pathIds=[3006,3007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 지하기지전경씬04()


class 지하기지전경씬04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000003], questStates=[3]):
            return 블리체함장등장()


#  ########################지하기지 전경씬########################
class 블리체함장등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False) # 블리체
        move_npc(spawnId=200, patrolName='MS2PatrolData_bliche_come') # 블리체 이동

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000004], questStates=[2]):
            return 블리체와대장들이동()


class 블리체와대장들이동(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_bliche_go') # 블리체 이동
        move_npc(spawnId=205, patrolName='MS2PatrolData_blackEye') # 블랙아이 이동
        move_npc(spawnId=206, patrolName='MS2PatrolData_alon') # 알론 이동
        move_npc(spawnId=207, patrolName='MS2PatrolData_pray') # 프레이 이동
        move_npc(spawnId=208, patrolName='MS2PatrolData_oscal') # 오스칼 이동

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000010], questStates=[3]):
            return 긴급상황발동01()


class 긴급상황발동01(state.State):
    def on_enter(self):
        set_sound(triggerId=9010, arg2=True) # 케이틀린 등장 브금
        set_ambient_light(primary=[232,92,53])
        set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_actor(triggerId=501, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=502, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=503, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=504, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=505, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=506, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=507, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=508, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=509, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=510, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=511, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=512, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=513, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=514, visible=True, initialSequence='sf_quest_light_A01_On')
        destroy_monster(spawnIds=[204]) # 메이슨 삭제
        destroy_monster(spawnIds=[200]) # 블리체 삭제
        move_npc(spawnId=201, patrolName='MS2PatrolData_conder_come') # 콘대르 이동
        move_npc(spawnId=202, patrolName='MS2PatrolData_shatten_come') # 샤텐 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 긴급상황발동02()


class 긴급상황발동02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        create_monster(spawnIds=[209], arg2=False) # 프레이
        create_monster(spawnIds=[210], arg2=False) # 오스칼


