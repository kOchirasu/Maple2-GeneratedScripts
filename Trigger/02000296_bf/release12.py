""" trigger/02000296_bf/release12.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5010,50101,50102])
        set_interact_object(triggerIds=[10000502], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000502], arg2=0):
            return NpcSpawn01()


class NpcSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[5010,50101,50102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcMove01()


class NpcMove01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=5010, script='$02000296_BF__NPC3__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=50101, script='$02000296_BF__NPC9__0$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=50102, script='$02000296_BF__NPC10__0$', arg4=2, arg5=2)
        move_npc(spawnId=5010, patrolName='MS2PatrolData2')
        move_npc(spawnId=50101, patrolName='MS2PatrolData2')
        move_npc(spawnId=50102, patrolName='MS2PatrolData2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return NpcRemove01()


class NpcRemove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5010,50101,50102])


