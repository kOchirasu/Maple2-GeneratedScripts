""" trigger/02000486_bf/101_buff.xml """
import common


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[900]):
            return 타임(self.ctx)


class 타임(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return None # Missing State: Move01


class 버프_종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 전투시작
