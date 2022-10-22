""" trigger/52010015_qd/act01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002824], questStates=[2]):
            return 딜레이01()


class 딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='100', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100'):
            return 미카교체01()


#   1st Quest 
class 미카교체01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 미카이동01()


class 미카이동01(state.State):
    def on_enter(self):
        move_npc(spawnId=202, patrolName='MS2PatrolData_2020')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=8000, spawnIds=[202]):
            return 미카소멸01()


class 미카소멸01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])


