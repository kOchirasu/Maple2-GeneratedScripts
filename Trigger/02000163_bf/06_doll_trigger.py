""" trigger/02000163_bf/06_doll_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[405], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000106], stateValue=0):
            return 로봇사라짐(self.ctx)


class 로봇사라짐(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[405], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000106], stateValue=1):
            return 대기(self.ctx)


initial_state = 대기
