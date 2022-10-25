""" trigger/61000022_me/07_gameguide.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GameGuide', value=1):
            return GameGuideR1_30(self.ctx)
        if self.user_value(key='GameGuide', value=2):
            return GameGuideR2_20(self.ctx)
        if self.user_value(key='GameGuide', value=3):
            return GameGuideR3_15(self.ctx)
        if self.user_value(key='GameGuide', value=4):
            return GameGuideR4_10(self.ctx)
        if self.user_value(key='GameGuide', value=5):
            return GameGuideR5_10(self.ctx)
        if self.user_value(key='GameGuide', value=6):
            return GambleGuideR4_15(self.ctx)
        if self.user_value(key='GameGuide', value=7):
            return JackpotGuideR4_20(self.ctx)


class GameGuideR1_30(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=29, startDelay=1, interval=0) # Round1 / 30sec

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NormalGameGuide_01(self.ctx)


class GameGuideR2_20(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=19, startDelay=1, interval=0) # Round2 / 20sec

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NormalGameGuide_01(self.ctx)


class GameGuideR3_15(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=14, startDelay=1, interval=0) # Round3 / 15sec

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NormalGameGuide_01(self.ctx)


class GameGuideR4_10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=9, startDelay=1, interval=0) # Round4 / 10sec

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NormalGameGuide_01(self.ctx)


class GameGuideR5_10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=9, startDelay=1, interval=0) # Round5 / 10sec

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NormalGameGuide_01(self.ctx)


# Normal GameGuide
class NormalGameGuide_01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100804, textId=26100804, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_02(self.ctx)


class NormalGameGuide_02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100805, textId=26100805, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_03(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class NormalGameGuide_03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100808, textId=26100808, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_04(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class NormalGameGuide_04(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100804, textId=26100804, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_05(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class NormalGameGuide_05(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100805, textId=26100805, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_06(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class NormalGameGuide_06(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100808, textId=26100808, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Reset(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class GambleGuideR4_15(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=14, startDelay=1, interval=0) # Round4 / 15sec Gamble

    def on_tick(self) -> common.Trigger:
        if self.true():
            return GambleGameGuide_01(self.ctx)


class JackpotGuideR4_20(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=19, startDelay=1, interval=0) # Round4 / 20sec Jackpot

    def on_tick(self) -> common.Trigger:
        if self.true():
            return GambleGameGuide_01(self.ctx)


# Gamble GameGuide
class GambleGameGuide_01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100806, textId=26100806, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return GambleGameGuide_02(self.ctx)


class GambleGameGuide_02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100807, textId=26100807, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return GambleGameGuide_03(self.ctx)


class GambleGameGuide_03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100808, textId=26100808, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return GambleGameGuide_04(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class GambleGameGuide_04(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100806, textId=26100806, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Reset(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


# Reset
class Reset(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='GameGuide', value=0)
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
