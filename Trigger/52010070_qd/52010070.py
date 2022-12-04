""" trigger/52010070_qd/52010070.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001], jobCode=0):
            return 엔피씨스폰(self.ctx)


class 엔피씨스폰(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False) # 유페리아
        self.create_monster(spawnIds=[102], animationEffect=False) # 이슈라
        self.create_monster(spawnIds=[103], animationEffect=False) # 렌듀비앙
        self.create_monster(spawnIds=[107], animationEffect=False) # 라네모네
        self.create_monster(spawnIds=[109], animationEffect=False) # 홀슈타트
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100800], questStates=[2]):
            return 룬블즈_일어남(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[50100790], questStates=[2]):
            return 룬블즈_일어남(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[50100790], questStates=[3]):
            return 룬블즈_일어남(self.ctx)


class 룬블즈_일어남(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_cinematic_ui(type=1)
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.move_user(mapId=52010070, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 룬블즈_일어남_02(self.ctx)


class 룬블즈_일어남_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 룬블즈_일어남_03(self.ctx)


class 룬블즈_일어남_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=109, sequenceName='Attack_Idle_A', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 룬블즈_일어남_04(self.ctx)


class 룬블즈_일어남_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.set_npc_emotion_loop(spawnId=107, sequenceName='Bore_A', duration=4000)
        self.set_npc_emotion_loop(spawnId=109, sequenceName='Attack_01_A', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 룬블즈_일어남_04_01(self.ctx)


class 룬블즈_일어남_04_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_time_scale(enable=True, startScale=0.1, endScale=0.5, duration=5, interpolator=1)
        self.set_npc_emotion_loop(spawnId=109, sequenceName='Attack_Idle_A', duration=4000)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 룬블즈_일어남_05(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 룬블즈_일어남_05(self.ctx)


class 룬블즈_일어남_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 룬블즈_일어남_07(self.ctx)


class 룬블즈_일어남_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.create_monster(spawnIds=[104], animationEffect=False) # 유페리아
        self.create_monster(spawnIds=[105], animationEffect=False) # 이슈라
        self.create_monster(spawnIds=[106], animationEffect=False) # 렌듀비앙
        self.destroy_monster(spawnIds=[101], arg2=False)
        self.destroy_monster(spawnIds=[102], arg2=False)
        self.destroy_monster(spawnIds=[103], arg2=False)
        self.set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 룬블즈_일어남_08(self.ctx)


class 룬블즈_일어남_08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 룬블즈_일어남_09(self.ctx)


class 룬블즈_일어남_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 룬블즈_일어남_09_01(self.ctx)


class 룬블즈_일어남_09_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 룬블즈_일어남_10(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 룬블즈_일어남_10(self.ctx)


class 룬블즈_일어남_10(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100790], questStates=[3]):
            return 홀슈타트로바꾸기(self.ctx)


class 홀슈타트로바꾸기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.destroy_monster(spawnIds=[109], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100800], questStates=[2]):
            return 에레브흑화(self.ctx)


class 에레브흑화(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_3, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에레브흑화_02(self.ctx)


class 에레브흑화_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에레브흑화_03(self.ctx)


class 에레브흑화_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에레브흑화_04(self.ctx)


class 에레브흑화_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52010070, portalId=6001)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3001')
        self.add_cinematic_talk(npcId=11004128, align='left', illustId='Ishura_normal', msg='$52010070_QD__52010070__0$', duration=4000)
        self.add_cinematic_talk(npcId=11004191, align='left', illustId='11004022', msg='$52010070_QD__52010070__1$', duration=4000)
        self.add_cinematic_talk(npcId=11004128, align='left', illustId='Ishura_normal', msg='$52010070_QD__52010070__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 에레브흑화_05(self.ctx)


class 에레브흑화_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='ProphecyofFall.swf', movieId=1)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 에레브흑화_06(self.ctx)
        if self.wait_tick(waitTick=85000):
            return 에레브흑화_06(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에레브흑화_06(self.ctx)


class 에레브흑화_06(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100800], questStates=[3]):
            return 이동시키기(self.ctx)


class 이동시키기(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010072, portalId=1)


initial_state = wait_01
