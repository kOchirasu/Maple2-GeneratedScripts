""" trigger/66200001_gd/barrier_8230.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10001191], state=2) # On
        self.set_interact_object(triggerIds=[10001207], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier23', value=1):
            return Sensor7231(self.ctx)
        if self.user_value(key='Barrier23', value=2):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=3):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=4):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=5):
            return Sensor7235(self.ctx)


# 1명 방어 불가
class Sensor7231(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=1, operator='Equal'):
            return Activate7231(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7231(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=1, operator='Equal'):
            return Sensor7231(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7232(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10001191], state=0) # On
        self.set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return SafeGreen7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7232(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return CheckSameUserTag7232(self.ctx)
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7232(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7232(self.ctx)
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if not self.check_same_user_tag(boxId=9230):
            return SafeGreen7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7232(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001191], stateValue=0):
            return Activate7232(self.ctx)
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7232(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7232(self.ctx)


class Delay7232(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001207], stateValue=0):
            return DeActivate7232(self.ctx)


class DeActivate7232(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7233(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10001191], state=0) # On
        self.set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return SafeGreen7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7233(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return CheckSameUserTag7233(self.ctx)
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7233(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7233(self.ctx)
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if not self.check_same_user_tag(boxId=9230):
            return SafeGreen7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7233(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001191], stateValue=0):
            return Activate7233(self.ctx)
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7233(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7233(self.ctx)


class Delay7233(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001207], stateValue=0):
            return DeActivate7233(self.ctx)


class DeActivate7233(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7234(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10001191], state=0) # On
        self.set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return SafeGreen7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7234(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return CheckSameUserTag7234(self.ctx)
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7234(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7234(self.ctx)
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if not self.check_same_user_tag(boxId=9230):
            return SafeGreen7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7234(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001191], stateValue=0):
            return Activate7234(self.ctx)
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7234(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7234(self.ctx)


class Delay7234(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001207], stateValue=0):
            return DeActivate7234(self.ctx)


class DeActivate7234(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7235(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10001191], state=0) # On
        self.set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return SafeGreen7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7235(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return CheckSameUserTag7235(self.ctx)
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7235(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7235(self.ctx)
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if not self.check_same_user_tag(boxId=9230):
            return SafeGreen7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7235(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001191], stateValue=0):
            return Activate7235(self.ctx)
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7235(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7235(self.ctx)


class Delay7235(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001207], stateValue=0):
            return DeActivate7235(self.ctx)


class DeActivate7235(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10001191], state=0) # On
        self.set_interact_object(triggerIds=[10001207], state=0) # Off
        self.set_user_value(key='Barrier23', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
