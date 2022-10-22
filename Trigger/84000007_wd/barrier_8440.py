""" trigger/84000007_wd/barrier_8440.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8440], visible=False)
        set_interact_object(triggerIds=[10000953], state=2) # On
        set_interact_object(triggerIds=[10000969], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier44', value=1):
            return Sensor7441()
        if user_value(key='Barrier44', value=2):
            return Sensor7442()
        if user_value(key='Barrier44', value=3):
            return Sensor7443()
        if user_value(key='Barrier44', value=4):
            return Sensor7444()
        if user_value(key='Barrier44', value=5):
            return Sensor7445()


#  1명 방어 불가 
class Sensor7441(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=1, operator='Equal'):
            return Activate7441()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Activate7441(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=1, operator='Equal'):
            return Sensor7441()
        if user_value(key='Barrier44', value=10):
            return Reset()


#  2명 
class Sensor7442(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8440], visible=False)
        set_interact_object(triggerIds=[10000953], state=0) # On
        set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=2, operator='Equal'):
            return SafeGreen7442()
        if user_value(key='Barrier44', value=10):
            return Reset()


class SafeGreen7442(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=2, operator='Equal'):
            return Enable7442()
        if not count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Enable7442(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000953], arg2=0):
            return Activate7442()
        if not count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Activate7442(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=True)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7442()


class Delay7442(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=2, operator='Equal'):
            return Sensor7442()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if object_interacted(interactIds=[10000969], arg2=0):
            return DeActivate7442()


class DeActivate7442(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=False)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7442()
        if user_value(key='Barrier44', value=10):
            return Reset()


#  3명 
class Sensor7443(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8440], visible=False)
        set_interact_object(triggerIds=[10000953], state=0) # On
        set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=3, operator='Equal'):
            return SafeGreen7443()
        if user_value(key='Barrier44', value=10):
            return Reset()


class SafeGreen7443(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=3, operator='Equal'):
            return Enable7443()
        if not count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Enable7443(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000953], arg2=0):
            return Activate7443()
        if not count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Activate7443(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=True)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7443()


class Delay7443(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=3, operator='Equal'):
            return Sensor7443()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if object_interacted(interactIds=[10000969], arg2=0):
            return DeActivate7443()


class DeActivate7443(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=False)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7443()
        if user_value(key='Barrier44', value=10):
            return Reset()


#  4명 
class Sensor7444(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8440], visible=False)
        set_interact_object(triggerIds=[10000953], state=0) # On
        set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=4, operator='Equal'):
            return SafeGreen7444()
        if user_value(key='Barrier44', value=10):
            return Reset()


class SafeGreen7444(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=4, operator='Equal'):
            return Enable7444()
        if not count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Enable7444(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000953], arg2=0):
            return Activate7444()
        if not count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Activate7444(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=True)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7444()


class Delay7444(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=4, operator='Equal'):
            return Sensor7444()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if object_interacted(interactIds=[10000969], arg2=0):
            return DeActivate7444()


class DeActivate7444(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=False)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7444()
        if user_value(key='Barrier44', value=10):
            return Reset()


#  5명 
class Sensor7445(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=1) # yellow
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8440], visible=False)
        set_interact_object(triggerIds=[10000953], state=0) # On
        set_interact_object(triggerIds=[10000969], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=5, operator='Equal'):
            return SafeGreen7445()
        if user_value(key='Barrier44', value=10):
            return Reset()


class SafeGreen7445(state.State):
    def on_enter(self):
        set_user_value(triggerId=7440, key='Color44', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9440, boxId=5, operator='Equal'):
            return Enable7445()
        if not count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Enable7445(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9440], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000953], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000953], arg2=0):
            return Activate7445()
        if not count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Activate7445(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=True)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000953], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7445()


class Delay7445(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000969], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9440, boxId=5, operator='Equal'):
            return Sensor7445()
        if user_value(key='Barrier44', value=10):
            return Reset()
        if object_interacted(interactIds=[10000969], arg2=0):
            return DeActivate7445()


class DeActivate7445(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8440], visible=False)
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7445()
        if user_value(key='Barrier44', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8441,8442,8443,8444], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8440], visible=False)
        set_interact_object(triggerIds=[10000953], state=0) # On
        set_interact_object(triggerIds=[10000969], state=0) # Off
        set_user_value(key='Barrier44', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


