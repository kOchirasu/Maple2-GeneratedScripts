""" trigger/02000352_bf/lever_check.xml """
import trigger_api


class 레버체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000823], state=0)
        self.set_interact_object(triggerIds=[10000824], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000823], stateValue=1):
            return 레버체크2(self.ctx)
        if self.object_interacted(interactIds=[10000824], stateValue=1):
            return 레버체크2(self.ctx)


class 레버체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000823], stateValue=0):
            return 레버체크3_1개(self.ctx)
        if self.object_interacted(interactIds=[10000824], stateValue=0):
            return 레버체크4_1개(self.ctx)


class 레버체크3_1개(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000824], stateValue=0):
            return 레버체크완료(self.ctx)


class 레버체크4_1개(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000823], stateValue=0):
            return 레버체크완료(self.ctx)


class 레버체크완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_mesh(triggerIds=[6054,6055,6056], visible=False, delay=200, scale=15) # 빨간선 사라지게
        self.set_mesh(triggerIds=[6154,6155,6156], visible=True, delay=200, scale=0) # 파란선 나타나게
        self.set_effect(triggerIds=[9000005], visible=True) # Sound EFfect on

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 열림_끝(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[6003], visible=False, delay=0, scale=10) # 벽 해제


class 열림_끝(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=113, textId=40011) # 다음 지역으로 이동하세요
        self.select_camera(triggerId=8002, enable=False) # 연출 카메라
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=113)


class 종료(trigger_api.Trigger):
    pass


initial_state = 레버체크
