""" trigger/02000315_bf/wounded_106.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='BridgeOpen', value=0)
        self.set_interact_object(triggerIds=[10001041], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001041], stateValue=0):
            return WakeUp(self.ctx)


class WakeUp(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001041], state=2)
        self.create_monster(spawnIds=[106], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BridgeOpen', value=3):
            return Patrol03(self.ctx)


class Patrol03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_1061')


initial_state = Wait
