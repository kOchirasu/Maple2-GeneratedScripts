""" trigger/52100011_qd/anchor_01.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1500,1501,1502,1503,1504], visible=True, arg3=0, delay=0, scale=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002055], stateValue=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1500,1501,1502,1503,1504], visible=False, arg3=0, delay=0, scale=10)


initial_state = idle
