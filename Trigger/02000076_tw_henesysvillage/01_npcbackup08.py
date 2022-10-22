""" trigger/02000076_tw_henesysvillage/01_npcbackup08.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108], arg2=False)
        move_npc(spawnId=108, patrolName='MS2PatrolData_18')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=3008, spawnIds=[108]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        move_npc(spawnId=108, patrolName='MS2PatrolData_108')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[108]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[108])
        set_timer(timerId='3', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기()

