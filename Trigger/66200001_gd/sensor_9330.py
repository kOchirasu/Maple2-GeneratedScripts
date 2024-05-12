""" trigger/66200001_gd/sensor_9330.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box33Check', value=10)
        self.set_mesh(triggerIds=[533], visible=True, arg3=0, delay=0, scale=0) # 33 / Ground outter
        self.set_mesh(triggerIds=[5330], visible=True, arg3=0, delay=0, scale=0) # 33 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box33Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box33Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box33Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box33Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box33Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box33Check', value=5):
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, minUsers='1', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, minUsers='1', operator='Equal'):
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, minUsers='2', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, minUsers='2', operator='Equal'):
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, minUsers='3', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, minUsers='3', operator='Equal'):
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, minUsers='4', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, minUsers='4', operator='Equal'):
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, minUsers='5', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, minUsers='5', operator='Equal'):
            return Fail(self.ctx)


class NormalPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Pass_01')
        self.set_mesh(triggerIds=[533], visible=False, arg3=0, delay=0, scale=2) # 33 / Ground outter
        self.set_user_value(triggerId=7330, key='ColorReset', value=1) # color reset

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Fail_01')
        self.set_mesh(triggerIds=[533], visible=False, arg3=0, delay=0, scale=2) # 33 / Ground outter
        self.set_mesh(triggerIds=[5330], visible=False, arg3=0, delay=0, scale=0) # 33 / Ground inner
        self.set_user_value(triggerId=7330, key='ColorClear', value=1) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box33Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
