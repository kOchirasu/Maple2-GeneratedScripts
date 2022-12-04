""" trigger/02010026_bf/01_lever01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1000,1001,1002,1003,1004], visible=False, arg3=0, delay=0, scale=5)
        self.set_interact_object(triggerIds=[10000908], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000908], stateValue=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[1000,1001,1002,1003,1004], visible=True, meshCount=5, arg4=100, delay=100)
        self.set_timer(timerId='2', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
