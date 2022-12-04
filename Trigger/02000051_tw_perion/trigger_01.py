""" trigger/02000051_tw_perion/trigger_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000382], state=1)
        self.set_mesh(triggerIds=[101], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000382], stateValue=0):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101], visible=True)
        self.set_timer(timerId='1', seconds=15, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
