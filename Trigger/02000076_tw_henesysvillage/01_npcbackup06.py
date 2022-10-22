""" trigger/02000076_tw_henesysvillage/01_npcbackup06.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[106], arg2=False)
        move_npc(spawnId=106, patrolName='MS2PatrolData_16')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=3006, spawnIds=[106]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        move_npc(spawnId=106, patrolName='MS2PatrolData_106')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[106]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[106])
        set_timer(timerId='6', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 대기()


