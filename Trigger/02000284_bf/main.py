""" trigger/02000284_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000428], state=2)
        self.set_interact_object(triggerIds=[10000430], state=2)
        self.set_interact_object(triggerIds=[10000431], state=2)
        self.set_interact_object(triggerIds=[10000432], state=2)
        self.set_interact_object(triggerIds=[10000433], state=2)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 보스연출(self.ctx)


class 보스연출(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.select_camera(triggerId=3001, enable=True)
        self.set_skip(state=준비)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 준비(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=3001, enable=False)


class 준비(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002815, textId=20002815, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 반응대기(self.ctx)


class 반응대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            self.set_interact_object(triggerIds=[10000428], state=1)
            self.show_guide_summary(entityId=20002814, textId=20002814)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return 반응체크(self.ctx)


class 반응체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000428], stateValue=0):
            self.hide_guide_summary(entityId=20002814)
            self.dungeon_clear()
            self.set_mesh(triggerIds=[301,302,303,304,305,306,307,308], visible=True, arg3=0, delay=100, scale=0)
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            return 소멸대기(self.ctx)


class 소멸대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 소멸(self.ctx)


class 소멸(common.Trigger):
    pass


initial_state = 대기
