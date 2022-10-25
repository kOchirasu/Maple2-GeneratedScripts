""" trigger/61000022_me/03_gamblebonus.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=False) # Firework

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GamblePass', value=22):
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='GamblePass', value=23):
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='GamblePass', value=32):
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='GamblePass', value=33):
            return GambleBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass', value=22):
            return JackpotBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass', value=23):
            return JackpotBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass', value=32):
            return JackpotBonusDelay01(self.ctx)
        if self.user_value(key='JackpotPass', value=33):
            return JackpotBonusDelay01(self.ctx)


# 한 팀이라도 큰 숫자 발판에서 통과하면 스테이지 위에 보너스 지급
class GambleBonusDelay01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='GambleSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return GambleBonusDelay02(self.ctx)


class GambleBonusDelay02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=True) # Firework

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return GambleBonus(self.ctx)


class GambleBonus(common.Trigger):
    def on_enter(self):
        self.mini_game_give_exp(boxId=9001, expRate=0.1, isOutside=False) # Gamble Pass Bonus For Everyone

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Quit(self.ctx)


class JackpotBonusDelay01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='GambleSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return JackpotBonusDelay02(self.ctx)


class JackpotBonusDelay02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=True) # Firework

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return JackpotBonus(self.ctx)


class JackpotBonus(common.Trigger):
    def on_enter(self):
        self.mini_game_give_exp(boxId=9001, expRate=0.1, isOutside=False) # Jackpot Pass Bonus For Everyone

    def on_tick(self) -> common.Trigger:
        if self.true():
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=False) # Firework
        self.set_user_value(key='GamblePass', value=0)


initial_state = Wait
