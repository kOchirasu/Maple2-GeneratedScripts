""" trigger/66200001_gd/barrier_8120.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_interact_object(triggerIds=[10001186], state=2) # On
        self.set_interact_object(triggerIds=[10001202], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier12', value=1):
            return Sensor7121(self.ctx)
        if self.user_value(key='Barrier12', value=2):
            return Sensor7122(self.ctx)
        if self.user_value(key='Barrier12', value=3):
            return Sensor7123(self.ctx)
        if self.user_value(key='Barrier12', value=4):
            return Sensor7124(self.ctx)
        if self.user_value(key='Barrier12', value=5):
            return Sensor7125(self.ctx)


# 1명 방어 불가
class Sensor7121(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=1) # yellow

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=1, operator='Equal'):
            return Activate7121(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Activate7121(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=1, operator='Equal'):
            return Sensor7121(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7122(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_interact_object(triggerIds=[10001186], state=0) # On
        self.set_interact_object(triggerIds=[10001202], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return SafeGreen7122(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class SafeGreen7122(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return CheckSameUserTag7122(self.ctx)
        if not self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7122(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7122(self.ctx)
        if not self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122(self.ctx)
        if not self.check_same_user_tag(boxId=9120):
            return SafeGreen7122(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Enable7122(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001186], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001186], stateValue=0):
            return Activate7122(self.ctx)
        if not self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Activate7122(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=True)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001186], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7122(self.ctx)


class Delay7122(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001202], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001202], stateValue=0):
            return DeActivate7122(self.ctx)


class DeActivate7122(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7122(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7123(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_interact_object(triggerIds=[10001186], state=0) # On
        self.set_interact_object(triggerIds=[10001202], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return SafeGreen7123(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class SafeGreen7123(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return CheckSameUserTag7123(self.ctx)
        if not self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7123(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7123(self.ctx)
        if not self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123(self.ctx)
        if not self.check_same_user_tag(boxId=9120):
            return SafeGreen7123(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Enable7123(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001186], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001186], stateValue=0):
            return Activate7123(self.ctx)
        if not self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Activate7123(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=True)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001186], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7123(self.ctx)


class Delay7123(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001202], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001202], stateValue=0):
            return DeActivate7123(self.ctx)


class DeActivate7123(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7123(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7124(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_interact_object(triggerIds=[10001186], state=0) # On
        self.set_interact_object(triggerIds=[10001202], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return SafeGreen7124(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class SafeGreen7124(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return CheckSameUserTag7124(self.ctx)
        if not self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7124(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7124(self.ctx)
        if not self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124(self.ctx)
        if not self.check_same_user_tag(boxId=9120):
            return SafeGreen7124(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Enable7124(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001186], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001186], stateValue=0):
            return Activate7124(self.ctx)
        if not self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Activate7124(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=True)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001186], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7124(self.ctx)


class Delay7124(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001202], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001202], stateValue=0):
            return DeActivate7124(self.ctx)


class DeActivate7124(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7124(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7125(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_interact_object(triggerIds=[10001186], state=0) # On
        self.set_interact_object(triggerIds=[10001202], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return SafeGreen7125(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class SafeGreen7125(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return CheckSameUserTag7125(self.ctx)
        if not self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7125(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7125(self.ctx)
        if not self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125(self.ctx)
        if not self.check_same_user_tag(boxId=9120):
            return SafeGreen7125(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Enable7125(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001186], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001186], stateValue=0):
            return Activate7125(self.ctx)
        if not self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Activate7125(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=True)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001186], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7125(self.ctx)


class Delay7125(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001202], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001202], stateValue=0):
            return DeActivate7125(self.ctx)


class DeActivate7125(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7125(self.ctx)
        if self.user_value(key='Barrier12', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8120], visible=False)
        self.set_interact_object(triggerIds=[10001186], state=0) # On
        self.set_interact_object(triggerIds=[10001202], state=0) # Off
        self.set_user_value(key='Barrier12', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
