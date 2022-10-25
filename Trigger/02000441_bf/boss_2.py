""" trigger/02000441_bf/boss_2.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='monster_respawn', value=1):
            return 몬스터체력_75(self.ctx)


class 몬스터체력_75(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=75, spawnId=209, isRelative=True):
            return 몬스터체력_35(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[210,211,212,213], animationEffect=True)


class 몬스터체력_35(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_npc_hp(compare='lowerEqual', value=35, spawnId=209, isRelative=True):
            return 몬스터_마지막_리스폰(self.ctx)


class 몬스터_마지막_리스폰(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[214,215,216,217], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return None


initial_state = idle
