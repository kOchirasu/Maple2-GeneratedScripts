""" trigger/02100001_bf/04_move.xml """
import trigger_api


# 아프렐라 오지 : 산 아래에서 올라올 수 있는 발판
class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001244], state=1) # CrowMove
        self.set_breakable(triggerIds=[4502], enable=False) # Move
        self.set_visible_breakable_object(triggerIds=[4502], visible=True) # Move

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001244], stateValue=0):
            return MoveStart(self.ctx)


class MoveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4502], enable=True) # Move

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return MoveStop(self.ctx)


class MoveStop(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4502], enable=False) # Move
        self.set_visible_breakable_object(triggerIds=[4502], visible=False) # Move

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001244], state=1) # CrowMove
        self.set_visible_breakable_object(triggerIds=[4502], visible=True) # Move

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001244], stateValue=0):
            return MoveStart(self.ctx)


initial_state = Wait
