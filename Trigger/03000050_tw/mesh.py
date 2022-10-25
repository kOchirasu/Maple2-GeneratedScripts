""" trigger/03000050_tw/mesh.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=200, scale=2)
        self.set_interact_object(triggerIds=[10000730], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000730], stateValue=0):
            return 부서짐(self.ctx)


class 부서짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=200, scale=2)
        self.set_timer(timerId='25', seconds=25)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='25'):
            return 대기(self.ctx)


initial_state = 대기
