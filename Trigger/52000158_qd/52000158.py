""" trigger/52000158_qd/52000158.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002736], questStates=[3]):
            return 돌아왔다준비_01(self.ctx)
        if self.user_detected(boxIds=[2001], jobCode=0):
            return wait_01_1(self.ctx)


class wait_01_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000158, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_02(self.ctx)


class wait_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 커닝시티전경_01(self.ctx)
        if self.wait_tick(waitTick=85000):
            return 커닝시티전경_01(self.ctx)


class 커닝시티전경_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 커닝시티전경_02(self.ctx)


class 커닝시티전경_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52000158_QD__52000158__0$', desc='$52000158_QD__52000158__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어쌔신_01(self.ctx)


class 어쌔신_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return UI초기화(self.ctx)


class UI초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 밝아짐(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.reset_camera(interpolationTime=0)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002733], questStates=[3]):
            return 이동_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002732], questStates=[2]):
            return 퀘스트가이드(self.ctx)


class 퀘스트가이드(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25201581, textId=25201581, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002734], questStates=[2]):
            return 이동_01(self.ctx)


class 이동_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 이동_02(self.ctx)


class 이동_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000159, portalId=1)


class 돌아왔다준비_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 돌아왔다_01(self.ctx)


class 돌아왔다_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 돌아왔다_02(self.ctx)


class 돌아왔다_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000158, portalId=6001)
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002741], questStates=[2]):
            return 이동2_01(self.ctx)


class 이동2_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 이동2_02(self.ctx)


class 이동2_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000160, portalId=1)


initial_state = wait_01
