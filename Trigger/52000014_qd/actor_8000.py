""" trigger/52000014_qd/actor_8000.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8100], visible=False) # Rage
        destroy_monster(spawnIds=[800,801])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 약화01()


class 약화01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[800], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 교체01()


class 교체01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        destroy_monster(spawnIds=[800])
        create_monster(spawnIds=[801], arg2=False)
        move_npc(spawnId=801, patrolName='MS2PatrolData_801')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 일어남01()


class 일어남01(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 포효01()


class 포효01(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=5)
        set_effect(triggerIds=[8100], visible=True) # Rage

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료01()


class 종료01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8100], visible=False) # Rage


