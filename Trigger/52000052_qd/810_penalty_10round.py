""" trigger/52000052_qd/810_penalty_10round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyMob', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PenaltyMob', value=1):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart01(self.ctx)


class FirstWaveStart01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91080,91084], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart02(self.ctx)


class FirstWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91087,91089], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart01(self.ctx)


class SecondWaveStart01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91090,91096], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveStart02(self.ctx)


class SecondWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91091,91099], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[91080,91081,91082,91083,91084,91085,91086,91087,91088,91089,91090,91091,91092,91093,91094,91095,91096,91097,91098,91099]):
            return PenaltyFinished01(self.ctx)


class PenaltyFinished01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[91080,91081,91082,91083,91084,91085,91086,91087,91088,91089,91090,91091,91092,91093,91094,91095,91096,91097,91098,91099])
        self.set_user_value(triggerId=910, key='PenaltyFinish', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PenaltyFinished02(self.ctx)


class PenaltyFinished02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
