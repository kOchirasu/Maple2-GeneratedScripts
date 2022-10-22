""" trigger/61000022_me/barrier_8430.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8430], visible=False)
        set_interact_object(triggerIds=[10000952], state=2) # On
        set_interact_object(triggerIds=[10000968], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier43', value=1):
            return Sensor7431()
        if user_value(key='Barrier43', value=2):
            return Sensor7432()
        if user_value(key='Barrier43', value=3):
            return Sensor7433()
        if user_value(key='Barrier43', value=4):
            return Sensor7434()
        if user_value(key='Barrier43', value=5):
            return Sensor7435()


#  1명 방어 불가 
class Sensor7431(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=1, operator='Equal'):
            return Activate7431()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Activate7431(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=1, operator='Equal'):
            return Sensor7431()
        if user_value(key='Barrier43', value=10):
            return Reset()


#  2명 
class Sensor7432(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8430], visible=False)
        set_interact_object(triggerIds=[10000952], state=0) # On
        set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=2, operator='Equal'):
            return SafeGreen7432()
        if user_value(key='Barrier43', value=10):
            return Reset()


class SafeGreen7432(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=2, operator='Equal'):
            return Enable7432()
        if not count_users(boxId=9430, boxId=2, operator='Equal'):
            return Sensor7432()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Enable7432(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000952], arg2=0):
            return Activate7432()
        if not count_users(boxId=9430, boxId=2, operator='Equal'):
            return Sensor7432()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Activate7432(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=True)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=2, operator='Equal'):
            return Sensor7432()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7432()


class Delay7432(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=2, operator='Equal'):
            return Sensor7432()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if object_interacted(interactIds=[10000968], arg2=0):
            return DeActivate7432()


class DeActivate7432(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=False)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7432()
        if user_value(key='Barrier43', value=10):
            return Reset()


#  3명 
class Sensor7433(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8430], visible=False)
        set_interact_object(triggerIds=[10000952], state=0) # On
        set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=3, operator='Equal'):
            return SafeGreen7433()
        if user_value(key='Barrier43', value=10):
            return Reset()


class SafeGreen7433(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=3, operator='Equal'):
            return Enable7433()
        if not count_users(boxId=9430, boxId=3, operator='Equal'):
            return Sensor7433()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Enable7433(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000952], arg2=0):
            return Activate7433()
        if not count_users(boxId=9430, boxId=3, operator='Equal'):
            return Sensor7433()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Activate7433(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=True)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=3, operator='Equal'):
            return Sensor7433()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7433()


class Delay7433(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=3, operator='Equal'):
            return Sensor7433()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if object_interacted(interactIds=[10000968], arg2=0):
            return DeActivate7433()


class DeActivate7433(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=False)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7433()
        if user_value(key='Barrier43', value=10):
            return Reset()


#  4명 
class Sensor7434(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8430], visible=False)
        set_interact_object(triggerIds=[10000952], state=0) # On
        set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=4, operator='Equal'):
            return SafeGreen7434()
        if user_value(key='Barrier43', value=10):
            return Reset()


class SafeGreen7434(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=4, operator='Equal'):
            return Enable7434()
        if not count_users(boxId=9430, boxId=4, operator='Equal'):
            return Sensor7434()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Enable7434(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000952], arg2=0):
            return Activate7434()
        if not count_users(boxId=9430, boxId=4, operator='Equal'):
            return Sensor7434()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Activate7434(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=True)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=4, operator='Equal'):
            return Sensor7434()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7434()


class Delay7434(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=4, operator='Equal'):
            return Sensor7434()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if object_interacted(interactIds=[10000968], arg2=0):
            return DeActivate7434()


class DeActivate7434(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=False)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7434()
        if user_value(key='Barrier43', value=10):
            return Reset()


#  5명 
class Sensor7435(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8430], visible=False)
        set_interact_object(triggerIds=[10000952], state=0) # On
        set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=5, operator='Equal'):
            return SafeGreen7435()
        if user_value(key='Barrier43', value=10):
            return Reset()


class SafeGreen7435(state.State):
    def on_enter(self):
        set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9430, boxId=5, operator='Equal'):
            return Enable7435()
        if not count_users(boxId=9430, boxId=5, operator='Equal'):
            return Sensor7435()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Enable7435(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000952], arg2=0):
            return Activate7435()
        if not count_users(boxId=9430, boxId=5, operator='Equal'):
            return Sensor7435()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Activate7435(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=True)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=5, operator='Equal'):
            return Sensor7435()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7435()


class Delay7435(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9430, boxId=5, operator='Equal'):
            return Sensor7435()
        if user_value(key='Barrier43', value=10):
            return Reset()
        if object_interacted(interactIds=[10000968], arg2=0):
            return DeActivate7435()


class DeActivate7435(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8430], visible=False)
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7435()
        if user_value(key='Barrier43', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8430], visible=False)
        set_interact_object(triggerIds=[10000952], state=0) # On
        set_interact_object(triggerIds=[10000968], state=0) # Off
        set_user_value(key='Barrier43', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


