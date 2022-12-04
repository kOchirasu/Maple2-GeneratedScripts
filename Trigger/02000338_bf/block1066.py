""" trigger/02000338_bf/block1066.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1066], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10066]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 진행1(self.ctx)


class 진행1(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1066], visible=False, arg3=0, delay=0, scale=2)


initial_state = 대기
