""" trigger/03000267_bf/mesh.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019], visible=True, arg3=0, delay=200, scale=2)
        self.set_interact_object(triggerIds=[10000724], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000724], stateValue=0):
            return 부서짐(self.ctx)


class 부서짐(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019], visible=False, arg3=0, delay=200, scale=2)
        self.set_timer(timerId='25', seconds=25)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='25'):
            return 대기(self.ctx)


initial_state = 대기
