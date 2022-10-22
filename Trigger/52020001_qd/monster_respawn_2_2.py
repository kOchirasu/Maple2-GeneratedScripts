""" trigger/52020001_qd/monster_respawn_2_2.xml """
from common import *
import state


class 체력조건(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=1):
            return 몬스터사망()


class 몬스터사망(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[6000031]):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6000031], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 몬스터사망()


