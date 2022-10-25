""" trigger/52020001_qd/monster_respawn_2_3.xml """
import common


class 체력조건(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=1):
            return 몬스터사망(self.ctx)


class 몬스터사망(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[6000032]):
            return 몬스터생성(self.ctx)


class 몬스터생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[6000032], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 몬스터사망(self.ctx)


initial_state = 체력조건
