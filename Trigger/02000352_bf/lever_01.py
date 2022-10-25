""" trigger/02000352_bf/lever_01.xml """
import common


class 닫힘상태(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6111], visible=True, delay=0, scale=0) # 벽
        self.set_mesh(triggerIds=[6101], visible=False, delay=0, scale=0) # 벽

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000822], stateValue=1):
            return 작동(self.ctx)


class 작동(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=111, textId=20000080) # 스위치를 정지하세요

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000822], stateValue=0):
            return 열림상태(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=111)


class 열림상태(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[9000002], visible=True) # Sound EFfect on
        self.set_mesh(triggerIds=[6111], visible=False, delay=200, scale=15) # 벽 해제
        self.set_mesh(triggerIds=[6101], visible=True, delay=200, scale=15) # 벽 해제

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 열림(self.ctx)


class 열림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6002], visible=False, delay=0, scale=10) # 벽 해제
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 열림_끝(self.ctx)


class 열림_끝(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=113, textId=40011) # 스위치를 정지하세요
        self.select_camera(triggerId=8001, enable=False) # 연출 카메라


initial_state = 닫힘상태
