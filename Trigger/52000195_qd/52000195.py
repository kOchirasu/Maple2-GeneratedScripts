""" trigger/52000195_qd/52000195.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[1]):
            # 여제의 꿈 퀘스트 진행 유저
            return CameraEffect01(self.ctx)
        if not self.quest_user_detected(boxIds=[2001], questIds=[10003407], questStates=[1]):
            # 여제의 꿈 퀘스트 진행 유저가 아니면 이동
            return 이동(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[204]) # 에레브
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000195, portalId=5001)
        self.select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52000195_QD__52000195__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraEffect03_4(self.ctx)


class CameraEffect03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_5(self.ctx)


class CameraEffect03_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[204])
        self.visible_my_pc(isVisible=True) # 유저 투명 처리 품
        self.set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        self.add_buff(boxIds=[2001], skillId=99910402, level=1, isPlayer=False, isSkillSet=True) # 에레브 변신
        self.add_buff(boxIds=[2001], skillId=99910402, level=1, isPlayer=False, isSkillSet=False) # 에레브 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_6(self.ctx)


class CameraEffect03_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_7(self.ctx)


class CameraEffect03_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11001302, msg='$52000195_QD__52000195__1$', align='left', illustId='Ereb_surprise', duration=3000)
        self.add_cinematic_talk(npcId=11001302, msg='$52000195_QD__52000195__2$', align='left', illustId='Ereb_serious', duration=3000)
        self.add_cinematic_talk(npcId=11001302, msg='$52000195_QD__52000195__3$', align='left', illustId='Ereb_serious', duration=3000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return CameraEffect03_8(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[204])
        self.visible_my_pc(isVisible=True) # 유저 투명 처리 품
        self.set_visible_ui(uiNames=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'], visible=False)
        self.add_buff(boxIds=[2001], skillId=99910402, level=1, isPlayer=False, isSkillSet=True) # 에레브 변신
        self.add_buff(boxIds=[2001], skillId=99910402, level=1, isPlayer=False, isSkillSet=False) # 에레브 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect03_8(self.ctx)


class CameraEffect03_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2002]):
            return 과거장면_01(self.ctx)


class 과거장면_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 과거장면_02(self.ctx)


class 과거장면_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.create_monster(spawnIds=[201]) # 바론
        self.create_monster(spawnIds=[202]) # 칼
        self.create_monster(spawnIds=[203]) # 에레브
        self.remove_buff(boxId=2002, skillId=99910402)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 과거장면_03(self.ctx)


class 과거장면_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 과거장면_05(self.ctx)


class 과거장면_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=11004787, msg='$52000195_QD__52000195__4$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 과거장면_06(self.ctx)


class 과거장면_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Talk_A', duration=8000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000195_QD__52000195__5$', align='right', illustId='Karl_normal', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000195_QD__52000195__6$', align='right', illustId='Karl_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 과거장면_07(self.ctx)


class 과거장면_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=11004787, msg='$52000195_QD__52000195__7$', align='right', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 과거장면_08(self.ctx)


class 과거장면_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 과거장면_08_1(self.ctx)


class 과거장면_08_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=11004778, msg='$52000195_QD__52000195__8$', align='right', illustId='Karl_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 과거장면_08_2(self.ctx)


class 과거장면_08_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[202])
        self.select_camera_path(pathIds=[4009], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 과거장면_09(self.ctx)


class 과거장면_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11004785, msg='$52000195_QD__52000195__9$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 과거장면_10(self.ctx)


class 과거장면_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11004785, msg='$52000195_QD__52000195__10$', illustId='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npcId=11004785, msg='$52000195_QD__52000195__11$', illustId='Ereb_surprise', duration=4000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 업적달성(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 업적달성(self.ctx)


class 업적달성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=2002, achieve='DreamofEreb')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000193, portalId=5001)


initial_state = start
