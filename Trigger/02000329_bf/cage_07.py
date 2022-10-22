""" trigger/02000329_bf/cage_07.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6807], visible=False)
        set_actor(triggerId=207, visible=True, initialSequence='Closed')
        create_monster(spawnIds=[1007,1107], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1107]):
            return 닭생성()


class 닭생성(state.State):
    def on_enter(self):
        set_actor(triggerId=207, visible=True, initialSequence='Opened')
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[6807], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 닭이동()


class 닭이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1007, patrolName='MS2PatrolData_1007')
        set_timer(timerId='4', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 닭소멸()


class 닭소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1007])


