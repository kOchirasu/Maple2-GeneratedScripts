""" trigger/61000022_me/barrier_8220.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=2) # On
        set_interact_object(triggerIds=[10000959], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier22', value=1):
            return Sensor7221()
        if user_value(key='Barrier22', value=2):
            return Sensor7222()
        if user_value(key='Barrier22', value=3):
            return Sensor7223()
        if user_value(key='Barrier22', value=4):
            return Sensor7224()
        if user_value(key='Barrier22', value=5):
            return Sensor7225()
        if user_value(key='Barrier22', value=7):
            return Sensor7227()
        if user_value(key='Barrier22', value=8):
            return Sensor7228()
        if user_value(key='Barrier22', value=9):
            return Sensor7229()
        if user_value(key='Barrier22', value=6):
            return Sensor7226()
        if user_value(key='Barrier22', value=15):
            return Sensor72215()
        if user_value(key='Barrier22', value=20):
            return Sensor72220()
        if user_value(key='Barrier22', value=25):
            return Sensor72225()
        if user_value(key='Barrier22', value=30):
            return Sensor72230()


#  1명 방어 불가 
class Sensor7221(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=1, operator='Equal'):
            return Activate7221()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7221(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=1, operator='Equal'):
            return Sensor7221()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  2명 
class Sensor7222(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=2, operator='Equal'):
            return SafeGreen7222()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7222(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=2, operator='Equal'):
            return Enable7222()
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7222(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7222()
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7222(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7222()


class Delay7222(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7222()


class DeActivate7222(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  3명 
class Sensor7223(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=3, operator='Equal'):
            return SafeGreen7223()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7223(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=3, operator='Equal'):
            return Enable7223()
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7223(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7223()
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7223(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7223()


class Delay7223(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7223()


class DeActivate7223(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  4명 
class Sensor7224(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=4, operator='Equal'):
            return SafeGreen7224()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7224(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=4, operator='Equal'):
            return Enable7224()
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7224(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7224()
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7224(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7224()


class Delay7224(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7224()


class DeActivate7224(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  5명 
class Sensor7225(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=1) # yellow
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=5, operator='Equal'):
            return SafeGreen7225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7225(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=5, operator='Equal'):
            return Enable7225()
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7225(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7225()
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7225(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7225()


class Delay7225(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7225()


class DeActivate7225(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  7명 
class Sensor7227(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=7, operator='Equal'):
            return SafeGreen7227()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7227(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=7, operator='Equal'):
            return Enable7227()
        if not count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7227(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7227()
        if not count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7227(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7227()


class Delay7227(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=7, operator='Equal'):
            return Sensor7227()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7227()


class DeActivate7227(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7227()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  8명 
class Sensor7228(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=8, operator='Equal'):
            return SafeGreen7228()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7228(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=8, operator='Equal'):
            return Enable7228()
        if not count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7228(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7228()
        if not count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7228(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7228()


class Delay7228(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=8, operator='Equal'):
            return Sensor7228()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7228()


class DeActivate7228(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7228()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  9명 
class Sensor7229(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=9, operator='Equal'):
            return SafeGreen7229()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7229(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=9, operator='Equal'):
            return Enable7229()
        if not count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7229(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7229()
        if not count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7229(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7229()


class Delay7229(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=9, operator='Equal'):
            return Sensor7229()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7229()


class DeActivate7229(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7229()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  10명 
class Sensor7226(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=10, operator='Equal'):
            return SafeGreen7226()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen7226(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=10, operator='Equal'):
            return Enable7226()
        if not count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7226(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate7226()
        if not count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7226(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7226()


class Delay7226(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=10, operator='Equal'):
            return Sensor7226()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate7226()


class DeActivate7226(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7226()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  15명 
class Sensor72215(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=15, operator='Equal'):
            return SafeGreen72215()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen72215(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=15, operator='Equal'):
            return Enable72215()
        if not count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable72215(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate72215()
        if not count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate72215(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72215()


class Delay72215(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=15, operator='Equal'):
            return Sensor72215()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate72215()


class DeActivate72215(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72215()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  20명 
class Sensor72220(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=20, operator='Equal'):
            return SafeGreen72220()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen72220(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=20, operator='Equal'):
            return Enable72220()
        if not count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable72220(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate72220()
        if not count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate72220(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72220()


class Delay72220(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=20, operator='Equal'):
            return Sensor72220()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate72220()


class DeActivate72220(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72220()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  25명 
class Sensor72225(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=25, operator='Equal'):
            return SafeGreen72225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen72225(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=25, operator='Equal'):
            return Enable72225()
        if not count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable72225(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate72225()
        if not count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate72225(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72225()


class Delay72225(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=25, operator='Equal'):
            return Sensor72225()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate72225()


class DeActivate72225(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72225()
        if user_value(key='Barrier22', value=10):
            return Reset()


#  30명 
class Sensor72230(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=3) # red
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=30, operator='Equal'):
            return SafeGreen72230()
        if user_value(key='Barrier22', value=10):
            return Reset()


class SafeGreen72230(state.State):
    def on_enter(self):
        set_user_value(triggerId=7220, key='Color22', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9220, boxId=30, operator='Equal'):
            return Enable72230()
        if not count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable72230(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000943], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000943], arg2=0):
            return Activate72230()
        if not count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate72230(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000943], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72230()


class Delay72230(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000959], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=30, operator='Equal'):
            return Sensor72230()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10000959], arg2=0):
            return DeActivate72230()


class DeActivate72230(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=False)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72230()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10000943], state=0) # On
        set_interact_object(triggerIds=[10000959], state=0) # Off
        set_user_value(key='Barrier22', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


