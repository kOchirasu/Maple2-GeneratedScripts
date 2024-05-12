""" trigger/61000022_me/sensor_9110.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box11Check', value=10)
        self.set_mesh(triggerIds=[511], visible=True, arg3=0, delay=0, scale=0) # 11 / Ground outter
        self.set_mesh(triggerIds=[5110], visible=True, arg3=0, delay=0, scale=0) # 11 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box11Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box11Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box11Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box11Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box11Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box11Check', value=5):
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9110, minUsers='1', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9110, minUsers='1', operator='Equal'):
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9110, minUsers='2', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9110, minUsers='2', operator='Equal'):
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9110, minUsers='3', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9110, minUsers='3', operator='Equal'):
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9110, minUsers='4', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9110, minUsers='4', operator='Equal'):
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9110, minUsers='5', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(boxId=9110, minUsers='5', operator='Equal'):
            return Fail(self.ctx)


class Pass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Pass_01')
        self.set_user_value(triggerId=7110, key='Color11', value=0) # color reset
        self.set_mesh(triggerIds=[511], visible=False, arg3=0, delay=0, scale=2) # 11 / Ground outter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Fail_01')
        self.set_mesh(triggerIds=[511], visible=False, arg3=0, delay=0, scale=2) # 11 / Ground outter
        self.set_mesh(triggerIds=[5110], visible=False, arg3=0, delay=0, scale=0) # 11 / Ground inner
        self.set_user_value(triggerId=7110, key='Color11', value=4) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box11Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
