""" trigger/02000329_bf/cage_08.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6808], visible=False)
        set_actor(triggerId=208, visible=True, initialSequence='Closed')
        create_monster(spawnIds=[1008,1108], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1108]):
            return 닭생성()


class 닭생성(state.State):
    def on_enter(self):
        set_actor(triggerId=208, visible=True, initialSequence='Opened')
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[6808], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 닭이동()


class 닭이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1008, patrolName='MS2PatrolData_1008')
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 닭소멸()


class 닭소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1008])


