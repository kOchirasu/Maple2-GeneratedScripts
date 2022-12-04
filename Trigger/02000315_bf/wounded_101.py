""" trigger/02000315_bf/wounded_101.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='BridgeOpen', value=0)
        self.set_interact_object(triggerIds=[10001036], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001036], stateValue=0):
            return WakeUp(self.ctx)


class WakeUp(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001036], state=2)
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen', value=1):
            return Patrol01(self.ctx)
        if self.user_value(key='BridgeOpen', value=2):
            return Patrol02(self.ctx)
        if self.user_value(key='BridgeOpen', value=3):
            return Patrol03(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen', value=2):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1012')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen', value=3):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1013')


initial_state = Wait
