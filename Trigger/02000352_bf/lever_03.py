""" trigger/02000352_bf/lever_03.xml """
import common


class 닫힘상태(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000824], state=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000824], stateValue=1):
            return 작동(self.ctx)


class 작동(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000824], stateValue=0):
            return 열림상태(self.ctx)


class 열림상태(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[9000004], visible=True) # Sound EFfect on
        self.set_mesh(triggerIds=[6060,6061,6062,6063], visible=False, delay=200, scale=15) # 빨간선 사라지게
        self.set_mesh(triggerIds=[6160,6161,6162,6163], visible=True, delay=200, scale=0) # 파란선 나타나게

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 열림(self.ctx)


class 열림(common.Trigger):
    pass


initial_state = 닫힘상태
