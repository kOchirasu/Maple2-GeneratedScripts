""" trigger/02000300_bf/ladder.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000484], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000484], stateValue=0):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016], visible=True, arg3=0, delay=0, scale=5)


initial_state = 대기
