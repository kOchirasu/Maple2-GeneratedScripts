""" trigger/66200001_gd/barrier_8210.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_interact_object(triggerIds=[10001189], state=2) # On
        self.set_interact_object(triggerIds=[10001205], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier21', value=1):
            return Sensor7211(self.ctx)
        if self.user_value(key='Barrier21', value=2):
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21', value=3):
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21', value=4):
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21', value=5):
            return Sensor7215(self.ctx)


# 1명 방어 불가
class Sensor7211(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=1, operator='Equal'):
            return Activate7211(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Activate7211(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=1, operator='Equal'):
            return Sensor7211(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7212(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_interact_object(triggerIds=[10001189], state=0) # On
        self.set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return SafeGreen7212(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class SafeGreen7212(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return CheckSameUserTag7212(self.ctx)
        if not self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7212(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return Enable7212(self.ctx)
        if not self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212(self.ctx)
        if not self.check_same_user_tag(boxId=9210):
            return SafeGreen7212(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Enable7212(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001189], stateValue=0):
            return Activate7212(self.ctx)
        if not self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Activate7212(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=True)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7212(self.ctx)


class Delay7212(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001205], stateValue=0):
            return DeActivate7212(self.ctx)


class DeActivate7212(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7212(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7213(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_interact_object(triggerIds=[10001189], state=0) # On
        self.set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return SafeGreen7213(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class SafeGreen7213(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return CheckSameUserTag7213(self.ctx)
        if not self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7213(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return Enable7213(self.ctx)
        if not self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213(self.ctx)
        if not self.check_same_user_tag(boxId=9210):
            return SafeGreen7213(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Enable7213(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001189], stateValue=0):
            return Activate7213(self.ctx)
        if not self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Activate7213(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=True)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7213(self.ctx)


class Delay7213(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001205], stateValue=0):
            return DeActivate7213(self.ctx)


class DeActivate7213(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7213(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7214(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_interact_object(triggerIds=[10001189], state=0) # On
        self.set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return SafeGreen7214(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class SafeGreen7214(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return CheckSameUserTag7214(self.ctx)
        if not self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7214(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return Enable7214(self.ctx)
        if not self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214(self.ctx)
        if not self.check_same_user_tag(boxId=9210):
            return SafeGreen7214(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Enable7214(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001189], stateValue=0):
            return Activate7214(self.ctx)
        if not self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Activate7214(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=True)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7214(self.ctx)


class Delay7214(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001205], stateValue=0):
            return DeActivate7214(self.ctx)


class DeActivate7214(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7214(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7215(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_interact_object(triggerIds=[10001189], state=0) # On
        self.set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return SafeGreen7215(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class SafeGreen7215(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return CheckSameUserTag7215(self.ctx)
        if not self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7215(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return Enable7215(self.ctx)
        if not self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215(self.ctx)
        if not self.check_same_user_tag(boxId=9210):
            return SafeGreen7215(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Enable7215(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001189], stateValue=0):
            return Activate7215(self.ctx)
        if not self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Activate7215(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=True)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7215(self.ctx)


class Delay7215(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001205], stateValue=0):
            return DeActivate7215(self.ctx)


class DeActivate7215(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7215(self.ctx)
        if self.user_value(key='Barrier21', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_interact_object(triggerIds=[10001189], state=0) # On
        self.set_interact_object(triggerIds=[10001205], state=0) # Off
        self.set_user_value(key='Barrier21', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
