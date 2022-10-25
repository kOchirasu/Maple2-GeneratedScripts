""" trigger/02000284_bf/ladder.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000429], state=1)
        self.set_mesh(triggerIds=[314,315,316,317,318,319,320], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000429], stateValue=0):
            return 사다리생성(self.ctx)


class 사다리생성(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000429], state=0)
        self.set_mesh(triggerIds=[314,315,316,317,318,319,320], visible=True, arg3=0, delay=500, scale=0)
        self.set_timer(timerId='1500', seconds=1500, startDelay=0, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1500'):
            return 대기(self.ctx)


initial_state = 대기
