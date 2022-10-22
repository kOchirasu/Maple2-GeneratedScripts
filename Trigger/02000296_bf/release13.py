""" trigger/02000296_bf/release13.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5011,50111,50112])
        set_interact_object(triggerIds=[10000503], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000503], arg2=0):
            return NpcSpawn01()


class NpcSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[5011,50111,50112])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcMove01()


class NpcMove01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=5011, script='$02000296_BF__NPC4__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=50111, script='$02000296_BF__NPC11__0$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=50112, script='$02000296_BF__NPC12__0$', arg4=2, arg5=2)
        move_npc(spawnId=5011, patrolName='MS2PatrolData2')
        move_npc(spawnId=50111, patrolName='MS2PatrolData2')
        move_npc(spawnId=50112, patrolName='MS2PatrolData2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return NpcRemove01()


class NpcRemove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5011,50111,50112])


