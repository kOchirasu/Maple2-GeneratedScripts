""" trigger/52000170_qd/52000170.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1000, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=52000170, portalId=1010)
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
            return 경기장전경씬01(self.ctx)
        if self.wait_tick(waitTick=85000):
            return 경기장전경씬01(self.ctx)


class 경기장전경씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 경기장전경씬02_1(self.ctx)


class 경기장전경씬02_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrolName='MS2PatrolData_PC')
        self.select_camera_path(pathIds=[4000,4001], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 경기장전경씬02(self.ctx)


class 경기장전경씬02(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000170_QD__52000170__0$', desc='$52000170_QD__52000170__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 경기장전경씬03(self.ctx)


class 경기장전경씬03(common.Trigger):
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
        self.create_monster(spawnIds=[400], animationEffect=False) # 바사라
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.add_balloon_talk(spawnId=0, msg='$52000170_QD__52000170__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=52001701, textId=52001701, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002378], questStates=[3]):
            return 바사라등장01(self.ctx)


# ########################씬2 케이틀린 등장########################
class 바사라등장01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401], animationEffect=False) # 바사라
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_basara')
        self.show_guide_summary(entityId=52001702, textId=52001702, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002381], questStates=[3]):
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
        self.move_user(mapId=52000171, portalId=1)


initial_state = Wait
