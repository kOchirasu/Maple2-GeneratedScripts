""" trigger/99999909/triggerbox_101.xml """
import trigger_api


class 블록(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008,3009], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 블록생성(self.ctx)


class 블록생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_random_mesh(triggerIds=[3002,3003,3004,3005,3006,3007,3008,3009], visible=True, meshCount=4, arg4=0, delay=1)


initial_state = 블록
