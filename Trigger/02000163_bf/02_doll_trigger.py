""" trigger/02000163_bf/02_doll_trigger.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000102], state=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[401], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000102], stateValue=0):
            return 로봇사라짐(self.ctx)


class 로봇사라짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[401], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000102], stateValue=1):
            return 대기(self.ctx)


initial_state = 시작
