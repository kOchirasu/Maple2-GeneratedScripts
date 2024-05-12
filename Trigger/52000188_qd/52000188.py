""" trigger/52000188_qd/52000188.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002794], questStates=[2]):
            return 바베니로_01(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2]):
            return 컷씬준비(self.ctx)
        if self.user_detected(boxIds=[2001], jobCode=0):
            return wait_01_02(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000188, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 동굴도착_01(self.ctx)


class 동굴도착_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 동굴도착_01_2(self.ctx)


class 동굴도착_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3001')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 동굴도착_02(self.ctx)


class 동굴도착_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52000188_QD__52000188__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 정리_01(self.ctx)


class 정리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 정리_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2]):
            return 컷씬준비(self.ctx)


# 직업별 컷씬 출력
class 컷씬준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 컷씬준비_02(self.ctx)


class 컷씬준비_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=10):
            return 나이트컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=20):
            return 버서커컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=30):
            return 위자드컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=40):
            return 프리스트컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=50):
            return 레인저컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=60):
            return 헤비거너컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=70):
            return 시프컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=80):
            return 어쌔신컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=90):
            return 룬블컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=100):
            return 스커컷씬(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=110):
            return 소바컷씬(self.ctx)


class 나이트컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_knight.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 버서커컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_berserker.swf', movieId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 위자드컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_wizard.swf', movieId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 프리스트컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_priest.swf', movieId=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 레인저컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_ranger.swf', movieId=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 헤비거너컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_heavy.swf', movieId=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 시프컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_thief.swf', movieId=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 어쌔신컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_Assassin.swf', movieId=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 룬블컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_RBlader.swf', movieId=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 스커컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_striker.swf', movieId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 소바컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='MasterSkill_soul.swf', movieId=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 영상재생_end(self.ctx)


class 영상재생_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 영상재생_end02(self.ctx)


class 영상재생_end02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[40002794], questStates=[2]):
            return 바베니로_01(self.ctx)


class 바베니로_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 바베니로_02(self.ctx)


class 바베니로_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2020041, portalId=1)


initial_state = wait_01
