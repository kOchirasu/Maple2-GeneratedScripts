""" trigger/03000214_bf/mesh.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=True, arg3=0, delay=200, scale=2)
        self.set_interact_object(triggerIds=[10000725], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000725], stateValue=0):
            return 부서짐(self.ctx)


class 부서짐(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, delay=200, scale=2)
        self.set_timer(timerId='25', seconds=25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='25'):
            return 대기(self.ctx)


initial_state = 대기
