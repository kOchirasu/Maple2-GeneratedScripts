""" trigger/99999910/wave.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return None # Missing State: ready


#  몬스터 랜덤 생성 
class random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=12):
            return pattern_a_01()
        if random_condition(rate=12):
            return pattern_b_01()
        if random_condition(rate=12):
            return pattern_c_01()
        if random_condition(rate=12):
            return pattern_d_01()
        if random_condition(rate=6):
            return pattern_e_01()
        if random_condition(rate=6):
            return pattern_f_01()


class pattern_a_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_a_02()


class pattern_a_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_a_03()


class pattern_a_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_a_04()


class pattern_a_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_b_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_b_02()


class pattern_b_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_b_03()


class pattern_b_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_b_04()


class pattern_b_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_c_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_c_02()


class pattern_c_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_c_03()


class pattern_c_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_c_04()


class pattern_c_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_d_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_d_02()


class pattern_d_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_d_03()


class pattern_d_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_d_04()


class pattern_d_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_e_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_e_02()


class pattern_e_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_e_03()


class pattern_e_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_e_04()


class pattern_e_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_f_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_f_02()


class pattern_f_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_f_03()


class pattern_f_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return pattern_f_04()


class pattern_f_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: ready


