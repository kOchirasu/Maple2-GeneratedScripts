""" trigger/02000277_bf/mesh_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000770], state=1)
        self.set_mesh(triggerIds=[10001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000770], stateValue=0):
            return 열기(self.ctx)


class 열기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10001], visible=False)
        self.set_timer(timerId='1', seconds=7)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
