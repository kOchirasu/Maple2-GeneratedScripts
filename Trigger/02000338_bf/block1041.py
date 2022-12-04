""" trigger/02000338_bf/block1041.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1041], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10041]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 진행1(self.ctx)


class 진행1(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1041], visible=False, arg3=0, delay=0, scale=2)


initial_state = 대기
