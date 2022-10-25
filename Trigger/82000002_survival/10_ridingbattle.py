""" trigger/82000002_survival/10_ridingbattle.xml """
import common


# 변신 탈것 riding battle
class Setting(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514,10000515,10000516,10000517,10000518], isStart=False)
        self.set_user_value(key='BattleRidingOnCount', value=0)
        self.set_user_value(key='BattleRidingOff', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOnCount', value=1):
            return RidingSpawn(self.ctx)


class RidingSpawn(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514], isStart=True) # riding battle test

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
        self.start_combine_spawn(groupId=[10000515], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_south(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000517], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_east(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000516], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_west(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000518], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_northsouth(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000515,10000517], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_northeast(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000515,10000516], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_northwest(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000515,10000518], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_eastwest(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000516,10000518], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_southeast(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000516,10000517], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class RidingSpawn_Extra_southwest(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000518,10000517], isStart=True) # riding battle test

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BattleRidingOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514,10000515,10000516,10000517,10000518], isStart=False) # riding battle test


initial_state = Setting
