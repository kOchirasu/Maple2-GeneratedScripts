""" trigger/02000315_bf/wounded_104.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='BridgeOpen', value=0)
        self.set_interact_object(triggerIds=[10001039], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001039], stateValue=0):
            return WakeUp(self.ctx)


class WakeUp(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001039], state=2)
        self.create_monster(spawnIds=[104], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen', value=2):
            return Patrol02(self.ctx)
        if self.user_value(key='BridgeOpen', value=3):
            return Patrol03(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_1041')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen', value=3):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_1042')


initial_state = Wait
