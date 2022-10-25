""" trigger/02000315_bf/wounded_107.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='BridgeOpen', value=0)
        self.set_interact_object(triggerIds=[10001042], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001042], stateValue=0):
            return WakeUp(self.ctx)


class WakeUp(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001042], state=2)
        self.create_monster(spawnIds=[107], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BridgeOpen', value=3):
            return Patrol03(self.ctx)


class Patrol03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_1071')


initial_state = Wait
