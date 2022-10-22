""" trigger/80000018_bonus/01_bonusobjectspawn.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000534,10000535,10000536,10000537,10000538,10000539,10000540,10000541,10000542,10000543,10000544,10000545,10000546,10000547,10000548], isStart=False)

    def on_tick(self) -> state.State:
        if check_user():
            return SpawnOn()


class SpawnOn(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000534,10000535,10000536,10000537,10000538,10000539,10000540,10000541,10000542,10000543,10000544,10000545,10000546,10000547,10000548], isStart=True)

    def on_tick(self) -> state.State:
        if not check_user():
            return SpawnOff()


class SpawnOff(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000534,10000535,10000536,10000537,10000538,10000539,10000540,10000541,10000542,10000543,10000544,10000545,10000546,10000547,10000548], isStart=False)


