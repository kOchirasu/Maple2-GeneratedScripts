""" trigger/52020010_qd/door_open.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5016], visible=False) # 우르르 쾅쾅
        self.set_effect(triggerIds=[5017], visible=False) # 먼지
        self.set_breakable(triggerIds=[10001], enable=False)
        self.set_breakable(triggerIds=[10002], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[2]):
            return Check(self.ctx)
        if self.quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[3]):
            return Check(self.ctx)


class Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001275], stateValue=0):
            return DoorOpen(self.ctx)


class DoorOpen(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5016], visible=True) # 우르르 쾅쾅
        self.set_effect(triggerIds=[5017], visible=True) # 먼지
        self.set_breakable(triggerIds=[10001], enable=True)
        self.set_breakable(triggerIds=[10002], enable=True)


initial_state = Idle
