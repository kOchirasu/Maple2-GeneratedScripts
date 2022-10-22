""" trigger/84000007_wd/06_danceguide.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DanceGuide', value=1):
            return DanceGuideP1_Random()
        if user_value(key='DanceGuide', value=2):
            return DanceGuideP2_Random()
        if user_value(key='DanceGuide', value=3):
            return DanceGuideP3_01()
        if user_value(key='DanceGuide', value=41):
            return DanceGuideP41_01()
        if user_value(key='DanceGuide', value=42):
            return DanceGuideP42_01()
        if user_value(key='DanceGuide', value=51):
            return DanceGuideP51_01()
        if user_value(key='DanceGuide', value=52):
            return DanceGuideP52_01()
        if user_value(key='DanceGuide', value=61):
            return DanceGuideP61_01()
        if user_value(key='DanceGuide', value=62):
            return DanceGuideP62_01()
        if user_value(key='DanceGuide', value=71):
            return DanceGuideP71_01()
        if user_value(key='DanceGuide', value=72):
            return DanceGuideP72_01()


class DanceGuideP1_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return DanceGuideP11_01()
        if random_condition(rate=50):
            return DanceGuideP12_01()


class DanceGuideP2_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return DanceGuideP21_01()
        if random_condition(rate=50):
            return DanceGuideP22_01()


#  9000ms Type1
class DanceGuideP11_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DanceGuideP11_02()


class DanceGuideP11_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100802, textId=26100802, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Reset()


#  9000ms Type2
class DanceGuideP12_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DanceGuideP12_02()


class DanceGuideP12_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400703, textId=28400703, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Reset()


#  12000ms Type1 
class DanceGuideP21_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DanceGuideP21_02()


class DanceGuideP21_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100802, textId=26100802, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Reset()


#  12000ms Type2 
class DanceGuideP22_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DanceGuideP22_02()


class DanceGuideP22_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400703, textId=28400703, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Reset()


#  15000ms
class DanceGuideP3_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DanceGuideP3_02()


class DanceGuideP3_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100802, textId=26100802, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DanceGuideP3_03()


class DanceGuideP3_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400703, textId=28400703, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Reset()


#  7000ms+ 9000ms First 
class DanceGuideP41_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Reset()


#  7000ms+ 9000ms Second 
class DanceGuideP42_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100802, textId=26100802, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DanceGuideP42_02()


class DanceGuideP42_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400703, textId=28400703, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Reset()


#   9000ms+ 7000ms First 
class DanceGuideP51_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DanceGuideP51_02()


class DanceGuideP51_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400703, textId=28400703, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Reset()


#   9000ms+ 7000ms Second 
class DanceGuideP52_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100802, textId=26100802, duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Reset()


#  12000ms+ 7000ms First 
class DanceGuideP61_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DanceGuideP61_02()


class DanceGuideP61_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100802, textId=26100802, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Reset()


#  12000ms+ 7000ms Second 
class DanceGuideP62_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400703, textId=28400703, duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Reset()


#   7000ms+ 12000ms First 
class DanceGuideP71_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100801, textId=26100801, duration=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Reset()


#   7000ms+ 12000ms Second 
class DanceGuideP72_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=28400703, textId=28400703, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return DanceGuideP72_02()


class DanceGuideP72_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100802, textId=26100802, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_user_value(key='DanceGuide', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


