""" trigger/61000008_me/barrier_8110.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8110], visible=False)
        set_interact_object(triggerIds=[10000938], state=2) # On
        set_interact_object(triggerIds=[10000954], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier11', value=1):
            return Sensor7111()
        if user_value(key='Barrier11', value=2):
            return Sensor7112()
        if user_value(key='Barrier11', value=3):
            return Sensor7113()
        if user_value(key='Barrier11', value=4):
            return Sensor7114()
        if user_value(key='Barrier11', value=5):
            return Sensor7115()


#  1명 방어 불가 
class Sensor7111(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=1, operator='Equal'):
            return Activate7111()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Activate7111(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=1, operator='Equal'):
            return Sensor7111()
        if user_value(key='Barrier11', value=10):
            return Reset()


#  2명 
class Sensor7112(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8110], visible=False)
        set_interact_object(triggerIds=[10000938], state=0) # On
        set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=2, operator='Equal'):
            return SafeGreen7112()
        if user_value(key='Barrier11', value=10):
            return Reset()


class SafeGreen7112(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=2, operator='Equal'):
            return Enable7112()
        if not count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Enable7112(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000938], arg2=0):
            return Activate7112()
        if not count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Activate7112(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=True)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7112()


class Delay7112(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if object_interacted(interactIds=[10000954], arg2=0):
            return DeActivate7112()


class DeActivate7112(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=False)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7112()
        if user_value(key='Barrier11', value=10):
            return Reset()


#  3명 
class Sensor7113(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8110], visible=False)
        set_interact_object(triggerIds=[10000938], state=0) # On
        set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=3, operator='Equal'):
            return SafeGreen7113()
        if user_value(key='Barrier11', value=10):
            return Reset()


class SafeGreen7113(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=3, operator='Equal'):
            return Enable7113()
        if not count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Enable7113(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000938], arg2=0):
            return Activate7113()
        if not count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Activate7113(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=True)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7113()


class Delay7113(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if object_interacted(interactIds=[10000954], arg2=0):
            return DeActivate7113()


class DeActivate7113(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=False)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7113()
        if user_value(key='Barrier11', value=10):
            return Reset()


#  4명 
class Sensor7114(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8110], visible=False)
        set_interact_object(triggerIds=[10000938], state=0) # On
        set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=4, operator='Equal'):
            return SafeGreen7114()
        if user_value(key='Barrier11', value=10):
            return Reset()


class SafeGreen7114(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=4, operator='Equal'):
            return Enable7114()
        if not count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Enable7114(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000938], arg2=0):
            return Activate7114()
        if not count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Activate7114(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=True)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7114()


class Delay7114(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if object_interacted(interactIds=[10000954], arg2=0):
            return DeActivate7114()


class DeActivate7114(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=False)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7114()
        if user_value(key='Barrier11', value=10):
            return Reset()


#  5명 
class Sensor7115(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8110], visible=False)
        set_interact_object(triggerIds=[10000938], state=0) # On
        set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=5, operator='Equal'):
            return SafeGreen7115()
        if user_value(key='Barrier11', value=10):
            return Reset()


class SafeGreen7115(state.State):
    def on_enter(self):
        set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9110, boxId=5, operator='Equal'):
            return Enable7115()
        if not count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Enable7115(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000938], arg2=0):
            return Activate7115()
        if not count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Activate7115(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=True)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7115()


class Delay7115(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115()
        if user_value(key='Barrier11', value=10):
            return Reset()
        if object_interacted(interactIds=[10000954], arg2=0):
            return DeActivate7115()


class DeActivate7115(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8110], visible=False)
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7115()
        if user_value(key='Barrier11', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8110], visible=False)
        set_interact_object(triggerIds=[10000938], state=0) # On
        set_interact_object(triggerIds=[10000954], state=0) # Off
        set_user_value(key='Barrier11', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


