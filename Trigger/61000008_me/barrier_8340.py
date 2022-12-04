""" trigger/61000008_me/barrier_8340.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_interact_object(triggerIds=[10000949], state=2) # On
        self.set_interact_object(triggerIds=[10000965], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier34', value=1):
            return Sensor7341(self.ctx)
        if self.user_value(key='Barrier34', value=2):
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34', value=3):
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34', value=4):
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34', value=5):
            return Sensor7345(self.ctx)


# 1명 방어 불가
class Sensor7341(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=1, operator='Equal'):
            return Activate7341(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Activate7341(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=1, operator='Equal'):
            return Sensor7341(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7342(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_interact_object(triggerIds=[10000949], state=0) # On
        self.set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=2, operator='Equal'):
            return SafeGreen7342(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class SafeGreen7342(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=2, operator='Equal'):
            return Enable7342(self.ctx)
        if not self.count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Enable7342(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000949], stateValue=0):
            return Activate7342(self.ctx)
        if not self.count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Activate7342(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=True)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7342(self.ctx)


class Delay7342(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000965], stateValue=0):
            return DeActivate7342(self.ctx)


class DeActivate7342(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7342(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7343(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_interact_object(triggerIds=[10000949], state=0) # On
        self.set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=3, operator='Equal'):
            return SafeGreen7343(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class SafeGreen7343(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=3, operator='Equal'):
            return Enable7343(self.ctx)
        if not self.count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Enable7343(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000949], stateValue=0):
            return Activate7343(self.ctx)
        if not self.count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Activate7343(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=True)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7343(self.ctx)


class Delay7343(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000965], stateValue=0):
            return DeActivate7343(self.ctx)


class DeActivate7343(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7343(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7344(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_interact_object(triggerIds=[10000949], state=0) # On
        self.set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=4, operator='Equal'):
            return SafeGreen7344(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class SafeGreen7344(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=4, operator='Equal'):
            return Enable7344(self.ctx)
        if not self.count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Enable7344(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000949], stateValue=0):
            return Activate7344(self.ctx)
        if not self.count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Activate7344(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=True)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7344(self.ctx)


class Delay7344(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000965], stateValue=0):
            return DeActivate7344(self.ctx)


class DeActivate7344(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7344(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7345(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_interact_object(triggerIds=[10000949], state=0) # On
        self.set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=5, operator='Equal'):
            return SafeGreen7345(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class SafeGreen7345(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9340, boxId=5, operator='Equal'):
            return Enable7345(self.ctx)
        if not self.count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Enable7345(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000949], stateValue=0):
            return Activate7345(self.ctx)
        if not self.count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Activate7345(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=True)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7345(self.ctx)


class Delay7345(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000965], stateValue=0):
            return DeActivate7345(self.ctx)


class DeActivate7345(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7345(self.ctx)
        if self.user_value(key='Barrier34', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8340], visible=False)
        self.set_interact_object(triggerIds=[10000949], state=0) # On
        self.set_interact_object(triggerIds=[10000965], state=0) # Off
        self.set_user_value(key='Barrier34', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
