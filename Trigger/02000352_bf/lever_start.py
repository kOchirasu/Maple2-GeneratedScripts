""" trigger/02000352_bf/lever_start.xml """
import trigger_api


class 작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[6201], visible=False, delay=0, scale=0) # 파란 선 안보이게
        self.set_interact_object(triggerIds=[10000821], state=1)
        self.set_mesh(triggerIds=[6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163], visible=True, delay=0, scale=0) # 빨간 선 보이게
        self.set_mesh(triggerIds=[6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163], visible=False, delay=0, scale=0) # 파란 선 안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000821], stateValue=0):
            return 열림상태(self.ctx)


class 열림상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[9000001], visible=True) # Sound EFfect on
        self.set_mesh(triggerIds=[6211], visible=False, delay=200, scale=15) # 빨간 선 안보이게
        self.set_mesh(triggerIds=[6201], visible=True, delay=200, scale=15) # 파란 선 보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[6001], visible=False, delay=0, scale=10) # 벽 해제
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 열림_끝(self.ctx)


class 열림_끝(trigger_api.Trigger):
    pass


initial_state = 작동
