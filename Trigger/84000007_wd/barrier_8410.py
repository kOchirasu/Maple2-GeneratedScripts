""" trigger/84000007_wd/barrier_8410.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_interact_object(trigger_ids=[10000950], state=2) # On
        self.set_interact_object(trigger_ids=[10000966], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier41', value=1):
            return Sensor7411(self.ctx)
        if self.user_value(key='Barrier41', value=2):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=3):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=4):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=5):
            return Sensor7415(self.ctx)


# 1명 방어 불가
class Sensor7411(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='1', operator='Equal'):
            return Activate7411(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7411(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='1', operator='Equal'):
            return Sensor7411(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_interact_object(trigger_ids=[10000950], state=0) # On
        self.set_interact_object(trigger_ids=[10000966], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='2', operator='Equal'):
            return SafeGreen7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='2', operator='Equal'):
            return Enable7412(self.ctx)
        if not self.count_users(box_id=9410, min_users='2', operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000950], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000950], state=0):
            # On
            return Activate7412(self.ctx)
        if not self.count_users(box_id=9410, min_users='2', operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10000950], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='2', operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7412(self.ctx)


class Delay7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000966], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='2', operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000966], state=0):
            # Off
            return DeActivate7412(self.ctx)


class DeActivate7412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_interact_object(trigger_ids=[10000950], state=0) # On
        self.set_interact_object(trigger_ids=[10000966], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='3', operator='Equal'):
            return SafeGreen7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='3', operator='Equal'):
            return Enable7413(self.ctx)
        if not self.count_users(box_id=9410, min_users='3', operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000950], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000950], state=0):
            # On
            return Activate7413(self.ctx)
        if not self.count_users(box_id=9410, min_users='3', operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10000950], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='3', operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7413(self.ctx)


class Delay7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000966], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='3', operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000966], state=0):
            # Off
            return DeActivate7413(self.ctx)


class DeActivate7413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_interact_object(trigger_ids=[10000950], state=0) # On
        self.set_interact_object(trigger_ids=[10000966], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='4', operator='Equal'):
            return SafeGreen7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='4', operator='Equal'):
            return Enable7414(self.ctx)
        if not self.count_users(box_id=9410, min_users='4', operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000950], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000950], state=0):
            # On
            return Activate7414(self.ctx)
        if not self.count_users(box_id=9410, min_users='4', operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10000950], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='4', operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7414(self.ctx)


class Delay7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000966], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='4', operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000966], state=0):
            # Off
            return DeActivate7414(self.ctx)


class DeActivate7414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=1) # yellow
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_interact_object(trigger_ids=[10000950], state=0) # On
        self.set_interact_object(trigger_ids=[10000966], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='5', operator='Equal'):
            return SafeGreen7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7410, key='Color41', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9410, min_users='5', operator='Equal'):
            return Enable7415(self.ctx)
        if not self.count_users(box_id=9410, min_users='5', operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10000950], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000950], state=0):
            # On
            return Activate7415(self.ctx)
        if not self.count_users(box_id=9410, min_users='5', operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=True)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10000950], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='5', operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7415(self.ctx)


class Delay7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000966], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9410, min_users='5', operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10000966], state=0):
            # Off
            return DeActivate7415(self.ctx)


class DeActivate7415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8411,8412,8413,8414], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8410], visible=False)
        self.set_interact_object(trigger_ids=[10000950], state=0) # On
        self.set_interact_object(trigger_ids=[10000966], state=0) # Off
        self.set_user_value(key='Barrier41', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
