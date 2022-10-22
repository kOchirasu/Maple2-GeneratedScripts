""" trigger/02000498_bf/timeattack_r4_03.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=140, spawnIds=[104099]):
            return 몹스폰()


class 몹스폰(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[104003], score=4100)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104099]):
            destroy_monster(spawnIds=[104003])
            return 종료()
        if monster_dead(boxIds=[104003]):
            return 몹스폰()


class 종료(state.State):
    pass


