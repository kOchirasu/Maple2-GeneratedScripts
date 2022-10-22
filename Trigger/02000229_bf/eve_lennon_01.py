""" trigger/02000229_bf/eve_lennon_01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[10002180], questStates=[1]):
            return NPC이동()

    def on_exit(self):
        create_monster(spawnIds=[1001])


class NPC이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='Patrol_1001')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1001]):
            return NPC소멸()


class NPC소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        set_timer(timerId='1', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


