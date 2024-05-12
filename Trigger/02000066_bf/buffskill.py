""" trigger/02000066_bf/buffskill.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return A스킬작동(self.ctx)


class A스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6002], visible=False)
        self.set_skill(triggerIds=[7001], enable=True)
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            self.set_skill(triggerIds=[7001], enable=False)
            self.set_effect(triggerIds=[6002], visible=False)
            return 시작대기중(self.ctx)


initial_state = 시작대기중
