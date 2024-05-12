""" trigger/84000007_wd/sensor_9340.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box34Check', value=10)
        self.set_mesh(trigger_ids=[534], visible=True, start_delay=0, interval=0, fade=0) # 34 / Ground outter
        self.set_mesh(trigger_ids=[5340], visible=True, start_delay=0, interval=0, fade=0) # 34 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box34Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box34Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box34Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box34Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box34Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box34Check', value=5):
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340, min_users='1', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(box_id=9340, min_users='1', operator='Equal'):
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340, min_users='2', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(box_id=9340, min_users='2', operator='Equal'):
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340, min_users='3', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(box_id=9340, min_users='3', operator='Equal'):
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340, min_users='4', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(box_id=9340, min_users='4', operator='Equal'):
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9340, min_users='5', operator='Equal'):
            return Pass(self.ctx)
        if not self.count_users(box_id=9340, min_users='5', operator='Equal'):
            return Fail(self.ctx)


class Pass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9340], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7340, key='Color34', value=0) # color reset
        self.set_mesh(trigger_ids=[534], visible=False, start_delay=0, interval=0, fade=2) # 34 / Ground outter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9340], sound='DDStop_Stage_Fail_01')
        self.set_mesh(trigger_ids=[534], visible=False, start_delay=0, interval=0, fade=2) # 34 / Ground outter
        self.set_mesh(trigger_ids=[5340], visible=False, start_delay=0, interval=0, fade=0) # 34 / Ground inner
        self.set_user_value(trigger_id=7340, key='Color34', value=4) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box34Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
