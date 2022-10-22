""" trigger/52020020_qd/main_c.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200145], questStates=[1]):
            return ready()


class ready(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=201, msg='전 밖에서 기다리고 있겠습니다.', duration=2500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return move()


class move(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return out()


class out(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])


