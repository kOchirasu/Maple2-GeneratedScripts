""" trigger/52010071_qd/52010071.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001]):
            return 상황설명(self.ctx)


class 상황설명(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=9, script='$52010071_QD__52010071__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 칠신장들_01(self.ctx)


class 칠신장들_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False) # 검마
        self.create_monster(spawnIds=[102], animationEffect=False) # 투르카
        self.create_monster(spawnIds=[103], animationEffect=False) # 다크로드
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 칠신장들_02(self.ctx)


class 칠신장들_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.select_camera_path(pathIds=[4000,4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 검마대사_01(self.ctx)


class 검마대사_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=6000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__1$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 검마대사_02(self.ctx)


class 검마대사_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 검마대사_03(self.ctx)


class 검마대사_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=15000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__2$', duration=5000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__3$', duration=5000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__4$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=16000):
            return 검마대사_04(self.ctx)


class 검마대사_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 투르카대사_01(self.ctx)


class 투르카대사_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=11000)
        self.add_cinematic_talk(npcId=11001956, msg='$52010071_QD__52010071__6$', duration=5000)
        self.add_cinematic_talk(npcId=11001956, msg='$52010071_QD__52010071__7$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 둘이말함_01(self.ctx)


class 둘이말함_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Attack_01_A', duration=3000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__8$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 둘이말함_02(self.ctx)


class 둘이말함_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=18000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__15$', duration=6000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__9$', duration=5000)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__10$', duration=4000)
        self.add_cinematic_talk(npcId=11001956, msg='$52010071_QD__52010071__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=18000):
            return 검마명령_02(self.ctx)


class 검마명령_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4006,4007], returnView=False)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__12$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 검마명령_03(self.ctx)


class 검마명령_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__13$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 검마명령_04(self.ctx)


class 검마명령_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.add_cinematic_talk(npcId=11003894, msg='$52010071_QD__52010071__14$', duration=5000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동시키기_01(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이동시키기_01(self.ctx)


class 이동시키기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=52010072, portalId=1)


initial_state = wait_01
