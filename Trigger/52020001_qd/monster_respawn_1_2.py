""" trigger/52020001_qd/monster_respawn_1_2.xml """
from common import *
import state


class 체력조건(state.State):
    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=70, spawnId=6000018, isRelative=True):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6000022], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


