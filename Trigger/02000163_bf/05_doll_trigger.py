""" trigger/02000163_bf/05_doll_trigger.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[404], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000105], stateValue=0):
            return 로봇사라짐(self.ctx)


class 로봇사라짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[404], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000105], stateValue=1):
            return 대기(self.ctx)


initial_state = 대기
