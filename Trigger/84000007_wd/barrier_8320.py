""" trigger/84000007_wd/barrier_8320.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=2) # On
        self.set_interact_object(triggerIds=[10000963], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier32', value=1):
            return Sensor7321(self.ctx)
        if self.user_value(key='Barrier32', value=2):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=3):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=4):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=5):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=7):
            return Sensor7327(self.ctx)
        if self.user_value(key='Barrier32', value=8):
            return Sensor7328(self.ctx)
        if self.user_value(key='Barrier32', value=9):
            return Sensor7329(self.ctx)
        if self.user_value(key='Barrier32', value=6):
            return Sensor7326(self.ctx)
        if self.user_value(key='Barrier32', value=15):
            return Sensor73215(self.ctx)
        if self.user_value(key='Barrier32', value=20):
            return Sensor73220(self.ctx)
        if self.user_value(key='Barrier32', value=25):
            return Sensor73225(self.ctx)
        if self.user_value(key='Barrier32', value=30):
            return Sensor73230(self.ctx)


# 1명 방어 불가
class Sensor7321(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=1, operator='Equal'):
            return Activate7321(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7321(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=1, operator='Equal'):
            return Sensor7321(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7322(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return SafeGreen7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7322(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Enable7322(self.ctx)
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7322(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7322(self.ctx)
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7322(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7322(self.ctx)


class Delay7322(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7322(self.ctx)


class DeActivate7322(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7323(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return SafeGreen7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7323(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Enable7323(self.ctx)
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7323(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7323(self.ctx)
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7323(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7323(self.ctx)


class Delay7323(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7323(self.ctx)


class DeActivate7323(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7324(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return SafeGreen7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7324(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Enable7324(self.ctx)
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7324(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7324(self.ctx)
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7324(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7324(self.ctx)


class Delay7324(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7324(self.ctx)


class DeActivate7324(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7325(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return SafeGreen7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7325(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Enable7325(self.ctx)
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7325(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7325(self.ctx)
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7325(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7325(self.ctx)


class Delay7325(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7325(self.ctx)


class DeActivate7325(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 7명
class Sensor7327(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=7, operator='Equal'):
            return SafeGreen7327(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7327(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=7, operator='Equal'):
            return Enable7327(self.ctx)
        if not self.count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7327(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7327(self.ctx)
        if not self.count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7327(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7327(self.ctx)


class Delay7327(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7327(self.ctx)


class DeActivate7327(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7327(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 8명
class Sensor7328(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=8, operator='Equal'):
            return SafeGreen7328(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7328(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=8, operator='Equal'):
            return Enable7328(self.ctx)
        if not self.count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7328(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7328(self.ctx)
        if not self.count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7328(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7328(self.ctx)


class Delay7328(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7328(self.ctx)


class DeActivate7328(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7328(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 9명
class Sensor7329(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=9, operator='Equal'):
            return SafeGreen7329(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7329(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=9, operator='Equal'):
            return Enable7329(self.ctx)
        if not self.count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7329(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7329(self.ctx)
        if not self.count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7329(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7329(self.ctx)


class Delay7329(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7329(self.ctx)


class DeActivate7329(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7329(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 10명
class Sensor7326(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=10, operator='Equal'):
            return SafeGreen7326(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen7326(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=10, operator='Equal'):
            return Enable7326(self.ctx)
        if not self.count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7326(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate7326(self.ctx)
        if not self.count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7326(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7326(self.ctx)


class Delay7326(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate7326(self.ctx)


class DeActivate7326(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7326(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 15명
class Sensor73215(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=15, operator='Equal'):
            return SafeGreen73215(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen73215(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=15, operator='Equal'):
            return Enable73215(self.ctx)
        if not self.count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable73215(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate73215(self.ctx)
        if not self.count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate73215(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73215(self.ctx)


class Delay73215(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate73215(self.ctx)


class DeActivate73215(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73215(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 20명
class Sensor73220(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=20, operator='Equal'):
            return SafeGreen73220(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen73220(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=20, operator='Equal'):
            return Enable73220(self.ctx)
        if not self.count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable73220(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate73220(self.ctx)
        if not self.count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate73220(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73220(self.ctx)


class Delay73220(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate73220(self.ctx)


class DeActivate73220(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73220(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 25명
class Sensor73225(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=25, operator='Equal'):
            return SafeGreen73225(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen73225(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=25, operator='Equal'):
            return Enable73225(self.ctx)
        if not self.count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable73225(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate73225(self.ctx)
        if not self.count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate73225(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73225(self.ctx)


class Delay73225(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate73225(self.ctx)


class DeActivate73225(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73225(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


# 30명
class Sensor73230(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=3) # red
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=30, operator='Equal'):
            return SafeGreen73230(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class SafeGreen73230(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9320, boxId=30, operator='Equal'):
            return Enable73230(self.ctx)
        if not self.count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable73230(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000947], stateValue=0):
            return Activate73230(self.ctx)
        if not self.count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate73230(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay73230(self.ctx)


class Delay73230(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000963], stateValue=0):
            return DeActivate73230(self.ctx)


class DeActivate73230(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor73230(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10000947], state=0) # On
        self.set_interact_object(triggerIds=[10000963], state=0) # Off
        self.set_user_value(key='Barrier32', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
