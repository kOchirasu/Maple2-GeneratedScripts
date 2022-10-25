""" trigger/02000351_bf/lever_03.xml """
import common


class 닫힘상태(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000820], state=0)
        self.set_mesh(triggerIds=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162], visible=True, delay=0, scale=0) # 빨간 선 보이게
        self.set_mesh(triggerIds=[6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192], visible=False, delay=0, scale=0) # 파란 선 안보이게

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000820], stateValue=1):
            return 작동(self.ctx)


class 작동(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000820], stateValue=0):
            return 열림상태(self.ctx)


class 열림상태(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[9000004], visible=True) # Object_Electricity_On_01
        self.set_mesh(triggerIds=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162], visible=False, delay=200, scale=15) # 빨간선 사라지게
        self.set_mesh(triggerIds=[6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192], visible=True, delay=200, scale=0) # 파란선 나타나게

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 열림(self.ctx)


class 열림(common.Trigger):
    pass


initial_state = 닫힘상태
