""" trigger/02000296_bf/release11.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5009,50091,50092])
        set_interact_object(triggerIds=[10000501], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000501], arg2=0):
            return NpcSpawn01()


class NpcSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[5009,50091,50092])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcMove01()


class NpcMove01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=5009, script='$02000296_BF__NPC2__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=50091, script='$02000296_BF__NPC7__0$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=50092, script='$02000296_BF__NPC8__0$', arg4=2, arg5=2)
        move_npc(spawnId=5009, patrolName='MS2PatrolData2')
        move_npc(spawnId=50091, patrolName='MS2PatrolData2')
        move_npc(spawnId=50092, patrolName='MS2PatrolData2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return NpcRemove01()


class NpcRemove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5009,50091,50092])


