""" trigger/66200001_gd/sensor_9120.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box12Check', value=10)
        self.set_mesh(triggerIds=[512], visible=True, arg3=0, delay=0, scale=0) # 12 / Ground outter
        self.set_mesh(triggerIds=[5120], visible=True, arg3=0, delay=0, scale=0) # 12 / Ground inner

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Box12Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box12Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box12Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box12Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box12Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box12Check', value=5):
            return Sensor5(self.ctx)


class Sensor0(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return Fail(self.ctx)


class Sensor1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=1, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9120, boxId=1, operator='Equal'):
            return Fail(self.ctx)


class Sensor2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return Fail(self.ctx)


class Sensor3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return Fail(self.ctx)


class Sensor4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return Fail(self.ctx)


class Sensor5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return Fail(self.ctx)


class Pass(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Pass_01')
        self.set_mesh(triggerIds=[512], visible=False, arg3=0, delay=0, scale=2) # 12 / Ground outter
        self.set_user_value(triggerId=7120, key='ColorReset', value=1) # color reset

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Fail(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Fail_01')
        self.set_mesh(triggerIds=[512], visible=False, arg3=0, delay=0, scale=2) # 12 / Ground outter
        self.set_mesh(triggerIds=[5120], visible=False, arg3=0, delay=0, scale=0) # 12 / Ground inner
        self.set_user_value(triggerId=7120, key='ColorClear', value=1) # color clear

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box12Check', value=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
