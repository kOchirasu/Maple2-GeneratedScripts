""" trigger/80000020_bonus/01_bonusobjectspawn.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578], isStart=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return SpawnOn(self.ctx)


class SpawnOn(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578], isStart=True)

    def on_tick(self) -> common.Trigger:
        if not self.check_user():
            return SpawnOff(self.ctx)


class SpawnOff(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000564,10000565,10000566,10000567,10000568,10000569,10000570,10000571,10000572,10000573,10000574,10000575,10000576,10000577,10000578], isStart=False)


initial_state = Setting
