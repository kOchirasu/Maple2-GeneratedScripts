""" trigger/65000003_bd/seagull_04.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10504]):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            move_npc(spawnId=2004, patrolName='MS2PatrolData_2004')
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2

