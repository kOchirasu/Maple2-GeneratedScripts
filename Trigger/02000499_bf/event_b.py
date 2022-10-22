""" trigger/02000499_bf/event_b.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_effect(triggerIds=[5007], visible=False)
        set_effect(triggerIds=[5008], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Start()


class Start(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_3012')
        move_npc(spawnId=106, patrolName='MS2PatrolData_3013')
        move_npc(spawnId=107, patrolName='MS2PatrolData_3014')
        move_npc(spawnId=108, patrolName='MS2PatrolData_3015')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105,106,107,108]):
            return CompleteEffect()


class CompleteEffect(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=True)
        set_effect(triggerIds=[5006], visible=True)
        set_effect(triggerIds=[5007], visible=True)
        set_effect(triggerIds=[5008], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return idle()


