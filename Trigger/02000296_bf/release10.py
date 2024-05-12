""" trigger/02000296_bf/release10.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000500], state=1)
        self.destroy_monster(spawnIds=[5008,50081,50082])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000500], stateValue=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[5008,50081,50082])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=5008, script='$02000296_BF__NPC1__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=50081, script='$02000296_BF__NPC5__0$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=50082, script='$02000296_BF__NPC6__0$', arg4=2, arg5=2)
        self.move_npc(spawnId=5008, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50081, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50082, patrolName='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[5008,50081,50082])


initial_state = Wait
