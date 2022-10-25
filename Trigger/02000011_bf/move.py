""" trigger/02000011_bf/move.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2, startDelay=0)
        self.set_breakable(triggerIds=[7000], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 반응대기(self.ctx)


class 반응대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000361], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000361], stateValue=0):
            return 이동(self.ctx)


class 이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=6, startDelay=0)
        self.set_breakable(triggerIds=[7000], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='6'):
            return 대기(self.ctx)


initial_state = 대기
