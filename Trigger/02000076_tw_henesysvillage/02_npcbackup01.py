""" trigger/02000076_tw_henesysvillage/02_npcbackup01.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1002], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_21')
        set_conversation(type=1, spawnId=201, script='$02000076_TW_HenesysVillage__02_NPCBACKUP01__0$', arg4=1)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=4001, spawnIds=[201]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[201]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])
        set_timer(timerId='1', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


