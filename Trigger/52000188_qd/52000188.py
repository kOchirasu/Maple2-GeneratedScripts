""" trigger/52000188_qd/52000188.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002794], questStates=[2]):
            return 바베니로_01()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2]):
            return 컷씬준비()
        if user_detected(boxIds=[2001], jobCode=0):
            return wait_01_02()


class wait_01_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52000188, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 동굴도착_01()


class 동굴도착_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 동굴도착_01_2()


class 동굴도착_01_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 동굴도착_02()


class 동굴도착_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52000188_QD__52000188__0$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 정리_01()


class 정리_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 정리_02()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 정리_02()


class 정리_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 밝아짐()


class 밝아짐(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2]):
            return 컷씬준비()


# 직업별 컷씬 출력
class 컷씬준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 컷씬준비_02()


class 컷씬준비_02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=10):
            return 나이트컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=20):
            return 버서커컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=30):
            return 위자드컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=40):
            return 프리스트컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=50):
            return 레인저컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=60):
            return 헤비거너컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=70):
            return 시프컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=80):
            return 어쌔신컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=90):
            return 룬블컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=100):
            return 스커컷씬()
        if quest_user_detected(boxIds=[2001], questIds=[40002793], questStates=[2], jobCode=110):
            return 소바컷씬()


class 나이트컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_knight.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 버서커컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_berserker.swf', movieId=2)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 위자드컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_wizard.swf', movieId=3)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 프리스트컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_priest.swf', movieId=4)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 레인저컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_ranger.swf', movieId=5)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 헤비거너컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_heavy.swf', movieId=6)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 시프컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_thief.swf', movieId=7)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 어쌔신컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_Assassin.swf', movieId=8)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 룬블컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_RBlader.swf', movieId=9)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 스커컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_striker.swf', movieId=10)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 소바컷씬(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='MasterSkill_soul.swf', movieId=11)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상재생_end()
        if wait_tick(waitTick=5000):
            return 영상재생_end()


class 영상재생_end(state.State):
    def on_enter(self):
        set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 영상재생_end02()


class 영상재생_end02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[40002794], questStates=[2]):
            return 바베니로_01()


class 바베니로_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 바베니로_02()


class 바베니로_02(state.State):
    def on_enter(self):
        move_user(mapId=2020041, portalId=1)


