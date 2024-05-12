""" trigger/02000316_bf/qeagle_10.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000202], state=1)
        self.set_actor(triggerId=919, visible=False, initialSequence='Attack_Idle_A')
        self.set_effect(triggerIds=[920], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000202], stateValue=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=919, visible=True, initialSequence='Attack_Idle_A')
        self.set_effect(triggerIds=[920], visible=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 그리폰제거(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(triggerId=919, visible=False, initialSequence='Attack_Idle_A')
        self.set_effect(triggerIds=[920], visible=False)


class 그리폰제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
