""" trigger/02010028_bf/mesh01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1000,1001,1002,1003,1004,1005], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000902], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000902], stateValue=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1000,1001,1002,1003,1004,1005], visible=False, arg3=0, delay=0, scale=7)
        self.set_timer(timerId='2', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
