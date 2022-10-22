""" trigger/84000007_wd/barrier_8330.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=2) # On
        set_interact_object(triggerIds=[10000964], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier33', value=1):
            return Sensor7331()
        if user_value(key='Barrier33', value=2):
            return Sensor7332()
        if user_value(key='Barrier33', value=3):
            return Sensor7333()
        if user_value(key='Barrier33', value=4):
            return Sensor7334()
        if user_value(key='Barrier33', value=5):
            return Sensor7335()
        if user_value(key='Barrier33', value=7):
            return Sensor7337()
        if user_value(key='Barrier33', value=8):
            return Sensor7338()
        if user_value(key='Barrier33', value=9):
            return Sensor7339()
        if user_value(key='Barrier33', value=6):
            return Sensor7336()
        if user_value(key='Barrier33', value=15):
            return Sensor73315()
        if user_value(key='Barrier33', value=20):
            return Sensor73320()
        if user_value(key='Barrier33', value=25):
            return Sensor73325()
        if user_value(key='Barrier33', value=30):
            return Sensor73330()


#  1명 방어 불가 
class Sensor7331(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=1, operator='Equal'):
            return Activate7331()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7331(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=1, operator='Equal'):
            return Sensor7331()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  2명 
class Sensor7332(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=2, operator='Equal'):
            return SafeGreen7332()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7332(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=2, operator='Equal'):
            return Enable7332()
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7332(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7332()
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7332(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7332()


class Delay7332(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7332()


class DeActivate7332(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  3명 
class Sensor7333(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=3, operator='Equal'):
            return SafeGreen7333()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7333(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=3, operator='Equal'):
            return Enable7333()
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7333(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7333()
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7333(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7333()


class Delay7333(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7333()


class DeActivate7333(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  4명 
class Sensor7334(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=4, operator='Equal'):
            return SafeGreen7334()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7334(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=4, operator='Equal'):
            return Enable7334()
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7334(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7334()
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7334(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7334()


class Delay7334(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7334()


class DeActivate7334(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  5명 
class Sensor7335(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=1) # yellow
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=5, operator='Equal'):
            return SafeGreen7335()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7335(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=5, operator='Equal'):
            return Enable7335()
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7335(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7335()
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7335(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7335()


class Delay7335(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7335()


class DeActivate7335(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  7명 
class Sensor7337(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=7, operator='Equal'):
            return SafeGreen7337()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7337(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=7, operator='Equal'):
            return Enable7337()
        if not count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7337(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7337()
        if not count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7337(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7337()


class Delay7337(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=7, operator='Equal'):
            return Sensor7337()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7337()


class DeActivate7337(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7337()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  8명 
class Sensor7338(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=8, operator='Equal'):
            return SafeGreen7338()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7338(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=8, operator='Equal'):
            return Enable7338()
        if not count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7338(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7338()
        if not count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7338(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7338()


class Delay7338(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=8, operator='Equal'):
            return Sensor7338()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7338()


class DeActivate7338(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7338()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  9명 
class Sensor7339(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=9, operator='Equal'):
            return SafeGreen7339()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7339(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=9, operator='Equal'):
            return Enable7339()
        if not count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7339(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7339()
        if not count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7339(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7339()


class Delay7339(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=9, operator='Equal'):
            return Sensor7339()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7339()


class DeActivate7339(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7339()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  10명 
class Sensor7336(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=10, operator='Equal'):
            return SafeGreen7336()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen7336(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=10, operator='Equal'):
            return Enable7336()
        if not count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7336(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate7336()
        if not count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7336(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7336()


class Delay7336(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=10, operator='Equal'):
            return Sensor7336()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate7336()


class DeActivate7336(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7336()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  15명 
class Sensor73315(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=15, operator='Equal'):
            return SafeGreen73315()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen73315(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=15, operator='Equal'):
            return Enable73315()
        if not count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable73315(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate73315()
        if not count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate73315(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73315()


class Delay73315(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=15, operator='Equal'):
            return Sensor73315()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate73315()


class DeActivate73315(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73315()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  20명 
class Sensor73320(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=20, operator='Equal'):
            return SafeGreen73320()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen73320(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=20, operator='Equal'):
            return Enable73320()
        if not count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable73320(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate73320()
        if not count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate73320(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73320()


class Delay73320(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=20, operator='Equal'):
            return Sensor73320()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate73320()


class DeActivate73320(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73320()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  25명 
class Sensor73325(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=25, operator='Equal'):
            return SafeGreen73325()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen73325(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=25, operator='Equal'):
            return Enable73325()
        if not count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable73325(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate73325()
        if not count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate73325(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73325()


class Delay73325(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=25, operator='Equal'):
            return Sensor73325()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate73325()


class DeActivate73325(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73325()
        if user_value(key='Barrier33', value=10):
            return Reset()


#  30명 
class Sensor73330(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=3) # red
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=30, operator='Equal'):
            return SafeGreen73330()
        if user_value(key='Barrier33', value=10):
            return Reset()


class SafeGreen73330(state.State):
    def on_enter(self):
        set_user_value(triggerId=7330, key='Color33', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9330, boxId=30, operator='Equal'):
            return Enable73330()
        if not count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable73330(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000948], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000948], arg2=0):
            return Activate73330()
        if not count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate73330(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000948], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73330()


class Delay73330(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000964], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=30, operator='Equal'):
            return Sensor73330()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10000964], arg2=0):
            return DeActivate73330()


class DeActivate73330(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=False)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73330()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10000948], state=0) # On
        set_interact_object(triggerIds=[10000964], state=0) # Off
        set_user_value(key='Barrier33', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


