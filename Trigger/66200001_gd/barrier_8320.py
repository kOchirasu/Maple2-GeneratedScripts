""" trigger/66200001_gd/barrier_8320.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10001194], state=2) # On
        self.set_interact_object(triggerIds=[10001210], state=2) # Off

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


# 1명 방어 불가
class Sensor7321(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7320, key='Color32', value=1) # yellow

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
        self.set_interact_object(triggerIds=[10001194], state=0) # On
        self.set_interact_object(triggerIds=[10001210], state=0) # Off

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
            return CheckSameUserTag7322(self.ctx)
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7322(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7322(self.ctx)
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if not self.check_same_user_tag(boxId=9320):
            return SafeGreen7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7322(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001194], stateValue=0):
            return Activate7322(self.ctx)
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7322(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7322(self.ctx)


class Delay7322(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001210], stateValue=0):
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
        self.set_interact_object(triggerIds=[10001194], state=0) # On
        self.set_interact_object(triggerIds=[10001210], state=0) # Off

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
            return CheckSameUserTag7323(self.ctx)
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7323(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7323(self.ctx)
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if not self.check_same_user_tag(boxId=9320):
            return SafeGreen7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7323(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001194], stateValue=0):
            return Activate7323(self.ctx)
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7323(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7323(self.ctx)


class Delay7323(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001210], stateValue=0):
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
        self.set_interact_object(triggerIds=[10001194], state=0) # On
        self.set_interact_object(triggerIds=[10001210], state=0) # Off

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
            return CheckSameUserTag7324(self.ctx)
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7324(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7324(self.ctx)
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if not self.check_same_user_tag(boxId=9320):
            return SafeGreen7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7324(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001194], stateValue=0):
            return Activate7324(self.ctx)
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7324(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7324(self.ctx)


class Delay7324(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001210], stateValue=0):
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
        self.set_interact_object(triggerIds=[10001194], state=0) # On
        self.set_interact_object(triggerIds=[10001210], state=0) # Off

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
            return CheckSameUserTag7325(self.ctx)
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7325(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7325(self.ctx)
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if not self.check_same_user_tag(boxId=9320):
            return SafeGreen7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Enable7325(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001194], stateValue=0):
            return Activate7325(self.ctx)
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)


class Activate7325(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8320], visible=True)
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7325(self.ctx)


class Delay7325(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325(self.ctx)
        if self.user_value(key='Barrier32', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001210], stateValue=0):
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


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8320], visible=False)
        self.set_interact_object(triggerIds=[10001194], state=0) # On
        self.set_interact_object(triggerIds=[10001210], state=0) # Off
        self.set_user_value(key='Barrier32', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
