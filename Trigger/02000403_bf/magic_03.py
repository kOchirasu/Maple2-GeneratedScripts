""" trigger/02000403_bf/magic_03.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000033], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7003], visible=False)
        set_mesh(triggerIds=[1103], visible=False, arg3=0, arg4=200, arg5=15)
        set_mesh(triggerIds=[1203], visible=True, arg3=0, arg4=200, arg5=15)
        create_monster(spawnIds=[203], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[203]):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        set_achievement(triggerId=713, type='trigger', achieve='Hauntedmansion')
        create_monster(spawnIds=[165,166,167,168,169], arg2=False)
        set_npc_emotion_loop(spawnId=165, sequenceName='Down_Idle_A', duration=600000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_03_b()


class Event_03_b(state.State):
    def on_enter(self):
        move_npc(spawnId=168, patrolName='MS2PatrolData_2138')
        set_npc_emotion_loop(spawnId=165, sequenceName='Down_Idle_A', duration=600000)
        set_conversation(type=1, spawnId=165, script='$02000403_BF__MAGIC_03__0$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=169, script='$02000403_BF__MAGIC_03__1$', arg4=3, arg5=2)
        set_conversation(type=1, spawnId=168, script='$02000403_BF__MAGIC_03__2$', arg4=3, arg5=1)
        set_conversation(type=1, spawnId=168, script='$02000403_BF__MAGIC_03__3$', arg4=3, arg5=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return Event_03_c()


class Event_03_c(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[165,166,167,168,169])


