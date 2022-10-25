""" trigger/02000296_bf/release11.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5009,50091,50092])
        self.set_interact_object(triggerIds=[10000501], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000501], stateValue=0):
            return NpcSpawn01(self.ctx)


class NpcSpawn01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[5009,50091,50092])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcMove01(self.ctx)


class NpcMove01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=5009, script='$02000296_BF__NPC2__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=50091, script='$02000296_BF__NPC7__0$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=50092, script='$02000296_BF__NPC8__0$', arg4=2, arg5=2)
        self.move_npc(spawnId=5009, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50091, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=50092, patrolName='MS2PatrolData2')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return NpcRemove01(self.ctx)


class NpcRemove01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5009,50091,50092])


initial_state = Wait
