""" trigger/02000388_bf/anchor_02.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1505,1506,1507,1508,1509], visible=True, arg3=0, delay=0, scale=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001098], stateValue=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1505,1506,1507,1508,1509], visible=False, arg3=0, delay=0, scale=10)


initial_state = idle
