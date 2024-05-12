""" trigger/02000296_bf/release13.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[5011,50111,50112])
        self.set_interact_object(triggerIds=[10000503], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000503], stateValue=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[5011,50111,50112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=5011, script='$02000296_BF__NPC4__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=50111, script='$02000296_BF__NPC11__0$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=50112, script='$02000296_BF__NPC12__0$', arg4=2, arg5=2)
        self.move_npc(spawnId=5011, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50111, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50112, patrolName='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[5011,50111,50112])


initial_state = Wait
