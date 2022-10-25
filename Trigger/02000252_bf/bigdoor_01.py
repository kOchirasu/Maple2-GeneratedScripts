""" trigger/02000252_bf/bigdoor_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[161,162,163,164], visible=True)
        self.set_interact_object(triggerIds=[10000403], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000403], stateValue=0):
            return 열기(self.ctx)


class 열기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[161,162,163,164], visible=False)


initial_state = 대기
