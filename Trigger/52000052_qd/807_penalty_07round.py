""" trigger/52000052_qd/807_penalty_07round.xml """
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
        self.create_monster(spawnIds=[90780,90784], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart02(self.ctx)


class FirstWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90787,90789], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart01(self.ctx)


class SecondWaveStart01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90792,90798], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveStart02(self.ctx)


class SecondWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90791,90795], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[90780,90781,90782,90783,90784,90785,90786,90787,90788,90789,90790,90791,90792,90793,90794,90795,90796,90797,90798,90799]):
            return PenaltyFinished01(self.ctx)


class PenaltyFinished01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[90780,90781,90782,90783,90784,90785,90786,90787,90788,90789,90790,90791,90792,90793,90794,90795,90796,90797,90798,90799])
        self.set_user_value(triggerId=907, key='PenaltyFinish', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PenaltyFinished02(self.ctx)


class PenaltyFinished02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
