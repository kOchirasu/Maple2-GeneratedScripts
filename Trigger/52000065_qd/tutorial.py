""" trigger/52000065_qd/tutorial.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1000], visible=True, arg3=0, arg4=0, arg5=0) # 강철 결계
        set_mesh(triggerIds=[2000], visible=True, arg3=0, arg4=0, arg5=0) # Invisible
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=30, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=40, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=50, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=60, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=70, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=80, visible=False, enabled=False, minimapVisible=False)
        create_widget(type='Guide')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 영상준비_01()


class 영상준비_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상재생_01()


class 영상재생_01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\Common_Opening.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상완료_01()
        if wait_tick(waitTick=190000):
            return 영상완료_01()


class 영상완료_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='251'):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 해제()


class 해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1000], visible=False, arg3=0, arg4=0, arg5=0) # 강철 결계
        set_mesh(triggerIds=[2000], visible=False, arg3=0, arg4=0, arg5=0) # Invisible
        guide_event(eventId=260)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001], jobCode=90):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            start_tutorial()
            return None
        if user_detected(boxIds=[9001], jobCode=110):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            start_tutorial()
            return None
        if user_detected(boxIds=[9001], jobCode=100):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            start_tutorial()
            return None
        if user_detected(boxIds=[9001], jobCode=1):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            start_tutorial()
            return None
        if user_detected(boxIds=[9001], jobCode=10):
            set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
            return None
        if user_detected(boxIds=[9001], jobCode=20):
            set_portal(portalId=20, visible=True, enabled=True, minimapVisible=True)
            return None
        if user_detected(boxIds=[9001], jobCode=30):
            set_portal(portalId=30, visible=True, enabled=True, minimapVisible=True)
            return None
        if user_detected(boxIds=[9001], jobCode=40):
            set_portal(portalId=40, visible=True, enabled=True, minimapVisible=True)
            return None
        if user_detected(boxIds=[9001], jobCode=50):
            set_portal(portalId=50, visible=True, enabled=True, minimapVisible=True)
            return None
        if user_detected(boxIds=[9001], jobCode=60):
            set_portal(portalId=60, visible=True, enabled=True, minimapVisible=True)
            return None
        if user_detected(boxIds=[9001], jobCode=70):
            set_portal(portalId=70, visible=True, enabled=True, minimapVisible=True)
            return None
        if user_detected(boxIds=[9001], jobCode=80):
            set_portal(portalId=80, visible=True, enabled=True, minimapVisible=True)
            return None


class 종료(state.State):
    pass


