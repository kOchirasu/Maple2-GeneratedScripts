""" trigger/52100041_qd/event_03.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[171], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        move_npc(spawnId=171, patrolName='MS2PatrolData_2139')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Ready_02()


class Ready_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[171])


