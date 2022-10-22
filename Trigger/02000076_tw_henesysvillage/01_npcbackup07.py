""" trigger/02000076_tw_henesysvillage/01_npcbackup07.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[107], arg2=False)
        move_npc(spawnId=107, patrolName='MS2PatrolData_17')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=3007, spawnIds=[107]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=104, script='$02000076_TW_HenesysVillage__01_NPCBACKUP07__0$', arg4=1)
        move_npc(spawnId=107, patrolName='MS2PatrolData_107')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[107]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[107])
        set_timer(timerId='3', seconds=90)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기()


