""" trigger/02000142_bf/trigger_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[7000], enable=False)
        self.set_interact_object(triggerIds=[10000245], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000245], stateValue=0):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=15, startDelay=0)
        self.set_breakable(triggerIds=[7000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='1')


initial_state = 대기
