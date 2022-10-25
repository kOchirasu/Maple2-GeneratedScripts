""" trigger/99999907/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000019], state=1)
        self.set_interact_object(triggerIds=[12000020], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000019], stateValue=0):
            return 리셋(self.ctx)
        if self.object_interacted(interactIds=[12000020], stateValue=0):
            return 리셋(self.ctx)


class 리셋(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 대기(self.ctx)


initial_state = 대기
