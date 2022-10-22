""" trigger/02000499_bf/event_a.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Start()


class Start(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3008')
        move_npc(spawnId=102, patrolName='MS2PatrolData_3009')
        move_npc(spawnId=103, patrolName='MS2PatrolData_3010')
        move_npc(spawnId=104, patrolName='MS2PatrolData_3011')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104]):
            return CompleteEffect()


class CompleteEffect(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return idle()


