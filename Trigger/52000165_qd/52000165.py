""" trigger/52000165_qd/52000165.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[400], animationEffect=False) # 아이샤
        self.create_monster(spawnIds=[401], animationEffect=False) # 아이샤
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChange_heavy.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=8000):
            return 영상재생_end(self.ctx)


class 영상재생_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000165_QD__52000165__0$', arg3=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 영상재생_end02(self.ctx)


class 영상재생_end02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 전경씬01(self.ctx)


class 전경씬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_pc_emotion_loop(sequenceName='Sword_Attack_Idle_A', duration=10000, arg3=True)
        self.select_camera_path(pathIds=[4000,4001], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_pc')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return 전경씬02(self.ctx)


class 전경씬02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=52001651, textId=52001651, duration=10000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002355], questStates=[3]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_isha')
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit03(self.ctx)


# ########################퀘스트 종료########################
class Quit03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002358], questStates=[3]):
            return 프론티아재단으로01(self.ctx)


class 프론티아재단으로01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 프론티아재단으로02(self.ctx)


class 프론티아재단으로02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000186, portalId=1)


initial_state = Wait
