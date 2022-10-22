""" trigger/52020016_qd/monster_spawn_2_3.xml """
from common import *
import state


class 체력조건(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='respawn_phase_2', value=1):
            return 전투페이즈()


class 전투페이즈(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4000103], arg2=False)
        set_conversation(type=1, spawnId=4000103, script='네녀석 처음부터 마음에 들지 않았어!!', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=20, spawnId=4000103, isRelative=True):
            return 몬스터소멸()


class 몬스터소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[4000103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return None


