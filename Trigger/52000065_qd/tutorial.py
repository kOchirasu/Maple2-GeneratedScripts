""" trigger/52000065_qd/tutorial.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1000], visible=True, arg3=0, delay=0, scale=0) # 강철 결계
        self.set_mesh(triggerIds=[2000], visible=True, arg3=0, delay=0, scale=0) # Invisible
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=30, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=40, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=50, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=60, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=70, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=80, visible=False, enable=False, minimapVisible=False)
        self.create_widget(type='Guide')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\Common_Opening.usm', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상완료_01(self.ctx)
        if self.wait_tick(waitTick=190000):
            return 영상완료_01(self.ctx)


class 영상완료_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='Guide', name='IsTriggerEvent', condition='251'):
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1000], visible=False, arg3=0, delay=0, scale=0) # 강철 결계
        self.set_mesh(triggerIds=[2000], visible=False, arg3=0, delay=0, scale=0) # Invisible
        self.guide_event(eventId=260)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001], jobCode=90):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.start_tutorial()
            return None
        if self.user_detected(boxIds=[9001], jobCode=110):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.start_tutorial()
            return None
        if self.user_detected(boxIds=[9001], jobCode=100):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.start_tutorial()
            return None
        if self.user_detected(boxIds=[9001], jobCode=1):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.start_tutorial()
            return None
        if self.user_detected(boxIds=[9001], jobCode=10):
            self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)
            return None
        if self.user_detected(boxIds=[9001], jobCode=20):
            self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=True)
            return None
        if self.user_detected(boxIds=[9001], jobCode=30):
            self.set_portal(portalId=30, visible=True, enable=True, minimapVisible=True)
            return None
        if self.user_detected(boxIds=[9001], jobCode=40):
            self.set_portal(portalId=40, visible=True, enable=True, minimapVisible=True)
            return None
        if self.user_detected(boxIds=[9001], jobCode=50):
            self.set_portal(portalId=50, visible=True, enable=True, minimapVisible=True)
            return None
        if self.user_detected(boxIds=[9001], jobCode=60):
            self.set_portal(portalId=60, visible=True, enable=True, minimapVisible=True)
            return None
        if self.user_detected(boxIds=[9001], jobCode=70):
            self.set_portal(portalId=70, visible=True, enable=True, minimapVisible=True)
            return None
        if self.user_detected(boxIds=[9001], jobCode=80):
            self.set_portal(portalId=80, visible=True, enable=True, minimapVisible=True)
            return None


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
