""" trigger/52000052_qd/811_penalty_11round.xml """
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
        self.create_monster(spawnIds=[91182,91188], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart02(self.ctx)


class FirstWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91183,91187], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart01(self.ctx)


class SecondWaveStart01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91194,91198], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveStart02(self.ctx)


class SecondWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91191,91195], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[91180,91181,91182,91183,91184,91185,91186,91187,91188,91189,91190,91191,91192,91193,91194,91195,91196,91197,91198,91199]):
            return PenaltyFinished01(self.ctx)


class PenaltyFinished01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[91180,91181,91182,91183,91184,91185,91186,91187,91188,91189,91190,91191,91192,91193,91194,91195,91196,91197,91198,91199])
        self.set_user_value(triggerId=911, key='PenaltyFinish', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PenaltyFinished02(self.ctx)


class PenaltyFinished02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
