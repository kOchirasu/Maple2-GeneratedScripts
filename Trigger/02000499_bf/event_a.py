""" trigger/02000499_bf/event_a.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3008')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3009')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_3010')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104]):
            return CompleteEffect(self.ctx)


class CompleteEffect(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return idle(self.ctx)


initial_state = idle
