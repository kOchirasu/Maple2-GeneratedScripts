""" trigger/52020001_qd/monster_respawn_1_2.xml """
import common


class 체력조건(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=70, spawnId=6000018, isRelative=True):
            return 몬스터생성(self.ctx)


class 몬스터생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[6000022], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 체력조건
