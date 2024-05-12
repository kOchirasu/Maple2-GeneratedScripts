""" trigger/81000001_item/trap_05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000130], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000130], stateValue=0):
            self.set_mesh(triggerIds=[801,802,803,804,805,806], visible=False, arg3=0, delay=0)
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='130', seconds=5, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='130'):
            self.set_mesh(triggerIds=[801,802,803,804,805,806], visible=True, arg3=0, delay=0)
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timerId='130')


initial_state = 시작
