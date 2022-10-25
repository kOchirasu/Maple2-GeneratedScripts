""" trigger/61000022_me/barrier_8220.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=2) # On
        self.set_interact_object(triggerIds=[10000959], state=2) # Off

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
        if self.user_value(key='Barrier22', value=7):
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22', value=8):
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22', value=9):
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22', value=6):
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22', value=15):
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22', value=20):
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22', value=25):
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22', value=30):
            return Sensor72230(self.ctx)


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
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

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
            return Enable7222(self.ctx)
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7222(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7222(self.ctx)
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7222(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7222(self.ctx)


class Delay7222(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
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
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

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
            return Enable7223(self.ctx)
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7223(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7223(self.ctx)
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7223(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7223(self.ctx)


class Delay7223(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
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
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

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
            return Enable7224(self.ctx)
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7224(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7224(self.ctx)
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7224(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7224(self.ctx)


class Delay7224(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
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
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

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
            return Enable7225(self.ctx)
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7225(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7225(self.ctx)
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7225(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7225(self.ctx)


class Delay7225(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
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


# 7명
class Sensor7227(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=7, operator='Equal'):
            return SafeGreen7227(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7227(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=7, operator='Equal'):
            return Enable7227(self.ctx)
        if not self.count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7227(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7227(self.ctx)
        if not self.count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7227(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7227(self.ctx)


class Delay7227(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate7227(self.ctx)


class DeActivate7227(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7227(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 8명
class Sensor7228(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=8, operator='Equal'):
            return SafeGreen7228(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7228(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=8, operator='Equal'):
            return Enable7228(self.ctx)
        if not self.count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7228(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7228(self.ctx)
        if not self.count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7228(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7228(self.ctx)


class Delay7228(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate7228(self.ctx)


class DeActivate7228(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7228(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 9명
class Sensor7229(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=9, operator='Equal'):
            return SafeGreen7229(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7229(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=9, operator='Equal'):
            return Enable7229(self.ctx)
        if not self.count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7229(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7229(self.ctx)
        if not self.count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7229(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7229(self.ctx)


class Delay7229(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate7229(self.ctx)


class DeActivate7229(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7229(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 10명
class Sensor7226(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=10, operator='Equal'):
            return SafeGreen7226(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen7226(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=10, operator='Equal'):
            return Enable7226(self.ctx)
        if not self.count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable7226(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate7226(self.ctx)
        if not self.count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate7226(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7226(self.ctx)


class Delay7226(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate7226(self.ctx)


class DeActivate7226(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7226(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 15명
class Sensor72215(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=15, operator='Equal'):
            return SafeGreen72215(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen72215(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=15, operator='Equal'):
            return Enable72215(self.ctx)
        if not self.count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable72215(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate72215(self.ctx)
        if not self.count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate72215(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72215(self.ctx)


class Delay72215(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate72215(self.ctx)


class DeActivate72215(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72215(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 20명
class Sensor72220(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=20, operator='Equal'):
            return SafeGreen72220(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen72220(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=20, operator='Equal'):
            return Enable72220(self.ctx)
        if not self.count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable72220(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate72220(self.ctx)
        if not self.count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate72220(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72220(self.ctx)


class Delay72220(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate72220(self.ctx)


class DeActivate72220(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72220(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 25명
class Sensor72225(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=25, operator='Equal'):
            return SafeGreen72225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen72225(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=25, operator='Equal'):
            return Enable72225(self.ctx)
        if not self.count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable72225(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate72225(self.ctx)
        if not self.count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate72225(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72225(self.ctx)


class Delay72225(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate72225(self.ctx)


class DeActivate72225(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72225(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


# 30명
class Sensor72230(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=3) # red
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=30, operator='Equal'):
            return SafeGreen72230(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class SafeGreen72230(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9220, boxId=30, operator='Equal'):
            return Enable72230(self.ctx)
        if not self.count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Enable72230(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000943], stateValue=0):
            return Activate72230(self.ctx)
        if not self.count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Activate72230(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=True)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72230(self.ctx)


class Delay72230(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000959], stateValue=0):
            return DeActivate72230(self.ctx)


class DeActivate72230(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72230(self.ctx)
        if self.user_value(key='Barrier22', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8220], visible=False)
        self.set_interact_object(triggerIds=[10000943], state=0) # On
        self.set_interact_object(triggerIds=[10000959], state=0) # Off
        self.set_user_value(key='Barrier22', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
