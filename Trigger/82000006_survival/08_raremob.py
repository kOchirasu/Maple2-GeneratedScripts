""" trigger/82000006_survival/08_raremob.xml """
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
        self.start_combine_spawn(groupId=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], isStart=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareMobOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], isStart=False)


initial_state = Setting
