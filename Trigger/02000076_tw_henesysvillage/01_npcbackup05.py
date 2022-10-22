""" trigger/02000076_tw_henesysvillage/01_npcbackup05.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=False)
        move_npc(spawnId=105, patrolName='MS2PatrolData_15')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=3005, spawnIds=[105]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        move_npc(spawnId=105, patrolName='MS2PatrolData_105')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[105]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105])
        set_timer(timerId='5', seconds=90)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 대기()


