""" trigger/66200001_gd/barrier_8220.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10001190], state=2) # On
        self.set_interact_object(triggerIds=[10001206], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier22', value=1):
            return Sensor7221(self.ctx)
        if self.user_value(key='Barrier22', value=2):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=3):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=4):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=5):
            return Sensor7225(self.ctx)


# 1명 방어 불가
class Sensor7221(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=1) # yellow

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=1, operator='Equal'):
            return Activate7221(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7221(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=1, operator='Equal'):
            return Sensor7221(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7222(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10001190], state=0) # On
        self.set_interact_object(triggerIds=[10001206], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return SafeGreen7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7222(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return CheckSameUserTag7222(self.ctx)
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7222(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7222(self.ctx)
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if not self.check_same_user_tag(boxId=9220):
            return SafeGreen7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7222(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001190], stateValue=0):
            return Activate7222(self.ctx)
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7222(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7222(self.ctx)


class Delay7222(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001206], stateValue=0):
            return DeActivate7222(self.ctx)


class DeActivate7222(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7223(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10001190], state=0) # On
        self.set_interact_object(triggerIds=[10001206], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return SafeGreen7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7223(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return CheckSameUserTag7223(self.ctx)
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7223(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7223(self.ctx)
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if not self.check_same_user_tag(boxId=9220):
            return SafeGreen7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7223(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001190], stateValue=0):
            return Activate7223(self.ctx)
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7223(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7223(self.ctx)


class Delay7223(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001206], stateValue=0):
            return DeActivate7223(self.ctx)


class DeActivate7223(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7224(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10001190], state=0) # On
        self.set_interact_object(triggerIds=[10001206], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return SafeGreen7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7224(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return CheckSameUserTag7224(self.ctx)
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7224(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7224(self.ctx)
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if not self.check_same_user_tag(boxId=9220):
            return SafeGreen7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7224(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001190], stateValue=0):
            return Activate7224(self.ctx)
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7224(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7224(self.ctx)


class Delay7224(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001206], stateValue=0):
            return DeActivate7224(self.ctx)


class DeActivate7224(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7225(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10001190], state=0) # On
        self.set_interact_object(triggerIds=[10001206], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return SafeGreen7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7225(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return CheckSameUserTag7225(self.ctx)
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class CheckSameUserTag7225(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Enable7225(self.ctx)
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if not self.check_same_user_tag(boxId=9220):
            return SafeGreen7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7225(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001190], stateValue=0):
            return Activate7225(self.ctx)
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7225(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7225(self.ctx)


class Delay7225(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10001206], stateValue=0):
            return DeActivate7225(self.ctx)


class DeActivate7225(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10001190], state=0) # On
        self.set_interact_object(triggerIds=[10001206], state=0) # Off
        self.set_user_value(key='Barrier22', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
