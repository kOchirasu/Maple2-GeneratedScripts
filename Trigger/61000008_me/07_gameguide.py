""" trigger/61000008_me/07_gameguide.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GameGuide', value=1):
            return GameGuideR1_30()
        if user_value(key='GameGuide', value=2):
            return GameGuideR2_20()
        if user_value(key='GameGuide', value=3):
            return GameGuideR3_15()
        if user_value(key='GameGuide', value=4):
            return GameGuideR4_10()
        if user_value(key='GameGuide', value=5):
            return GameGuideR5_10()
        if user_value(key='GameGuide', value=6):
            return GambleGuideR4_15()
        if user_value(key='GameGuide', value=7):
            return JackpotGuideR4_20()


class GameGuideR1_30(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=29, clearAtZero=True, display=False) # Round1 / 30sec

    def on_tick(self) -> state.State:
        if true():
            return NormalGameGuide_01()


class GameGuideR2_20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=19, clearAtZero=True, display=False) # Round2 / 20sec

    def on_tick(self) -> state.State:
        if true():
            return NormalGameGuide_01()


class GameGuideR3_15(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14, clearAtZero=True, display=False) # Round3 / 15sec

    def on_tick(self) -> state.State:
        if true():
            return NormalGameGuide_01()


class GameGuideR4_10(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=9, clearAtZero=True, display=False) # Round4 / 10sec

    def on_tick(self) -> state.State:
        if true():
            return NormalGameGuide_01()


class GameGuideR5_10(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=9, clearAtZero=True, display=False) # Round5 / 10sec

    def on_tick(self) -> state.State:
        if true():
            return NormalGameGuide_01()


#  Normal GameGuide
class NormalGameGuide_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100804, textId=26100804, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_02()


class NormalGameGuide_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100805, textId=26100805, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_03()
        if time_expired(timerId='1'):
            return Reset()


class NormalGameGuide_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100808, textId=26100808, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_04()
        if time_expired(timerId='1'):
            return Reset()


class NormalGameGuide_04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100804, textId=26100804, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_05()
        if time_expired(timerId='1'):
            return Reset()


class NormalGameGuide_05(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100805, textId=26100805, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NormalGameGuide_06()
        if time_expired(timerId='1'):
            return Reset()


class NormalGameGuide_06(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100808, textId=26100808, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Reset()
        if time_expired(timerId='1'):
            return Reset()


class GambleGuideR4_15(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14, clearAtZero=True, display=False) # Round4 / 15sec Gamble

    def on_tick(self) -> state.State:
        if true():
            return GambleGameGuide_01()


class JackpotGuideR4_20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=19, clearAtZero=True, display=False) # Round4 / 20sec Jackpot

    def on_tick(self) -> state.State:
        if true():
            return GambleGameGuide_01()


#  Gamble GameGuide
class GambleGameGuide_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100806, textId=26100806, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GambleGameGuide_02()


class GambleGameGuide_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100807, textId=26100807, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GambleGameGuide_03()


class GambleGameGuide_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100808, textId=26100808, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return GambleGameGuide_04()
        if time_expired(timerId='1'):
            return Reset()


class GambleGameGuide_04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100806, textId=26100806, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Reset()
        if time_expired(timerId='1'):
            return Reset()


#  Reset 
class Reset(state.State):
    def on_enter(self):
        set_user_value(key='GameGuide', value=0)
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


