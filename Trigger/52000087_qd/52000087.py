""" trigger/52000087_qd/52000087.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[22651], questIds=[10003370], questStates=[2]):
            return 보고시작준비_01(self.ctx)


# 에레브여제에게 보고
class 보고시작준비_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000087, portalId=6001)
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보고시작준비_02(self.ctx)


class 보고시작준비_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3001')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return 보고시작준비_03(self.ctx)


class 보고시작준비_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=5000)
        self.select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보고시작준비_04(self.ctx)


class 보고시작준비_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보고시작_01(self.ctx)


class 보고시작_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087__0$')
        self.move_user(mapId=52000087, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='Kritias_EpicCutScene_second_01.swf', movieId=1)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return Quit(self.ctx)
        if self.wait_tick(waitTick=35000):
            return Quit(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52000087, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)


initial_state = 대기
