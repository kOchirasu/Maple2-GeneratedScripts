""" trigger/02000329_bf/cage_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6801], visible=False)
        set_actor(triggerId=201, visible=True, initialSequence='Closed')
        create_monster(spawnIds=[1001,1101], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1101]):
            return 닭생성()


class 닭생성(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=True, initialSequence='Opened')
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[6601], visible=False)
        set_effect(triggerIds=[6801], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 닭이동()


class 닭이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001')
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 닭소멸()


class 닭소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])


