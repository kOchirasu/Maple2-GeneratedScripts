""" trigger/61000004_me/trap_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000129], stateValue=0):
            self.set_mesh(triggerIds=[701,702,703], visible=False, arg3=0, delay=0)
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='129', seconds=5, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='129'):
            self.set_mesh(triggerIds=[701,702,703], visible=True, arg3=0, delay=0)
            return 시작(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='129')


initial_state = 시작
