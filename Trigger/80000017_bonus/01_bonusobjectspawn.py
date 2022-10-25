""" trigger/80000017_bonus/01_bonusobjectspawn.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533], isStart=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return SpawnOn(self.ctx)


class SpawnOn(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533], isStart=True)

    def on_tick(self) -> common.Trigger:
        if not self.check_user():
            return SpawnOff(self.ctx)


class SpawnOff(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000519,10000520,10000521,10000522,10000523,10000524,10000525,10000526,10000527,10000528,10000529,10000530,10000531,10000532,10000533], isStart=False)


initial_state = Setting
