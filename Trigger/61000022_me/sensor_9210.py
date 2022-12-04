""" trigger/61000022_me/sensor_9210.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box21Check', value=10)
        self.set_mesh(triggerIds=[521], visible=True, arg3=0, delay=0, scale=0) # 21 / Ground outter
        self.set_mesh(triggerIds=[5210], visible=True, arg3=0, delay=0, scale=0) # 21 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box21Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box21Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box21Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box21Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box21Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box21Check', value=5):
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=1, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9210, boxId=1, operator='Equal'):
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return Fail(self.ctx)


class Pass(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Pass_01')
        self.set_user_value(triggerId=7210, key='Color21', value=0) # color reset
        self.set_mesh(triggerIds=[521], visible=False, arg3=0, delay=0, scale=2) # 21 / Ground outter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Fail_01')
        self.set_mesh(triggerIds=[521], visible=False, arg3=0, delay=0, scale=2) # 21 / Ground outter
        self.set_mesh(triggerIds=[5210], visible=False, arg3=0, delay=0, scale=0) # 21 / Ground inner
        self.set_user_value(triggerId=7210, key='Color21', value=4) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box21Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
