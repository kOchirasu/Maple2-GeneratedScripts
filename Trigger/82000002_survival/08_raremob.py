""" trigger/82000002_survival/08_raremob.xml """
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
        self.start_combine_spawn(groupId=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354], isStart=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareMobOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354], isStart=False)


initial_state = Setting
