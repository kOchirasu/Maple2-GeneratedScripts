""" trigger/66200001_gd/barrier_8220.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10001190], state=2) # On
        set_interact_object(triggerIds=[10001206], state=2) # Off

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
        set_interact_object(triggerIds=[10001190], state=0) # On
        set_interact_object(triggerIds=[10001206], state=0) # Off

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
            return CheckSameUserTag7222()
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()


class CheckSameUserTag7222(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7222()
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if not check_same_user_tag(boxId=9220):
            return SafeGreen7222()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7222(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001190], arg2=0):
            return Activate7222()
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7222(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7222()


class Delay7222(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=2, operator='Equal'):
            return Sensor7222()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10001206], arg2=0):
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
        set_interact_object(triggerIds=[10001190], state=0) # On
        set_interact_object(triggerIds=[10001206], state=0) # Off

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
            return CheckSameUserTag7223()
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()


class CheckSameUserTag7223(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7223()
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if not check_same_user_tag(boxId=9220):
            return SafeGreen7223()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7223(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001190], arg2=0):
            return Activate7223()
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7223(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7223()


class Delay7223(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=3, operator='Equal'):
            return Sensor7223()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10001206], arg2=0):
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
        set_interact_object(triggerIds=[10001190], state=0) # On
        set_interact_object(triggerIds=[10001206], state=0) # Off

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
            return CheckSameUserTag7224()
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()


class CheckSameUserTag7224(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7224()
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if not check_same_user_tag(boxId=9220):
            return SafeGreen7224()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7224(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001190], arg2=0):
            return Activate7224()
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7224(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7224()


class Delay7224(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=4, operator='Equal'):
            return Sensor7224()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10001206], arg2=0):
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
        set_interact_object(triggerIds=[10001190], state=0) # On
        set_interact_object(triggerIds=[10001206], state=0) # Off

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
            return CheckSameUserTag7225()
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class CheckSameUserTag7225(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7225()
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if not check_same_user_tag(boxId=9220):
            return SafeGreen7225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Enable7225(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9220], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001190], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001190], arg2=0):
            return Activate7225()
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()


class Activate7225(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8220], visible=True)
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001190], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7225()


class Delay7225(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001206], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9220, boxId=5, operator='Equal'):
            return Sensor7225()
        if user_value(key='Barrier22', value=10):
            return Reset()
        if object_interacted(interactIds=[10001206], arg2=0):
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


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8221,8222,8223,8224,8225,8226,8227,8228], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8220], visible=False)
        set_interact_object(triggerIds=[10001190], state=0) # On
        set_interact_object(triggerIds=[10001206], state=0) # Off
        set_user_value(key='Barrier22', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


