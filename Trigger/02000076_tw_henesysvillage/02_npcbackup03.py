""" trigger/02000076_tw_henesysvillage/02_npcbackup03.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1002], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=False)
        move_npc(spawnId=203, patrolName='MS2PatrolData_23')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=4003, spawnIds=[203]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        move_npc(spawnId=203, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[203]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[203])
        set_timer(timerId='1', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


