""" trigger/02000175_bf/triggercube_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[303], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 발판(self.ctx)


class 발판(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[303], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[103]):
            return 발판숨김(self.ctx)


class 발판숨김(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


initial_state = 대기
