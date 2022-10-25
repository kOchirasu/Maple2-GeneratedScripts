""" trigger/02000303_bf/machine_02.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000576], stateValue=0):
            self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=2)
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 시작
