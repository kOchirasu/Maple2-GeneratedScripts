""" trigger/66200001_gd/barrier_8420.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_interact_object(triggerIds=[10001198], state=2) # On
        self.set_interact_object(triggerIds=[10001214], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier42', value=1):
            return Sensor7421(self.ctx)
        if self.user_value(key='Barrier42', value=2):
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42', value=3):
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42', value=4):
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42', value=5):
            return Sensor7425(self.ctx)


# 1명 방어 불가
class Sensor7421(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=1) # yellow

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=1, operator='Equal'):
            return Activate7421(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Activate7421(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=1, operator='Equal'):
            return Sensor7421(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7422(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_interact_object(triggerIds=[10001198], state=0) # On
        self.set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=2, operator='Equal'):
            return SafeGreen7422(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class SafeGreen7422(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=2, operator='Equal'):
            return CheckSameUserTag7422(self.ctx)
        if not self.count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7422(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7422(self.ctx)
        if not self.count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422(self.ctx)
        if not self.check_same_user_tag(boxId=9420):
            return SafeGreen7422(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Enable7422(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001198], stateValue=0):
            return Activate7422(self.ctx)
        if not self.count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Activate7422(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=True)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7422(self.ctx)


class Delay7422(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001214], stateValue=0):
            return DeActivate7422(self.ctx)


class DeActivate7422(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7422(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7423(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_interact_object(triggerIds=[10001198], state=0) # On
        self.set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=3, operator='Equal'):
            return SafeGreen7423(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class SafeGreen7423(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=3, operator='Equal'):
            return CheckSameUserTag7423(self.ctx)
        if not self.count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7423(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7423(self.ctx)
        if not self.count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423(self.ctx)
        if not self.check_same_user_tag(boxId=9420):
            return SafeGreen7423(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Enable7423(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001198], stateValue=0):
            return Activate7423(self.ctx)
        if not self.count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Activate7423(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=True)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7423(self.ctx)


class Delay7423(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001214], stateValue=0):
            return DeActivate7423(self.ctx)


class DeActivate7423(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7423(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7424(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_interact_object(triggerIds=[10001198], state=0) # On
        self.set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=4, operator='Equal'):
            return SafeGreen7424(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class SafeGreen7424(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=4, operator='Equal'):
            return CheckSameUserTag7424(self.ctx)
        if not self.count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7424(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7424(self.ctx)
        if not self.count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424(self.ctx)
        if not self.check_same_user_tag(boxId=9420):
            return SafeGreen7424(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Enable7424(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001198], stateValue=0):
            return Activate7424(self.ctx)
        if not self.count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Activate7424(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=True)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7424(self.ctx)


class Delay7424(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001214], stateValue=0):
            return DeActivate7424(self.ctx)


class DeActivate7424(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7424(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7425(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_interact_object(triggerIds=[10001198], state=0) # On
        self.set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=5, operator='Equal'):
            return SafeGreen7425(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class SafeGreen7425(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9420, boxId=5, operator='Equal'):
            return CheckSameUserTag7425(self.ctx)
        if not self.count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7425(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7425(self.ctx)
        if not self.count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425(self.ctx)
        if not self.check_same_user_tag(boxId=9420):
            return SafeGreen7425(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Enable7425(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001198], stateValue=0):
            return Activate7425(self.ctx)
        if not self.count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Activate7425(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=True)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7425(self.ctx)


class Delay7425(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001214], stateValue=0):
            return DeActivate7425(self.ctx)


class DeActivate7425(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7425(self.ctx)
        if self.user_value(key='Barrier42', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8420], visible=False)
        self.set_interact_object(triggerIds=[10001198], state=0) # On
        self.set_interact_object(triggerIds=[10001214], state=0) # Off
        self.set_user_value(key='Barrier42', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
