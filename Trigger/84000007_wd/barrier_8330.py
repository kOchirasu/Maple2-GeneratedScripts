""" trigger/84000007_wd/barrier_8330.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=2) # On
        self.set_interact_object(triggerIds=[10000964], state=2) # Off

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
        if self.user_value(key='Barrier33', value=7):
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33', value=8):
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33', value=9):
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33', value=6):
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33', value=15):
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33', value=20):
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33', value=25):
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33', value=30):
            return Sensor73330(self.ctx)


# 1명 방어 불가
class Sensor7331(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=1, operator='Equal'):
            return Activate7331(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7331(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=1, operator='Equal'):
            return Sensor7331(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7332(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return SafeGreen7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7332(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return Enable7332(self.ctx)
        if not self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7332(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7332(self.ctx)
        if not self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7332(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7332(self.ctx)


class Delay7332(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7332(self.ctx)


class DeActivate7332(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7332(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7333(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return SafeGreen7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7333(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return Enable7333(self.ctx)
        if not self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7333(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7333(self.ctx)
        if not self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7333(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7333(self.ctx)


class Delay7333(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7333(self.ctx)


class DeActivate7333(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7333(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7334(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return SafeGreen7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7334(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return Enable7334(self.ctx)
        if not self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7334(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7334(self.ctx)
        if not self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7334(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7334(self.ctx)


class Delay7334(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7334(self.ctx)


class DeActivate7334(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7334(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7335(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return SafeGreen7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7335(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return Enable7335(self.ctx)
        if not self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7335(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7335(self.ctx)
        if not self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7335(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7335(self.ctx)


class Delay7335(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7335(self.ctx)


class DeActivate7335(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7335(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 7명
class Sensor7337(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return SafeGreen7337(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7337(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return Enable7337(self.ctx)
        if not self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7337(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7337(self.ctx)
        if not self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7337(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7337(self.ctx)


class Delay7337(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7337(self.ctx)


class DeActivate7337(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7337(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 8명
class Sensor7338(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return SafeGreen7338(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7338(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return Enable7338(self.ctx)
        if not self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7338(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7338(self.ctx)
        if not self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7338(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7338(self.ctx)


class Delay7338(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7338(self.ctx)


class DeActivate7338(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7338(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 9명
class Sensor7339(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return SafeGreen7339(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7339(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return Enable7339(self.ctx)
        if not self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7339(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7339(self.ctx)
        if not self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7339(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7339(self.ctx)


class Delay7339(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7339(self.ctx)


class DeActivate7339(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7339(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 10명
class Sensor7336(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return SafeGreen7336(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen7336(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return Enable7336(self.ctx)
        if not self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable7336(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate7336(self.ctx)
        if not self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate7336(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7336(self.ctx)


class Delay7336(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate7336(self.ctx)


class DeActivate7336(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7336(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 15명
class Sensor73315(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return SafeGreen73315(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen73315(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return Enable73315(self.ctx)
        if not self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable73315(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate73315(self.ctx)
        if not self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate73315(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73315(self.ctx)


class Delay73315(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate73315(self.ctx)


class DeActivate73315(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73315(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 20명
class Sensor73320(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return SafeGreen73320(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen73320(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return Enable73320(self.ctx)
        if not self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable73320(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate73320(self.ctx)
        if not self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate73320(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73320(self.ctx)


class Delay73320(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate73320(self.ctx)


class DeActivate73320(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73320(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 25명
class Sensor73325(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return SafeGreen73325(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen73325(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return Enable73325(self.ctx)
        if not self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable73325(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate73325(self.ctx)
        if not self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate73325(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73325(self.ctx)


class Delay73325(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate73325(self.ctx)


class DeActivate73325(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73325(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


# 30명
class Sensor73330(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=3) # red
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return SafeGreen73330(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class SafeGreen73330(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return Enable73330(self.ctx)
        if not self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Enable73330(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000948], stateValue=0):
            return Activate73330(self.ctx)
        if not self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Activate73330(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=True)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73330(self.ctx)


class Delay73330(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000964], stateValue=0):
            return DeActivate73330(self.ctx)


class DeActivate73330(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73330(self.ctx)
        if self.user_value(key='Barrier33', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8330], visible=False)
        self.set_interact_object(triggerIds=[10000948], state=0) # On
        self.set_interact_object(triggerIds=[10000964], state=0) # Off
        self.set_user_value(key='Barrier33', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
