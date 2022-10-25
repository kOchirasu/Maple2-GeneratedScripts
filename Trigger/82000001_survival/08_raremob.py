""" trigger/82000001_survival/08_raremob.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareMobOnCount', value=0)
        self.set_user_value(key='RareMobOff', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareMobOnCount', value=1):
            return Delay(self.ctx)


class Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return MobSpawn(self.ctx)
        if self.user_value(key='RareMobOff', value=1):
            return Quit(self.ctx)


class MobSpawn(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195], isStart=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareMobOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195], isStart=False)


initial_state = Setting
