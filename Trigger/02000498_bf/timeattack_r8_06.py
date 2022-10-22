""" trigger/02000498_bf/timeattack_r8_06.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=140, spawnIds=[108099]):
            return 몹스폰()


class 몹스폰(state.State):
    def on_enter(self):
        dark_stream(type='SpawnMonster', spawnIds=[108006], score=8000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[108099]):
            destroy_monster(spawnIds=[108006])
            return 종료()
        if monster_dead(boxIds=[108006]):
            return 몹스폰()


class 종료(state.State):
    pass


