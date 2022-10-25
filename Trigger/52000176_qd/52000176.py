""" trigger/52000176_qd/52000176.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1000, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=52000176, portalId=1010)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 숲전경씬01(self.ctx)
        if self.wait_tick(waitTick=85000):
            return 숲전경씬01(self.ctx)


class 숲전경씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 숲전경씬02_1(self.ctx)


class 숲전경씬02_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrolName='MS2PatrolData_pc')
        self.select_camera_path(pathIds=[4000,4002,4003], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 숲전경씬02(self.ctx)


class 숲전경씬02(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000176_QD__52000176__0$', desc='$52000176_QD__52000176__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 숲전경씬03(self.ctx)


class 숲전경씬03(common.Trigger):
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
        self.add_balloon_talk(spawnId=0, msg='$52000176_QD__52000176__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=52001761, textId=52001761, duration=10000)
        self.create_monster(spawnIds=[400], animationEffect=False) # 과녁

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002359], questStates=[3]):
            return 하스터등장01(self.ctx)


# ########################씬2 케이틀린 등장########################
class 하스터등장01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401], animationEffect=False) # 제니아
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_haster')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002363], questStates=[3]):
            return 수련장이동01(self.ctx)


class 수련장이동01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 수련장이동02(self.ctx)


class 수련장이동02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000177, portalId=1)


initial_state = Wait
