""" trigger/66200001_gd/sensor_9140.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box14Check', value=10)
        self.set_mesh(triggerIds=[514], visible=True, arg3=0, delay=0, scale=0) # 14 / Ground outter
        self.set_mesh(triggerIds=[5140], visible=True, arg3=0, delay=0, scale=0) # 14 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box14Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box14Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box14Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box14Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box14Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box14Check', value=5):
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, boxId=1, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9140, boxId=1, operator='Equal'):
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, boxId=2, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9140, boxId=2, operator='Equal'):
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, boxId=3, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9140, boxId=3, operator='Equal'):
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, boxId=4, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9140, boxId=4, operator='Equal'):
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, boxId=5, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9140, boxId=5, operator='Equal'):
            return Fail(self.ctx)


class Pass(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Pass_01')
        self.set_mesh(triggerIds=[514], visible=False, arg3=0, delay=0, scale=2) # 14 / Ground outter
        self.set_user_value(triggerId=7140, key='ColorReset', value=1) # color reset

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Fail_01')
        self.set_mesh(triggerIds=[514], visible=False, arg3=0, delay=0, scale=2) # 14 / Ground outter
        self.set_mesh(triggerIds=[5140], visible=False, arg3=0, delay=0, scale=0) # 14 / Ground inner
        self.set_user_value(triggerId=7140, key='ColorClear', value=1) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box14Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
