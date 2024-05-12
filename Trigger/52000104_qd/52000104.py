""" trigger/52000104_qd/52000104.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[205], animationEffect=False) # 리에나플라워등장
        self.set_effect(triggerIds=[5300], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5301], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5302], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5303], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5304], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5305], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5311], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5312], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5313], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5314], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5315], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5316], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5317], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5400], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5401], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5402], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5403], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5404], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5405], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5406], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5407], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5408], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5409], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5410], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5411], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5412], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5413], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5414], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5415], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5416], visible=False) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10011]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000104, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\\JobIntro_Berserker.usm', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 리엔전경씬01(self.ctx)
        if self.wait_tick(waitTick=75000):
            return 리엔전경씬01(self.ctx)


class 리엔전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1000,1001], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 리엔전경씬01_B(self.ctx)


class 리엔전경씬01_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리엔전경씬02(self.ctx)


class 리엔전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1002,1003], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리엔전경씬03(self.ctx)


class 리엔전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000104_QD__52000104__0$', desc='$52000104_QD__52000104__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 리엔전경씬04(self.ctx)


class 리엔전경씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5300], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5301], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5302], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5303], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5304], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5305], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5311], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5312], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5313], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5314], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5315], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5316], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5317], visible=True) # 경로 안내
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.add_balloon_talk(spawnId=0, msg='$52000104_QD__52000104__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=25201041, textId=25201041, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10012]):
            return 리린과대화01(self.ctx)


# ########################씬2 리린 등장########################
class 리린과대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_user(mapId=52000104, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리린과대화02(self.ctx)


class 리린과대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Ririn_Go')
        self.select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 리린과대화03(self.ctx)


class 리린과대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[1006,1007], returnView=False)
        self.face_emotion(spawnId=200, emotionName='hello_Cait')
        self.show_caption(type='NameCaption', title='$52000104_QD__52000104__3$', desc='$52000104_QD__52000104__4$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 리린과대화04(self.ctx)


class 리린과대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리린과대화05(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolationTime=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리린과대화05(self.ctx)


class 리린과대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.set_effect(triggerIds=[5300], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5301], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5302], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5303], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5304], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5305], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5306], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5307], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5308], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5309], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5310], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5311], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5312], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5313], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5314], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5315], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5316], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5317], visible=False) # 경로 안내
        self.face_emotion(spawnId=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002316], questStates=[1]):
            return 꽃가꾸기퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002317], questStates=[1]):
            return 꽃섬멸퀘스트01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002317], questStates=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 할아버지등장씬01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002319], questStates=[1]):
            return 할아버지등장씬01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002319], questStates=[2]):
            return 할아버지등장씬01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002319], questStates=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 할아버지등장씬01(self.ctx)


class 꽃가꾸기퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=25201042, textId=25201042, duration=10000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Ririn_Go2') # 마드리아 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002317], questStates=[1]):
            return 꽃섬멸퀘스트01(self.ctx)


# ########################씬3 꽃 섬멸 퀘스트########################
class 꽃섬멸퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1006,1007], returnView=False)
        self.set_cinematic_ui(type=1)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Ririn_Go2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 꽃섬멸퀘스트02(self.ctx)


class 꽃섬멸퀘스트02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1006,1007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 꽃섬멸퀘스트03(self.ctx)


class 꽃섬멸퀘스트03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.create_monster(spawnIds=[200,201,202,203,204], animationEffect=False)
        self.set_sound(triggerId=9000, enable=True) # 코믹한 상황 브금
        self.add_balloon_talk(spawnId=0, msg='$52000104_QD__52000104__5$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=25201043, textId=25201043, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002317], questStates=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 할아버지등장씬01(self.ctx)


# ########################씬4 할아버지 등장########################
class 할아버지등장씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=9000, enable=False) # 코믹한 상황 브금
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[102], animationEffect=False) # 할아버지등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 할아버지등장씬02(self.ctx)


class 할아버지등장씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_ten_go')
        self.select_camera_path(pathIds=[1008,1009], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 할아버지등장씬03(self.ctx)


class 할아버지등장씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003175, illustId='Ten_normal', msg='$52000104_QD__52000104__6$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 할아버지등장씬04(self.ctx)


class 할아버지등장씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='NameCaption', title='$52000104_QD__52000104__7$', desc='$52000104_QD__52000104__8$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 할아버지등장씬04_1(self.ctx)


class 할아버지등장씬04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 할아버지등장씬05(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolationTime=1)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_ten_go')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 할아버지등장씬05(self.ctx)


class 할아버지등장씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_ririn_move') # 마드리아 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002319], questStates=[1]):
            return 대검바라보기01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002319], questStates=[2]):
            return 대검바라보기01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002319], questStates=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 수련장으로이동01(self.ctx)


# ########################씬5 대검 바라보기########################
class 대검바라보기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Ririn_Go3') # 리린 이동
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_ten_go2') # 텐 이동
        self.show_guide_summary(entityId=25201044, textId=25201044, duration=10000)
        self.set_effect(triggerIds=[5400], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5401], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5402], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5403], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5404], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5405], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5406], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5407], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5408], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5409], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5410], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5411], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5412], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5413], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5414], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5415], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5416], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002319], questStates=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 수련장으로이동01(self.ctx)


class 수련장으로이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5400], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5401], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5402], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5403], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5404], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5405], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5406], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5407], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5408], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5409], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5410], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5411], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5412], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5413], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5414], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5415], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5416], visible=False) # 경로 안내
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Ririn_Go') # 리린 이동
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_ten_exit') # 텐 이동
        self.add_balloon_talk(spawnId=0, msg='$52000104_QD__52000104__9$', duration=6000, delayTick=1000)
        self.add_balloon_talk(spawnId=101, msg='$52000104_QD__52000104__10$', duration=6000, delayTick=2500)
        self.show_guide_summary(entityId=25201045, textId=25201045, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=10013, spawnIds=[102]):
            return 수련장으로이동02(self.ctx)


class 수련장으로이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.destroy_monster(spawnIds=[102])


initial_state = Wait
