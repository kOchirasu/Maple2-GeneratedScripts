""" trigger/66200001_gd/barrier_8410.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_interact_object(triggerIds=[10001197], state=2) # On
        self.set_interact_object(triggerIds=[10001213], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier41', value=1):
            return Sensor7411(self.ctx)
        if self.user_value(key='Barrier41', value=2):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=3):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=4):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=5):
            return Sensor7415(self.ctx)


# 1명 방어 불가
class Sensor7411(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=1) # yellow

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=1, operator='Equal'):
            return Activate7411(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7411(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=1, operator='Equal'):
            return Sensor7411(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7412(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_interact_object(triggerIds=[10001197], state=0) # On
        self.set_interact_object(triggerIds=[10001213], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=2, operator='Equal'):
            return SafeGreen7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7412(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=2, operator='Equal'):
            return CheckSameUserTag7412(self.ctx)
        if not self.count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7412(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7412(self.ctx)
        if not self.count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412(self.ctx)
        if not self.check_same_user_tag(boxId=9410):
            return SafeGreen7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7412(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001197], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001197], stateValue=0):
            return Activate7412(self.ctx)
        if not self.count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7412(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=True)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001197], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7412(self.ctx)


class Delay7412(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001213], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001213], stateValue=0):
            return DeActivate7412(self.ctx)


class DeActivate7412(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7412(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7413(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_interact_object(triggerIds=[10001197], state=0) # On
        self.set_interact_object(triggerIds=[10001213], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=3, operator='Equal'):
            return SafeGreen7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7413(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=3, operator='Equal'):
            return CheckSameUserTag7413(self.ctx)
        if not self.count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7413(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7413(self.ctx)
        if not self.count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413(self.ctx)
        if not self.check_same_user_tag(boxId=9410):
            return SafeGreen7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7413(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001197], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001197], stateValue=0):
            return Activate7413(self.ctx)
        if not self.count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7413(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=True)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001197], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7413(self.ctx)


class Delay7413(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001213], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001213], stateValue=0):
            return DeActivate7413(self.ctx)


class DeActivate7413(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7413(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7414(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_interact_object(triggerIds=[10001197], state=0) # On
        self.set_interact_object(triggerIds=[10001213], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=4, operator='Equal'):
            return SafeGreen7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7414(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=4, operator='Equal'):
            return CheckSameUserTag7414(self.ctx)
        if not self.count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7414(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7414(self.ctx)
        if not self.count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414(self.ctx)
        if not self.check_same_user_tag(boxId=9410):
            return SafeGreen7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7414(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001197], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001197], stateValue=0):
            return Activate7414(self.ctx)
        if not self.count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7414(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=True)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001197], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7414(self.ctx)


class Delay7414(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001213], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001213], stateValue=0):
            return DeActivate7414(self.ctx)


class DeActivate7414(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7414(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7415(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_interact_object(triggerIds=[10001197], state=0) # On
        self.set_interact_object(triggerIds=[10001213], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=5, operator='Equal'):
            return SafeGreen7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class SafeGreen7415(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9410, boxId=5, operator='Equal'):
            return CheckSameUserTag7415(self.ctx)
        if not self.count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7415(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7415(self.ctx)
        if not self.count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415(self.ctx)
        if not self.check_same_user_tag(boxId=9410):
            return SafeGreen7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Enable7415(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001197], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001197], stateValue=0):
            return Activate7415(self.ctx)
        if not self.count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Activate7415(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=True)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001197], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7415(self.ctx)


class Delay7415(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001213], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001213], stateValue=0):
            return DeActivate7415(self.ctx)


class DeActivate7415(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7415(self.ctx)
        if self.user_value(key='Barrier41', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8410], visible=False)
        self.set_interact_object(triggerIds=[10001197], state=0) # On
        self.set_interact_object(triggerIds=[10001213], state=0) # Off
        self.set_user_value(key='Barrier41', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
