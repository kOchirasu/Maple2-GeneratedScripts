""" trigger/02000315_bf/wounded_104.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='BridgeOpen', value=0)
        self.set_interact_object(trigger_ids=[10001039], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001039], state=0):
            return WakeUp(self.ctx)


class WakeUp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001039], state=2)
        self.spawn_monster(spawn_ids=[104], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen') >= 2:
            return Patrol02(self.ctx)
        if self.user_value(key='BridgeOpen') >= 3:
            return Patrol03(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_1041')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeOpen') >= 3:
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_1042')


initial_state = Wait
