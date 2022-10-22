""" trigger/82000001_survival/10_ridingbattle.xml """
from common import *
import state


#  변신 탈것 riding battle 
class Setting(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337,10000338,10000339,10000340,10000341], isStart=False)
        set_user_value(key='BattleRidingOnCount', value=0)
        set_user_value(key='BattleRidingOff', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOnCount', value=1):
            return OnOffRandom()


class OnOffRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=40):
            return BattleRidingOn()
        if random_condition(rate=60):
            return BattleRidingOff()


class BattleRidingOff(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class BattleRidingOn(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DelayRandom()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class DelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return Delay_5min00sec()
        if random_condition(rate=10):
            return Delay_5min20sec()
        if random_condition(rate=10):
            return Delay_5min40sec()
        if random_condition(rate=10):
            return Delay_6min00sec()
        if random_condition(rate=10):
            return Delay_6min20sec()
        if random_condition(rate=10):
            return Delay_6min40sec()
        if random_condition(rate=10):
            return Delay_7min00sec()


class Delay_5min00sec(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300000):
            return RidingSpawn()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Delay_5min20sec(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=320000):
            return RidingSpawn()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Delay_5min40sec(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=340000):
            return RidingSpawn()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Delay_6min00sec(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=360000):
            return RidingSpawn()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Delay_6min20sec(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=380000):
            return RidingSpawn()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Delay_6min40sec(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400000):
            return RidingSpawn()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Delay_7min00sec(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=420000):
            return RidingSpawn()
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337], isStart=True) # riding battle test
        side_npc_talk(npcId=23000110, illust='Mushking_normal', duration=5000, script='$82000000_survival__10_RIDINGBATTLE__0$')

    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return RidingSpawn_Extra_none()
        if random_condition(rate=10):
            return RidingSpawn_Extra_north()
        if random_condition(rate=10):
            return RidingSpawn_Extra_south()
        if random_condition(rate=10):
            return RidingSpawn_Extra_east()
        if random_condition(rate=10):
            return RidingSpawn_Extra_west()
        if random_condition(rate=10):
            return RidingSpawn_Extra_northsouth()
        if random_condition(rate=10):
            return RidingSpawn_Extra_northeast()
        if random_condition(rate=10):
            return RidingSpawn_Extra_northwest()
        if random_condition(rate=10):
            return RidingSpawn_Extra_eastwest()
        if random_condition(rate=10):
            return RidingSpawn_Extra_southeast()
        if random_condition(rate=10):
            return RidingSpawn_Extra_southwest()


class RidingSpawn_Extra_none(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_north(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000338], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_south(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000340], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_east(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000339], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_west(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000341], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_northsouth(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000338,10000340], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_northeast(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000338,10000339], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_northwest(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000338,10000341], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_eastwest(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000339,10000341], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_southeast(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000339,10000340], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_southwest(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000341,10000340], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337,10000338,10000339,10000340,10000341], isStart=False) # riding battle test


