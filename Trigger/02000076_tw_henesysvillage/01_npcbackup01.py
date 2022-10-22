""" trigger/02000076_tw_henesysvillage/01_npcbackup01.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성()


class 지원군생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_11')
        set_conversation(type=1, spawnId=101, script='$02000076_TW_HenesysVillage__01_NPCBACKUP01__0$', arg4=1)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=3001, spawnIds=[101]):
            return 지원군이동()


class 지원군이동(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=2001, spawnIds=[101]):
            return 지원군소멸()


class 지원군소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        set_timer(timerId='1', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


