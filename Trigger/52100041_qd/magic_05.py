""" trigger/52100041_qd/magic_05.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002076], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7005], visible=False)
        set_mesh(triggerIds=[1105], visible=False, arg3=0, arg4=200, arg5=15)
        set_mesh(triggerIds=[1205], visible=True, arg3=0, arg4=200, arg5=15)
        create_monster(spawnIds=[205], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[205]):
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[145,146,147], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_05_b()


class Event_05_b(state.State):
    def on_enter(self):
        move_npc(spawnId=147, patrolName='MS2PatrolData_2136')
        set_conversation(type=1, spawnId=147, script='$52100041_QD__MAGIC_05__0$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=145, script='$52100041_QD__MAGIC_05__1$', arg4=3, arg5=4)
        set_conversation(type=1, spawnId=146, script='$52100041_QD__MAGIC_05__1$', arg4=3, arg5=5)
        set_conversation(type=1, spawnId=147, script='$52100041_QD__MAGIC_05__3$', arg4=3, arg5=6)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_05_c()


class Event_05_c(state.State):
    def on_enter(self):
        create_monster(spawnIds=[148], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Event_05_d()


class Event_05_d(state.State):
    def on_enter(self):
        move_npc(spawnId=148, patrolName='MS2PatrolData_2137')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_05_e()


class Event_05_e(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[145,146,147])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_05_f()


class Event_05_f(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[148])


