""" trigger/52010037_qd/52010037.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=False) # 콘대르
        self.create_monster(spawnIds=[202], animationEffect=False) # 샤텐
        self.create_monster(spawnIds=[203], animationEffect=False) # 네이린
        self.create_monster(spawnIds=[204], animationEffect=False) # 메이슨
        self.create_monster(spawnIds=[205], animationEffect=False) # 블랙아이
        self.create_monster(spawnIds=[206], animationEffect=False) # 알론
        self.create_monster(spawnIds=[207], animationEffect=False) # 프레이
        self.create_monster(spawnIds=[208], animationEffect=False) # 오스칼
        self.set_actor(triggerId=501, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=502, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=503, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=504, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=505, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=506, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=507, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=508, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=509, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=510, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=511, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=512, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=513, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=514, visible=True, initialSequence='sf_quest_light_A01_Off')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000003], questStates=[2]):
            return 지하기지전경씬01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000013], questStates=[1]):
            self.move_user(mapId=52010038, portalId=1)
            return None
        if self.quest_user_detected(boxIds=[9001], questIds=[91000013], questStates=[2]):
            self.move_user(mapId=52010039, portalId=1)
            return None
        if self.quest_user_detected(boxIds=[9001], questIds=[91000004], questStates=[2]):
            self.create_monster(spawnIds=[200], animationEffect=False)
            return 블리체와대장들이동(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000010], questStates=[3]):
            return 긴급상황발동01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000004], questStates=[3]):
            self.create_monster(spawnIds=[200], animationEffect=False)
            return 블리체와대장들이동(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000003], questStates=[3]):
            return 블리체함장등장(self.ctx)


# ########################지하기지 전경씬########################
class 지하기지전경씬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 지하기지전경씬02(self.ctx)


class 지하기지전경씬02(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Quit01, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[3000,3001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 지하기지전경씬02_b(self.ctx)


class 지하기지전경씬02_b(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3002,3003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 지하기지전경씬02_c(self.ctx)


class 지하기지전경씬02_c(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[3004,3005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 지하기지전경씬03(self.ctx)


class 지하기지전경씬03(trigger_api.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52010037_QD__52010037__0$', desc='$52010037_QD__52010037__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)
        self.select_camera_path(pathIds=[3006,3007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 지하기지전경씬04(self.ctx)


class 지하기지전경씬04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000003], questStates=[3]):
            return 블리체함장등장(self.ctx)


# ########################지하기지 전경씬########################
class 블리체함장등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False) # 블리체
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_bliche_come') # 블리체 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000004], questStates=[2]):
            return 블리체와대장들이동(self.ctx)


class 블리체와대장들이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_bliche_go') # 블리체 이동
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_blackEye') # 블랙아이 이동
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_alon') # 알론 이동
        self.move_npc(spawnId=207, patrolName='MS2PatrolData_pray') # 프레이 이동
        self.move_npc(spawnId=208, patrolName='MS2PatrolData_oscal') # 오스칼 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000010], questStates=[3]):
            return 긴급상황발동01(self.ctx)


class 긴급상황발동01(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9010, enable=True) # 케이틀린 등장 브금
        self.set_ambient_light(primary=[232,92,53])
        self.set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_actor(triggerId=501, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=502, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=503, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=504, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=505, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=506, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=507, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=508, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=509, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=510, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=511, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=512, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=513, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=514, visible=True, initialSequence='sf_quest_light_A01_On')
        self.destroy_monster(spawnIds=[204]) # 메이슨 삭제
        self.destroy_monster(spawnIds=[200]) # 블리체 삭제
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_conder_come') # 콘대르 이동
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_shatten_come') # 샤텐 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 긴급상황발동02(self.ctx)


class 긴급상황발동02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_monster(spawnIds=[209], animationEffect=False) # 프레이
        self.create_monster(spawnIds=[210], animationEffect=False) # 오스칼


initial_state = Wait
