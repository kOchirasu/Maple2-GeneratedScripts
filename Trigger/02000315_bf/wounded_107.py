""" trigger/02000315_bf/wounded_107.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='BridgeOpen', value=0)
        self.set_interact_object(trigger_ids=[10001042], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001042], state=0):
            return WakeUp(self.ctx)


class WakeUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001042], state=2)
        self.spawn_monster(spawn_ids=[107], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen', value=3):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_1071')


initial_state = Wait
