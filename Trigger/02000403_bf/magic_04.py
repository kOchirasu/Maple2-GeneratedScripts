""" trigger/02000403_bf/magic_04.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000034], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7004], visible=False)
        set_mesh(triggerIds=[1104], visible=False, arg3=0, arg4=200, arg5=15)
        set_mesh(triggerIds=[1204], visible=True, arg3=0, arg4=200, arg5=15)
        create_monster(spawnIds=[204], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[204]):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_achievement(triggerId=714, type='trigger', achieve='Hauntedmansion')
        create_monster(spawnIds=[144], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_04_b()


class Event_04_b(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=144, script='$02000403_BF__MAGIC_04__0$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=144, script='$02000403_BF__MAGIC_04__1$', arg4=4, arg5=5)
        move_npc(spawnId=144, patrolName='MS2PatrolData_2134')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Event_04_c()


class Event_04_c(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=144, script='$02000403_BF__MAGIC_04__2$', arg4=3, arg5=1)
        set_conversation(type=1, spawnId=144, script='$02000403_BF__MAGIC_04__3$', arg4=3, arg5=4)
        move_npc(spawnId=144, patrolName='MS2PatrolData_2135')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Event_04_d()


class Event_04_d(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[144])


