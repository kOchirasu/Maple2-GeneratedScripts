""" trigger/52000052_qd/803_penalty_03round.xml """
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
        self.create_monster(spawnIds=[90386,90388], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart02(self.ctx)


class FirstWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90381,90383], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart01(self.ctx)


class SecondWaveStart01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90390,90398], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveStart02(self.ctx)


class SecondWaveStart02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90393,90395], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[90380,90381,90382,90383,90384,90385,90386,90387,90388,90389,90390,90391,90392,90393,90394,90395,90396,90397,90398,90399]):
            return PenaltyFinished01(self.ctx)


class PenaltyFinished01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[90380,90381,90382,90383,90384,90385,90386,90387,90388,90389,90390,90391,90392,90393,90394,90395,90396,90397,90398,90399])
        self.set_user_value(triggerId=903, key='PenaltyFinish', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PenaltyFinished02(self.ctx)


class PenaltyFinished02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
