""" trigger/84000007_wd/03_gamblebonus.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8001], visible=False) # Firework

    def on_tick(self) -> state.State:
        if user_value(key='GamblePass', value=22):
            return GambleBonusDelay01()
        if user_value(key='GamblePass', value=23):
            return GambleBonusDelay01()
        if user_value(key='GamblePass', value=32):
            return GambleBonusDelay01()
        if user_value(key='GamblePass', value=33):
            return GambleBonusDelay01()
        if user_value(key='JackpotPass', value=22):
            return JackpotBonusDelay01()
        if user_value(key='JackpotPass', value=23):
            return JackpotBonusDelay01()
        if user_value(key='JackpotPass', value=32):
            return JackpotBonusDelay01()
        if user_value(key='JackpotPass', value=33):
            return JackpotBonusDelay01()


#   한 팀이라도 큰 숫자 발판에서 통과하면 스테이지 위에 보너스 지급 
class GambleBonusDelay01(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='GambleSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GambleBonusDelay02()


class GambleBonusDelay02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8001], visible=True) # Firework

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GambleBonus()


class GambleBonus(state.State):
    def on_enter(self):
        mini_game_give_exp(boxId=9001, expRate=0.1, isOutside=False) # Gamble Pass Bonus For Everyone

    def on_tick(self) -> state.State:
        if true():
            return Quit()


class JackpotBonusDelay01(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='GambleSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return JackpotBonusDelay02()


class JackpotBonusDelay02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8001], visible=True) # Firework

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JackpotBonus()


class JackpotBonus(state.State):
    def on_enter(self):
        mini_game_give_exp(boxId=9001, expRate=0.1, isOutside=False) # Jackpot Pass Bonus For Everyone

    def on_tick(self) -> state.State:
        if true():
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8001], visible=False) # Firework
        set_user_value(key='GamblePass', value=0)


