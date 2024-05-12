""" trigger/84000007_wd/barrier_8140.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_interact_object(triggerIds=[10000941], state=2) # On
        self.set_interact_object(triggerIds=[10000957], state=2) # Off

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
        self.set_user_value(triggerId=7140, key='Color14', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='1', operator='Equal'):
            return Activate7141(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7141(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='1', operator='Equal'):
            return Sensor7141(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_interact_object(triggerIds=[10000941], state=0) # On
        self.set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='2', operator='Equal'):
            return SafeGreen7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='2', operator='Equal'):
            return Enable7142(self.ctx)
        if not self.count_users(boxId=9140, minUsers='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000941], stateValue=0):
            # On
            return Activate7142(self.ctx)
        if not self.count_users(boxId=9140, minUsers='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=True)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7142(self.ctx)


class Delay7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='2', operator='Equal'):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000957], stateValue=0):
            # Off
            return DeActivate7142(self.ctx)


class DeActivate7142(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7142(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_interact_object(triggerIds=[10000941], state=0) # On
        self.set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='3', operator='Equal'):
            return SafeGreen7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='3', operator='Equal'):
            return Enable7143(self.ctx)
        if not self.count_users(boxId=9140, minUsers='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000941], stateValue=0):
            # On
            return Activate7143(self.ctx)
        if not self.count_users(boxId=9140, minUsers='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=True)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7143(self.ctx)


class Delay7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='3', operator='Equal'):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000957], stateValue=0):
            # Off
            return DeActivate7143(self.ctx)


class DeActivate7143(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7143(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_interact_object(triggerIds=[10000941], state=0) # On
        self.set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='4', operator='Equal'):
            return SafeGreen7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='4', operator='Equal'):
            return Enable7144(self.ctx)
        if not self.count_users(boxId=9140, minUsers='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000941], stateValue=0):
            # On
            return Activate7144(self.ctx)
        if not self.count_users(boxId=9140, minUsers='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=True)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7144(self.ctx)


class Delay7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='4', operator='Equal'):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000957], stateValue=0):
            # Off
            return DeActivate7144(self.ctx)


class DeActivate7144(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7144(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_interact_object(triggerIds=[10000941], state=0) # On
        self.set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='5', operator='Equal'):
            return SafeGreen7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class SafeGreen7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9140, minUsers='5', operator='Equal'):
            return Enable7145(self.ctx)
        if not self.count_users(boxId=9140, minUsers='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Enable7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000941], stateValue=0):
            # On
            return Activate7145(self.ctx)
        if not self.count_users(boxId=9140, minUsers='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Activate7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=True)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7145(self.ctx)


class Delay7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9140, minUsers='5', operator='Equal'):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000957], stateValue=0):
            # Off
            return DeActivate7145(self.ctx)


class DeActivate7145(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7145(self.ctx)
        if self.user_value(key='Barrier14', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8140], visible=False)
        self.set_interact_object(triggerIds=[10000941], state=0) # On
        self.set_interact_object(triggerIds=[10000957], state=0) # Off
        self.set_user_value(key='Barrier14', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
