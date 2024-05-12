""" trigger/02000296_bf/release12.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[5010,50101,50102])
        self.set_interact_object(triggerIds=[10000502], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000502], stateValue=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[5010,50101,50102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=5010, script='$02000296_BF__NPC3__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=50101, script='$02000296_BF__NPC9__0$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=50102, script='$02000296_BF__NPC10__0$', arg4=2, arg5=2)
        self.move_npc(spawnId=5010, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50101, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50102, patrolName='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[5010,50101,50102])


initial_state = Wait
