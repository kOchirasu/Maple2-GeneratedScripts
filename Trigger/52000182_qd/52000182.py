""" trigger/52000182_qd/52000182.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1000, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=52000182, portalId=1010)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 병원전경씬01(self.ctx)
        if self.wait_tick(waitTick=85000):
            return 병원전경씬01(self.ctx)


class 병원전경씬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_monster(spawnIds=[400], animationEffect=False)
        self.create_monster(spawnIds=[401], animationEffect=False)
        self.create_monster(spawnIds=[402], animationEffect=False)
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 병원전경씬02_1(self.ctx)


class 병원전경씬02_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrolName='MS2PatrolData_PC_Walk')
        self.select_camera_path(pathIds=[4000,4001,4002,4003], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 병원전경씬02(self.ctx)


class 병원전경씬02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004,4005,4006,4007], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52000182_QD__52000182__0$', desc='$52000182_QD__52000182__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 병원전경씬03(self.ctx)


class 병원전경씬03(trigger_api.Trigger):
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
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.add_balloon_talk(spawnId=0, msg='$52000182_QD__52000182__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=52001821, textId=52001821, duration=10000)
        self.create_monster(spawnIds=[2000], animationEffect=False) # 조디의무덤

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002337], questStates=[3]):
            return 치유마법전개01(self.ctx)


# ########################치유 마법 전개########################
class 치유마법전개01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 치유마법전개02(self.ctx)


class 치유마법전개02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 치유마법전개03(self.ctx)


class 치유마법전개03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002340], questStates=[3]):
            return 수련장이동01(self.ctx)


class 수련장이동01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 수련장이동02(self.ctx)


class 수련장이동02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000183, portalId=1)


initial_state = Wait
