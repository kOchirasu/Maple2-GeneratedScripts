""" trigger/52000164_qd/52000164.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1000, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=52000164, portalId=1010)
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
            return 연구실전경씬01(self.ctx)
        if self.wait_tick(waitTick=85000):
            return 연구실전경씬01(self.ctx)


class 연구실전경씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.create_monster(spawnIds=[400], animationEffect=False) # 아이샤
        self.create_monster(spawnIds=[401], animationEffect=False) # 아이샤
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연구실전경씬02_1(self.ctx)


class 연구실전경씬02_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연구실전경씬02(self.ctx)


class 연구실전경씬02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4000,4001,4002], returnView=False)
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_isha')
        self.move_user_path(patrolName='MS2PatrolData_pc')
        self.show_caption(type='VerticalCaption', title='$52000164_QD__52000164__0$', desc='$52000164_QD__52000164__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연구실전경씬03(self.ctx)


class 연구실전경씬03(common.Trigger):
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
        self.show_guide_summary(entityId=52001641, textId=52001641, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002348], questStates=[3]):
            return 아이샤이동01(self.ctx)


class 아이샤이동01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_isha2')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002354], questStates=[3]):
            return 본격연구시작01(self.ctx)


# ########################씬2 케이틀린 등장########################
class 본격연구시작01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 본격연구시작02(self.ctx)


class 본격연구시작02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000165, portalId=1)


initial_state = Wait
