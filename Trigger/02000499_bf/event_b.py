""" trigger/02000499_bf/event_b.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_3012')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_3013')
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_3014')
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_3015')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[105,106,107,108]):
            return CompleteEffect(self.ctx)


class CompleteEffect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5005], visible=True)
        self.set_effect(triggerIds=[5006], visible=True)
        self.set_effect(triggerIds=[5007], visible=True)
        self.set_effect(triggerIds=[5008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return idle(self.ctx)


initial_state = idle
