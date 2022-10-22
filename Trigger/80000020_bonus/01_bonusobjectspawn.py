""" trigger/80000020_bonus/01_bonusobjectspawn.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578], isStart=False)

    def on_tick(self) -> state.State:
        if check_user():
            return SpawnOn()


class SpawnOn(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578], isStart=True)

    def on_tick(self) -> state.State:
        if not check_user():
            return SpawnOff()


class SpawnOff(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578], isStart=False)


