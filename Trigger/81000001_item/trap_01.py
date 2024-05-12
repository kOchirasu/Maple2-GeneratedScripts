""" trigger/81000001_item/trap_01.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000126], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000126], stateValue=0):
            self.set_mesh(triggerIds=[401,402,403], visible=False, arg3=0, delay=0)
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='126', seconds=5, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='126'):
            self.set_mesh(triggerIds=[401,402,403], visible=True, arg3=0, delay=0)
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='126')


initial_state = 시작
