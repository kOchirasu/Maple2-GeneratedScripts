""" trigger/52020031_qd/main30000332.xml """
import trigger_api


# 제단 입장
# 예상치 못한 인물 하렌(11003747) - spawnpoint : 1 
# 한순간의 방심 하렌(11003749) - spawnpoint : 2
# 연출용 하렌(11003756) - spawnpoint : 101
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[30000332], questStates=[1]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_02(self.ctx)


class 연출시작_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52020031, portalId=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 제단보여주기(self.ctx)


class 제단보여주기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005,4001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='천공의 제단', desc='천공의 심장의 보관소', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)
        self.set_scene_skip(state=끝, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 다음스타트(self.ctx)


class 다음스타트(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=0, msg='이곳이 천공의 심장이 보관되어 있다는 곳이구나.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3200):
            return 제단확인(self.ctx)


class 제단확인(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4005,4009], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제단관찰(self.ctx)


class 제단관찰(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=0, msg='누군가 이미 들어온 흔적이 있어 보였는데... 기분 탓인가...', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='저 벽에 있는 장치에 천공의 심장이 보관 되어있는 거겠지?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 제단관찰_02(self.ctx)


class 제단관찰_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4011], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='...어라? 천공의 심장으로 보이는 물건이 없는 것 같은데... ', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 제단관찰_02_1(self.ctx)


class 제단관찰_02_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 제단관찰_03(self.ctx)


class 제단관찰_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 제단관찰_04(self.ctx)


class 제단관찰_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=0, msg='가까이 가봐도 되려나..?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 부시럭(self.ctx)


class 부시럭(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부시럭_02(self.ctx)


class 부시럭_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003756, msg='어머? 이게 누구야?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 하렌발견01(self.ctx)


class 하렌발견01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006,4007], returnView=False)
        self.add_cinematic_talk(npcId=11003756, msg='설마 했는데... 너였구나?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 하렌발견01_2(self.ctx)


class 하렌발견01_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 하렌발견01_3(self.ctx)


class 하렌발견01_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003756, msg='많이 늦었네?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 하렌발견02(self.ctx)


class 하렌발견02(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0.1)
        self.add_cinematic_talk(npcId=0, msg='아니, 너는?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 하렌발견03(self.ctx)


class 하렌발견03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.show_caption(type='VerticalCaption', title='하렌', desc='흑성회의 제 3 간부', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003756, msg='...이렇게 만나다니 우연이네.', duration=3000)
        self.add_cinematic_talk(npcId=11003756, msg='혼자 이것저것 하기 힘들지? 후후.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020031, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 하렌등장2(self.ctx)


class 하렌등장2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Music_Cello_Play_03_A')
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='어떻게 여기에... 네가?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(triggerId=2001, type='trigger', achieve='MeetHaren')
        self.create_monster(spawnIds=[102], animationEffect=False) # 퀘스트 하렌
        self.destroy_monster(spawnIds=[101])
        self.reset_camera(interpolationTime=0.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 끝02(self.ctx)


class 끝02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[101])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
