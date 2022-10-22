""" trigger/82000003_survival/10_ridingbattle.xml """
from common import *
import state


#  변신 탈것 riding battle 
class Setting(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514,10000515,10000516,10000517,10000518], isStart=False)
        set_user_value(key='BattleRidingOnCount', value=0)
        set_user_value(key='BattleRidingOff', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOnCount', value=1):
            return RidingSpawn()


class RidingSpawn(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514], isStart=True) # riding battle test

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
        start_combine_spawn(groupId=[10000515], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_south(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000517], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_east(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000516], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_west(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000518], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_northsouth(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000515,10000517], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_northeast(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000515,10000516], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_northwest(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000515,10000518], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_eastwest(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000516,10000518], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_southeast(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000516,10000517], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class RidingSpawn_Extra_southwest(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000518,10000517], isStart=True) # riding battle test

    def on_tick(self) -> state.State:
        if user_value(key='BattleRidingOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000507,10000508,10000509,10000510,10000511,10000512,10000513,10000514,10000515,10000516,10000517,10000518], isStart=False) # riding battle test


