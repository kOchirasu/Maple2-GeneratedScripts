""" trigger/84000007_wd/barrier_8340.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8340], visible=False)
        set_interact_object(triggerIds=[10000949], state=2) # On
        set_interact_object(triggerIds=[10000965], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier34', value=1):
            return Sensor7341()
        if user_value(key='Barrier34', value=2):
            return Sensor7342()
        if user_value(key='Barrier34', value=3):
            return Sensor7343()
        if user_value(key='Barrier34', value=4):
            return Sensor7344()
        if user_value(key='Barrier34', value=5):
            return Sensor7345()


#  1명 방어 불가 
class Sensor7341(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=1, operator='Equal'):
            return Activate7341()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Activate7341(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=1, operator='Equal'):
            return Sensor7341()
        if user_value(key='Barrier34', value=10):
            return Reset()


#  2명 
class Sensor7342(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8340], visible=False)
        set_interact_object(triggerIds=[10000949], state=0) # On
        set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=2, operator='Equal'):
            return SafeGreen7342()
        if user_value(key='Barrier34', value=10):
            return Reset()


class SafeGreen7342(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=2, operator='Equal'):
            return Enable7342()
        if not count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Enable7342(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000949], arg2=0):
            return Activate7342()
        if not count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Activate7342(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=True)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7342()


class Delay7342(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=2, operator='Equal'):
            return Sensor7342()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if object_interacted(interactIds=[10000965], arg2=0):
            return DeActivate7342()


class DeActivate7342(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=False)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7342()
        if user_value(key='Barrier34', value=10):
            return Reset()


#  3명 
class Sensor7343(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8340], visible=False)
        set_interact_object(triggerIds=[10000949], state=0) # On
        set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=3, operator='Equal'):
            return SafeGreen7343()
        if user_value(key='Barrier34', value=10):
            return Reset()


class SafeGreen7343(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=3, operator='Equal'):
            return Enable7343()
        if not count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Enable7343(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000949], arg2=0):
            return Activate7343()
        if not count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Activate7343(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=True)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7343()


class Delay7343(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=3, operator='Equal'):
            return Sensor7343()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if object_interacted(interactIds=[10000965], arg2=0):
            return DeActivate7343()


class DeActivate7343(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=False)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7343()
        if user_value(key='Barrier34', value=10):
            return Reset()


#  4명 
class Sensor7344(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8340], visible=False)
        set_interact_object(triggerIds=[10000949], state=0) # On
        set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=4, operator='Equal'):
            return SafeGreen7344()
        if user_value(key='Barrier34', value=10):
            return Reset()


class SafeGreen7344(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=4, operator='Equal'):
            return Enable7344()
        if not count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Enable7344(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000949], arg2=0):
            return Activate7344()
        if not count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Activate7344(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=True)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7344()


class Delay7344(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=4, operator='Equal'):
            return Sensor7344()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if object_interacted(interactIds=[10000965], arg2=0):
            return DeActivate7344()


class DeActivate7344(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=False)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7344()
        if user_value(key='Barrier34', value=10):
            return Reset()


#  5명 
class Sensor7345(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=1) # yellow
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8340], visible=False)
        set_interact_object(triggerIds=[10000949], state=0) # On
        set_interact_object(triggerIds=[10000965], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=5, operator='Equal'):
            return SafeGreen7345()
        if user_value(key='Barrier34', value=10):
            return Reset()


class SafeGreen7345(state.State):
    def on_enter(self):
        set_user_value(triggerId=7340, key='Color34', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=5, operator='Equal'):
            return Enable7345()
        if not count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Enable7345(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000949], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000949], arg2=0):
            return Activate7345()
        if not count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Activate7345(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=True)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000949], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7345()


class Delay7345(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000965], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9340, boxId=5, operator='Equal'):
            return Sensor7345()
        if user_value(key='Barrier34', value=10):
            return Reset()
        if object_interacted(interactIds=[10000965], arg2=0):
            return DeActivate7345()


class DeActivate7345(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8340], visible=False)
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7345()
        if user_value(key='Barrier34', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8341,8342,8343,8344,8345,8346], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8340], visible=False)
        set_interact_object(triggerIds=[10000949], state=0) # On
        set_interact_object(triggerIds=[10000965], state=0) # Off
        set_user_value(key='Barrier34', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


