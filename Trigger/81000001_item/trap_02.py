""" trigger/81000001_item/trap_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000127], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000127], stateValue=0):
            self.set_mesh(triggerIds=[501,502,503,504,505], visible=False, arg3=0, delay=0)
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='127', seconds=5, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='127'):
            self.set_mesh(triggerIds=[501,502,503,504,505], visible=True, arg3=0, delay=0)
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='127')


initial_state = 시작
