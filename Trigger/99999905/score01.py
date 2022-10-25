""" trigger/99999905/score01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000413], stateValue=0):
            return 점수(self.ctx)


class 점수(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[604], visible=True)
        # action name="전장점수를준다" arg1="104" arg2="50" /

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
