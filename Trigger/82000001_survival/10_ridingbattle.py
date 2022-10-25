""" trigger/82000001_survival/10_ridingbattle.xml """
import common


# 변신 탈것 riding battle
class Setting(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337,10000338,10000339,10000340,10000341], isStart=False)
        self.set_user_value(key='BattleRidingOnCount', value=0)
        self.set_user_value(key='BattleRidingOff', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOnCount', value=1):
            return OnOffRandom(self.ctx)


class OnOffRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=40):
            return BattleRidingOn(self.ctx)
        if self.random_condition(rate=60):
            return BattleRidingOff(self.ctx)


class BattleRidingOff(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class BattleRidingOn(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DelayRandom(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class DelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Delay_5min00sec(self.ctx)
        if self.random_condition(rate=10):
            return Delay_5min20sec(self.ctx)
        if self.random_condition(rate=10):
            return Delay_5min40sec(self.ctx)
        if self.random_condition(rate=10):
            return Delay_6min00sec(self.ctx)
        if self.random_condition(rate=10):
            return Delay_6min20sec(self.ctx)
        if self.random_condition(rate=10):
            return Delay_6min40sec(self.ctx)
        if self.random_condition(rate=10):
            return Delay_7min00sec(self.ctx)


class Delay_5min00sec(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300000):
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Delay_5min20sec(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=320000):
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Delay_5min40sec(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=340000):
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Delay_6min00sec(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=360000):
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Delay_6min20sec(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=380000):
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Delay_6min40sec(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=400000):
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Delay_7min00sec(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=420000):
            return RidingSpawn(self.ctx)
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337], isStart=True) # riding battle test
        self.side_npc_talk(npcId=23000110, illust='Mushking_normal', duration=5000, script='$82000000_survival__10_RIDINGBATTLE__0$')

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_none(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_north(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_south(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_east(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_west(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_northsouth(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_northeast(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_northwest(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_eastwest(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_southeast(self.ctx)
        if self.random_condition(rate=10):
            return RidingSpawn_Extra_southwest(self.ctx)


class RidingSpawn_Extra_none(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_north(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000338], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_south(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000340], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_east(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000339], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_west(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000341], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_northsouth(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000338,10000340], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_northeast(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000338,10000339], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_northwest(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000338,10000341], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_eastwest(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000339,10000341], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_southeast(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000339,10000340], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_southwest(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000341,10000340], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000330,10000331,10000332,10000333,10000334,10000335,10000336,10000337,10000338,10000339,10000340,10000341], isStart=False) # riding battle test


initial_state = Setting
