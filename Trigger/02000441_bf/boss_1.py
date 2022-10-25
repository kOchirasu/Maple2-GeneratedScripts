""" trigger/02000441_bf/boss_1.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='monster_buff', value=1):
            return 몬스터_사망(self.ctx)


class 몬스터_사망(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return 초강력버프(self.ctx)


class 초강력버프(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[401,402], skillId=49200001, level=1, isPlayer=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return None


initial_state = idle
