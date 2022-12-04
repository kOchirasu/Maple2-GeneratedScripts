""" trigger/80000019_bonus/01_bonusobjectspawn.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563], isStart=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return SpawnOn(self.ctx)


class SpawnOn(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_user():
            return SpawnOff(self.ctx)


class SpawnOff(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[10000549,10000550,10000551,10000552,10000553,10000554,10000555,10000556,10000557,10000558,10000559,10000560,10000561,10000562,10000563], isStart=False)


initial_state = Setting
