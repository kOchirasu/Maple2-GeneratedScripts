""" trigger/61000022_me/08_cheerupskill.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheerUpTimer', value=1):
            return CheerUpTimer_30(self.ctx)
        if self.user_value(key='CheerUpTimer', value=2):
            return CheerUpTimer_20(self.ctx)
        if self.user_value(key='CheerUpTimer', value=3):
            return CheerUpTimer_15(self.ctx)
        if self.user_value(key='CheerUpTimer', value=4):
            return CheerUpTimer_10(self.ctx)


class CheerUpTimer_30(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1, interval=0) # Round1 / 30sec

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=26000):
            return GiveCheerUp(self.ctx)


class CheerUpTimer_20(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20, startDelay=1, interval=0) # Round3 or Jackpot / 20sec

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=16000):
            return GiveCheerUp(self.ctx)


class CheerUpTimer_15(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=15, startDelay=1, interval=0) # Gamble / 15sec

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return GiveCheerUp(self.ctx)


class CheerUpTimer_10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10, startDelay=1, interval=0) # Round4 or Round 5 / 10sec

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return GiveCheerUp(self.ctx)


class GiveCheerUp(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9001], skillId=70000086, level=1, isPlayer=False, isSkillSet=False) # 할 수 있어 버프

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


# Reset
class Reset(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheerUpTimer', value=0)
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
