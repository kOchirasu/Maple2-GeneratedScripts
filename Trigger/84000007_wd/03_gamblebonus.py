""" trigger/84000007_wd/03_gamblebonus.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=False) # Firework

    def on_tick(self) -> trigger_api.Trigger:
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
class GambleBonusDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='GambleSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GambleBonusDelay02(self.ctx)


class GambleBonusDelay02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=True) # Firework

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return GambleBonus(self.ctx)


class GambleBonus(trigger_api.Trigger):
    def on_enter(self):
        self.mini_game_give_exp(boxId=9001, expRate=0.1, isOutside=False) # Gamble Pass Bonus For Everyone

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Quit(self.ctx)


class JackpotBonusDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='GambleSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return JackpotBonusDelay02(self.ctx)


class JackpotBonusDelay02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=True) # Firework

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return JackpotBonus(self.ctx)


class JackpotBonus(trigger_api.Trigger):
    def on_enter(self):
        self.mini_game_give_exp(boxId=9001, expRate=0.1, isOutside=False) # Jackpot Pass Bonus For Everyone

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=False) # Firework
        self.set_user_value(key='GamblePass', value=0)


initial_state = Wait
