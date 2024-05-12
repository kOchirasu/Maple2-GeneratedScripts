""" trigger/66200001_gd/sensor_9230.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box23Check', value=10)
        self.set_mesh(trigger_ids=[523], visible=True, start_delay=0, interval=0, fade=0) # 23 / Ground outter
        self.set_mesh(trigger_ids=[5230], visible=True, start_delay=0, interval=0, fade=0) # 23 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box23Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box23Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box23Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box23Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box23Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box23Check', value=5):
            return Sensor5(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230, min_users='1', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9230, min_users='1', operator='Equal'):
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230, min_users='2', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9230, min_users='2', operator='Equal'):
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230, min_users='3', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9230, min_users='3', operator='Equal'):
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230, min_users='4', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9230, min_users='4', operator='Equal'):
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9230, min_users='5', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9230, min_users='5', operator='Equal'):
            return Fail(self.ctx)


class NormalPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Pass_01')
        self.set_mesh(trigger_ids=[523], visible=False, start_delay=0, interval=0, fade=2) # 23 / Ground outter
        self.set_user_value(trigger_id=7230, key='ColorReset', value=1) # color reset

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9230], sound='DDStop_Stage_Fail_01')
        self.set_mesh(trigger_ids=[523], visible=False, start_delay=0, interval=0, fade=2) # 23 / Ground outter
        self.set_mesh(trigger_ids=[5230], visible=False, start_delay=0, interval=0, fade=0) # 23 / Ground inner
        self.set_user_value(trigger_id=7230, key='ColorClear', value=1) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box23Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
