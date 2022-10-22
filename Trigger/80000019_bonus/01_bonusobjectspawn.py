""" trigger/80000019_bonus/01_bonusobjectspawn.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563], isStart=False)

    def on_tick(self) -> state.State:
        if check_user():
            return SpawnOn()


class SpawnOn(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563], isStart=True)

    def on_tick(self) -> state.State:
        if not check_user():
            return SpawnOff()


class SpawnOff(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563], isStart=False)


