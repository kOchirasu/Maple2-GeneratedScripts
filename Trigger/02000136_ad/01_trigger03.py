""" trigger/02000136_ad/01_trigger03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[804], visible=False)
        self.set_interact_object(triggerIds=[10000068], state=1)
        self.set_mesh(triggerIds=[15], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000068], stateValue=0):
            return 발판등장(self.ctx)


class 발판등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[15], visible=True)
        self.set_effect(triggerIds=[804], visible=True)
        self.set_timer(timerId='2', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


initial_state = 대기
