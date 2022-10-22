""" trigger/02000296_bf/release10.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000500], state=1)
        destroy_monster(spawnIds=[5008,50081,50082])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000500], arg2=0):
            return NpcSpawn01()


class NpcSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[5008,50081,50082])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcMove01()


class NpcMove01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=5008, script='$02000296_BF__NPC1__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=50081, script='$02000296_BF__NPC5__0$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=50082, script='$02000296_BF__NPC6__0$', arg4=2, arg5=2)
        move_npc(spawnId=5008, patrolName='MS2PatrolData2')
        move_npc(spawnId=50081, patrolName='MS2PatrolData2')
        move_npc(spawnId=50082, patrolName='MS2PatrolData2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return NpcRemove01()


class NpcRemove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5008,50081,50082])


