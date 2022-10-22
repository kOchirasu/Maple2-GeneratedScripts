""" trigger/02000076_tw_henesysvillage/02_npcbackup04.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1002], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=False)
        move_npc(spawnId=204, patrolName='MS2PatrolData_24')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=4004, spawnIds=[204]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=204, script='$02000076_TW_HenesysVillage__02_NPCBACKUP04__0$', arg4=1)
        move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[204]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[204])
        set_timer(timerId='1', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


