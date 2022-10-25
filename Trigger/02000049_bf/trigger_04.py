""" trigger/02000049_bf/trigger_04.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000270], state=1)
        self.set_effect(triggerIds=[101], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000270], stateValue=0):
            return 비내림(self.ctx)


class 비내림(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[101], visible=True)
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
