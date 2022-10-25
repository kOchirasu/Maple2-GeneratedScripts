""" trigger/02000317_bf/vehicle.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001047], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001047], stateValue=0):
            return hide(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001047], state=2)


class hide(common.Trigger):
    pass


initial_state = idle
