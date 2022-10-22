""" trigger/52020016_qd/monster_spawn_1_2.xml """
from common import *
import state


class 체력조건(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='respawn_phase_1', value=1):
            return 전투페이즈()


class 전투페이즈(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4000002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4000002]):
            return 몬스터리젠()
        if user_value(key='respawn_phase_1_end', value=1):
            return 끝()


class 몬스터리젠(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4000004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4000004]):
            return 전투페이즈()
        if user_value(key='respawn_phase_1_end', value=1):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[4000002], arg2=False)
        destroy_monster(spawnIds=[4000004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return None


