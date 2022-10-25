""" trigger/99999910/wave.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return None # Missing State: ready


# 몬스터 랜덤 생성
class random(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=12):
            return pattern_a_01(self.ctx)
        if self.random_condition(rate=12):
            return pattern_b_01(self.ctx)
        if self.random_condition(rate=12):
            return pattern_c_01(self.ctx)
        if self.random_condition(rate=12):
            return pattern_d_01(self.ctx)
        if self.random_condition(rate=6):
            return pattern_e_01(self.ctx)
        if self.random_condition(rate=6):
            return pattern_f_01(self.ctx)


class pattern_a_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_a_02(self.ctx)


class pattern_a_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_a_03(self.ctx)


class pattern_a_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[203], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_a_04(self.ctx)


class pattern_a_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_b_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_b_02(self.ctx)


class pattern_b_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[203], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_b_03(self.ctx)


class pattern_b_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_b_04(self.ctx)


class pattern_b_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_c_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_c_02(self.ctx)


class pattern_c_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_c_03(self.ctx)


class pattern_c_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_c_04(self.ctx)


class pattern_c_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_d_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_d_02(self.ctx)


class pattern_d_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_d_03(self.ctx)


class pattern_d_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_d_04(self.ctx)


class pattern_d_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_e_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_e_02(self.ctx)


class pattern_e_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_e_03(self.ctx)


class pattern_e_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_e_04(self.ctx)


class pattern_e_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: ready


class pattern_f_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_f_02(self.ctx)


class pattern_f_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_f_03(self.ctx)


class pattern_f_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return pattern_f_04(self.ctx)


class pattern_f_04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return None # Missing State: ready


initial_state = idle
