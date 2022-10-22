""" trigger/02000498_bf/timeattack_r24_01.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=140, spawnIds=[124099]):
            return 몹스폰()


class 몹스폰(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[124001], score=32000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[124099]):
            destroy_monster(spawnIds=[124001])
            return 종료()
        if monster_dead(boxIds=[124001]):
            return 몹스폰()


class 종료(state.State):
    pass


