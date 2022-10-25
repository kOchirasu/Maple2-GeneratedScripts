""" trigger/02000351_bf/lever_02.xml """
import common


class 닫힘상태(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000819], state=0)
        self.set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062], visible=True, delay=0, scale=0) # 빨간 선 보이게
        self.set_mesh(triggerIds=[6081,6082,6083,6084,6085,6086,6087,6088,6089,6090,6091,6092], visible=False, delay=0, scale=0) # 파란 선 안보이게

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000819], stateValue=1):
            return 작동(self.ctx)


class 작동(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000819], stateValue=0):
            return 열림상태(self.ctx)


class 열림상태(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[9000003], visible=True) # Object_Electricity_On_01
        self.set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062], visible=False, delay=200, scale=15) # 빨간선 사라지게
        self.set_mesh(triggerIds=[6081,6082,6083,6084,6085,6086,6087,6088,6089,6090,6091,6092], visible=True, delay=200, scale=15) # 파란선 나타나게

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 열림(self.ctx)


class 열림(common.Trigger):
    pass


initial_state = 닫힘상태
