""" trigger/66200001_gd/barrier_8140.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_interact_object(trigger_ids=[10001188], state=2) # On
        self.set_interact_object(trigger_ids=[10001204], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier14', value=1):
            return Sensor7141(self.ctx)
        if self.user_value(key='Barrier14', value=2):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=3):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=4):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=5):
            return Sensor7145(self.ctx)


# 1명 방어 불가
class Sensor7141(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='1', operator='Equal'):
            return Activate7141(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7141(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='1', operator='Equal'):
            return Sensor7141(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_interact_object(trigger_ids=[10001188], state=0) # On
        self.set_interact_object(trigger_ids=[10001204], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return SafeGreen7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return CheckSameUserTag7142(self.ctx)
        if not self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7142(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9140) and self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return Enable7142(self.ctx)
        if not self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if not self.check_same_user_tag(box_id=9140):
            return SafeGreen7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001188], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001188], state=0):
            # On
            return Activate7142(self.ctx)
        if not self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001188], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7142(self.ctx)


class Delay7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001204], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001204], state=0):
            # Off
            return DeActivate7142(self.ctx)


class DeActivate7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_interact_object(trigger_ids=[10001188], state=0) # On
        self.set_interact_object(trigger_ids=[10001204], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='3', operator='Equal'):
            return SafeGreen7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='3', operator='Equal'):
            return CheckSameUserTag7143(self.ctx)
        if not self.count_users(box_id=9140, min_users='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7143(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9140) and self.count_users(box_id=9140, min_users='3', operator='Equal'):
            return Enable7143(self.ctx)
        if not self.check_same_user_tag(box_id=9140):
            return SafeGreen7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001188], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001188], state=0):
            # On
            return Activate7143(self.ctx)
        if not self.count_users(box_id=9140, min_users='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001188], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7143(self.ctx)


class Delay7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001204], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001204], state=0):
            # Off
            return DeActivate7143(self.ctx)


class DeActivate7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_interact_object(trigger_ids=[10001188], state=0) # On
        self.set_interact_object(trigger_ids=[10001204], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return SafeGreen7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return CheckSameUserTag7144(self.ctx)
        if not self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7144(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9140) and self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return Enable7144(self.ctx)
        if not self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if not self.check_same_user_tag(box_id=9140):
            return SafeGreen7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001188], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001188], state=0):
            # On
            return Activate7144(self.ctx)
        if not self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001188], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7144(self.ctx)


class Delay7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001204], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001204], state=0):
            # Off
            return DeActivate7144(self.ctx)


class DeActivate7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=1) # yellow
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_interact_object(trigger_ids=[10001188], state=0) # On
        self.set_interact_object(trigger_ids=[10001204], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return SafeGreen7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return CheckSameUserTag7145(self.ctx)
        if not self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7145(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_same_user_tag(box_id=9140) and self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return Enable7145(self.ctx)
        if not self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if not self.check_same_user_tag(box_id=9140):
            return SafeGreen7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(trigger_ids=[10001188], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001188], state=0):
            # On
            return Activate7145(self.ctx)
        if not self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=True)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001188], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return Delay7145(self.ctx)


class Delay7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001204], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(box_id=9140, min_users='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interact_ids=[10001204], state=0):
            # Off
            return DeActivate7145(self.ctx)


class DeActivate7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8141,8142,8143,8144], visible=False, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[8140], visible=False)
        self.set_interact_object(trigger_ids=[10001188], state=0) # On
        self.set_interact_object(trigger_ids=[10001204], state=0) # Off
        self.set_user_value(key='Barrier14', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
