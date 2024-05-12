""" trigger/03000181_bf/mesh.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=True, arg3=0, delay=300, scale=3)
        self.set_interact_object(triggerIds=[10000728], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000728], stateValue=0):
            return 부서짐(self.ctx)


class 부서짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=False, arg3=0, delay=300, scale=3)
        self.set_timer(timerId='25', seconds=25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='25'):
            return 대기(self.ctx)


initial_state = 대기
