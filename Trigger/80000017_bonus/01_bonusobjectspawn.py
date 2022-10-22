""" trigger/80000017_bonus/01_bonusobjectspawn.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533], isStart=False)

    def on_tick(self) -> state.State:
        if check_user():
            return SpawnOn()


class SpawnOn(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533], isStart=True)

    def on_tick(self) -> state.State:
        if not check_user():
            return SpawnOff()


class SpawnOff(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533], isStart=False)


