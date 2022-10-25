""" trigger/84000007_wd/barrier_8440.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_interact_object(triggerIds=[10000953], state=2) # On
        self.set_interact_object(triggerIds=[10000969], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier44', value=1):
            return Sensor7441(self.ctx)
        if self.user_value(key='Barrier44', value=2):
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44', value=3):
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44', value=4):
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44', value=5):
            return Sensor7445(self.ctx)


# 1명 방어 불가
class Sensor7441(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=1) # yellow

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=1, operator='Equal'):
            return Activate7441(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Activate7441(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=1, operator='Equal'):
            return Sensor7441(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7442(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_interact_object(triggerIds=[10000953], state=0) # On
        self.set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=2, operator='Equal'):
            return SafeGreen7442(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class SafeGreen7442(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=2, operator='Equal'):
            return Enable7442(self.ctx)
        if not self.count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Enable7442(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000953], stateValue=0):
            return Activate7442(self.ctx)
        if not self.count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Activate7442(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=True)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7442(self.ctx)


class Delay7442(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000969], stateValue=0):
            return DeActivate7442(self.ctx)


class DeActivate7442(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7442(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7443(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_interact_object(triggerIds=[10000953], state=0) # On
        self.set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=3, operator='Equal'):
            return SafeGreen7443(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class SafeGreen7443(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=3, operator='Equal'):
            return Enable7443(self.ctx)
        if not self.count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Enable7443(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000953], stateValue=0):
            return Activate7443(self.ctx)
        if not self.count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Activate7443(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=True)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7443(self.ctx)


class Delay7443(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000969], stateValue=0):
            return DeActivate7443(self.ctx)


class DeActivate7443(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7443(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7444(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_interact_object(triggerIds=[10000953], state=0) # On
        self.set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=4, operator='Equal'):
            return SafeGreen7444(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class SafeGreen7444(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=4, operator='Equal'):
            return Enable7444(self.ctx)
        if not self.count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Enable7444(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000953], stateValue=0):
            return Activate7444(self.ctx)
        if not self.count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Activate7444(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=True)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7444(self.ctx)


class Delay7444(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000969], stateValue=0):
            return DeActivate7444(self.ctx)


class DeActivate7444(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7444(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7445(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_interact_object(triggerIds=[10000953], state=0) # On
        self.set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=5, operator='Equal'):
            return SafeGreen7445(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class SafeGreen7445(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9440, boxId=5, operator='Equal'):
            return Enable7445(self.ctx)
        if not self.count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Enable7445(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000953], stateValue=0):
            return Activate7445(self.ctx)
        if not self.count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Activate7445(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=True)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7445(self.ctx)


class Delay7445(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000969], stateValue=0):
            return DeActivate7445(self.ctx)


class DeActivate7445(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7445(self.ctx)
        if self.user_value(key='Barrier44', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8440], visible=False)
        self.set_interact_object(triggerIds=[10000953], state=0) # On
        self.set_interact_object(triggerIds=[10000969], state=0) # Off
        self.set_user_value(key='Barrier44', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
