""" trigger/02000136_ad/01_trigger02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[801,802,803], visible=False)
        self.set_interact_object(triggerIds=[10000067], state=1)
        self.set_mesh(triggerIds=[14,17,16], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000067], stateValue=0):
            return 발판등장1(self.ctx)


class 발판등장1(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[14], visible=True)
        self.set_effect(triggerIds=[801], visible=True)
        self.set_timer(timerId='2', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 발판등장2(self.ctx)


class 발판등장2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[17], visible=True)
        self.set_effect(triggerIds=[802], visible=True)
        self.set_timer(timerId='3', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 발판등장3(self.ctx)


class 발판등장3(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[16], visible=True)
        self.set_effect(triggerIds=[803], visible=True)
        self.set_timer(timerId='4', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 대기(self.ctx)


initial_state = 대기
