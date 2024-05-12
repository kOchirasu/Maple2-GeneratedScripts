""" trigger/02000268_bf/ladder.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[301,302,303,304,305], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000456], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000456], stateValue=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[301,302,303,304,305], visible=True, arg3=0, delay=500, scale=0)
        self.set_timer(timerId='10', seconds=10, startDelay=0, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            self.set_mesh(triggerIds=[305,304,303,302,301], visible=False, arg3=0, delay=500, scale=0)
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='170', seconds=170, startDelay=0, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='170'):
            return 대기(self.ctx)


initial_state = 대기
