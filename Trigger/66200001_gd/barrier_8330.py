""" trigger/66200001_gd/barrier_8330.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_interact_object(trigger_ids=[10001195], state=2) # On
        self.set_interact_object(trigger_ids=[10001211], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier33', value=1):
            return Sensor7331(self.ctx)
        if self.user_value(key='Barrier33', value=2):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=3):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=4):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=5):
            return Sensor7335(self.ctx)


# 1명 방어 불가
class Sensor7331(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='1', operator='Equal'):
            return Activate7331(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7331(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='1', operator='Equal'):
            return Sensor7331(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_interact_object(trigger_ids=[10001195], state=0) # On
        self.set_interact_object(trigger_ids=[10001211], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return SafeGreen7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return CheckSameUserTag7332(self.ctx)
        if not self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7332(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9330) and self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return Enable7332(self.ctx)
        if not self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return Sensor7332(self.ctx)
        if not self.check_same_user_tag(box_id=9330):
            return SafeGreen7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001195], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001195], state=0):
            # On
            return Activate7332(self.ctx)
        if not self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001195], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7332(self.ctx)


class Delay7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001211], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='2', operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001211], state=0):
            # Off
            return DeActivate7332(self.ctx)


class DeActivate7332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_interact_object(trigger_ids=[10001195], state=0) # On
        self.set_interact_object(trigger_ids=[10001211], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return SafeGreen7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return CheckSameUserTag7333(self.ctx)
        if not self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7333(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9330) and self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return Enable7333(self.ctx)
        if not self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return Sensor7333(self.ctx)
        if not self.check_same_user_tag(box_id=9330):
            return SafeGreen7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001195], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001195], state=0):
            # On
            return Activate7333(self.ctx)
        if not self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001195], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7333(self.ctx)


class Delay7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001211], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='3', operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001211], state=0):
            # Off
            return DeActivate7333(self.ctx)


class DeActivate7333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_interact_object(trigger_ids=[10001195], state=0) # On
        self.set_interact_object(trigger_ids=[10001211], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return SafeGreen7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return CheckSameUserTag7334(self.ctx)
        if not self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7334(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9330) and self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return Enable7334(self.ctx)
        if not self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return Sensor7334(self.ctx)
        if not self.check_same_user_tag(box_id=9330):
            return SafeGreen7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001195], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001195], state=0):
            # On
            return Activate7334(self.ctx)
        if not self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001195], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7334(self.ctx)


class Delay7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001211], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='4', operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001211], state=0):
            # Off
            return DeActivate7334(self.ctx)


class DeActivate7334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=1) # yellow
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_interact_object(trigger_ids=[10001195], state=0) # On
        self.set_interact_object(trigger_ids=[10001211], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return SafeGreen7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return CheckSameUserTag7335(self.ctx)
        if not self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7335(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9330) and self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return Enable7335(self.ctx)
        if not self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return Sensor7335(self.ctx)
        if not self.check_same_user_tag(box_id=9330):
            return SafeGreen7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001195], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001195], state=0):
            # On
            return Activate7335(self.ctx)
        if not self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=True)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001195], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7335(self.ctx)


class Delay7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001211], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9330, min_users='5', operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001211], state=0):
            # Off
            return DeActivate7335(self.ctx)


class DeActivate7335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8330], visible=False)
        self.set_interact_object(trigger_ids=[10001195], state=0) # On
        self.set_interact_object(trigger_ids=[10001211], state=0) # Off
        self.set_user_value(key='Barrier33', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
