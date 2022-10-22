""" trigger/52100041_qd/magic_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002072], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False)
        set_mesh(triggerIds=[1101], visible=False, arg3=0, arg4=200, arg5=15)
        set_mesh(triggerIds=[1201], visible=True, arg3=0, arg4=200, arg5=15)
        create_monster(spawnIds=[201], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[161,162,163], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_01_b()


class Event_01_b(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=161, sequenceName='Bore_A')
        set_npc_emotion_sequence(spawnId=162, sequenceName='Bore_A')
        set_npc_emotion_sequence(spawnId=163, sequenceName='Bore_A')
        set_conversation(type=1, spawnId=161, script='$52100041_QD__MAGIC_01__0$', arg4=3, arg5=2)
        set_conversation(type=1, spawnId=162, script='$52100041_QD__MAGIC_01__1$', arg4=3, arg5=4)
        set_conversation(type=1, spawnId=163, script='$52100041_QD__MAGIC_01__2$', arg4=3, arg5=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Event_01_c()


class Event_01_c(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[161,162,163])


