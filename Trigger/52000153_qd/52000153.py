""" trigger/52000153_qd/52000153.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000], animationEffect=False) # 제니아
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChange_knight.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=8000):
            return 영상재생_end(self.ctx)


class 영상재생_end(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000153_QD__52000153__0$', arg3=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 영상재생_end02(self.ctx)


class 영상재생_end02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 전경씬01(self.ctx)


class 전경씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_pc_emotion_loop(sequenceName='Sword_Attack_Idle_A', duration=10000, arg3=True)
        self.select_camera_path(pathIds=[4000,4001], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 전경씬02(self.ctx)


class 전경씬02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit01(self.ctx)


class Quit01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_pc_emotion_loop(sequenceName='Sword_Attack_Idle_A', duration=1, arg3=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.show_guide_summary(entityId=25201531, textId=25201531, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002333], questStates=[3]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit03(self.ctx)


# ########################퀘스트 종료########################
class Quit03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002335], questStates=[3]):
            return 프론티아재단으로01(self.ctx)


class 프론티아재단으로01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 프론티아재단으로02(self.ctx)


class 프론티아재단으로02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000186, portalId=1)


initial_state = Wait
