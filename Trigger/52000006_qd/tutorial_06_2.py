""" trigger/52000006_qd/tutorial_06_2.xml """
import trigger_api


class 엔터대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 오픈대기중(self.ctx)


class 오픈대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000016]):
            return 화면효과(self.ctx)


class 화면효과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 화면효과2(self.ctx)


class 화면효과2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=3)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_2__0$')
        self.set_effect(triggerIds=[401], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 화면효과3(self.ctx)


class 화면효과3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.select_camera(triggerId=303, enable=True)
        self.set_effect(triggerIds=[402], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 맵이동(self.ctx)


class 맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.move_user(mapId=52000007, portalId=1)


initial_state = 엔터대기중
