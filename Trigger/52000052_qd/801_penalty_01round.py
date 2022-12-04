""" trigger/52000052_qd/801_penalty_01round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyMob', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PenaltyMob', value=1):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart01(self.ctx)


class FirstWaveStart01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90180,90188], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart02(self.ctx)


class FirstWaveStart02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90185,90189], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart01(self.ctx)


class SecondWaveStart01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90190,90192], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveStart02(self.ctx)


class SecondWaveStart02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90195,90197], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[90180,90181,90182,90183,90184,90185,90186,90187,90188,90189,90190,90191,90192,90193,90194,90195,90196,90197,90198,90199]):
            return PenaltyFinished01(self.ctx)


class PenaltyFinished01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[90180,90181,90182,90183,90184,90185,90186,90187,90188,90189,90190,90191,90192,90193,90194,90195,90196,90197,90198,90199])
        self.set_user_value(triggerId=901, key='PenaltyFinish', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PenaltyFinished02(self.ctx)


class PenaltyFinished02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
