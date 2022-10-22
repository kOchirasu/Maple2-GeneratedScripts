""" trigger/61000008_me/barrier_8120.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8120], visible=False)
        set_interact_object(triggerIds=[10000939], state=2) # On
        set_interact_object(triggerIds=[10000955], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier12', value=1):
            return Sensor7121()
        if user_value(key='Barrier12', value=2):
            return Sensor7122()
        if user_value(key='Barrier12', value=3):
            return Sensor7123()
        if user_value(key='Barrier12', value=4):
            return Sensor7124()
        if user_value(key='Barrier12', value=5):
            return Sensor7125()


#  1명 방어 불가 
class Sensor7121(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=1, operator='Equal'):
            return Activate7121()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Activate7121(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=1, operator='Equal'):
            return Sensor7121()
        if user_value(key='Barrier12', value=10):
            return Reset()


#  2명 
class Sensor7122(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8120], visible=False)
        set_interact_object(triggerIds=[10000939], state=0) # On
        set_interact_object(triggerIds=[10000955], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=2, operator='Equal'):
            return SafeGreen7122()
        if user_value(key='Barrier12', value=10):
            return Reset()


class SafeGreen7122(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=2, operator='Equal'):
            return Enable7122()
        if not count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Enable7122(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000939], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000939], arg2=0):
            return Activate7122()
        if not count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Activate7122(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=True)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000939], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7122()


class Delay7122(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000955], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=2, operator='Equal'):
            return Sensor7122()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if object_interacted(interactIds=[10000955], arg2=0):
            return DeActivate7122()


class DeActivate7122(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=False)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7122()
        if user_value(key='Barrier12', value=10):
            return Reset()


#  3명 
class Sensor7123(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8120], visible=False)
        set_interact_object(triggerIds=[10000939], state=0) # On
        set_interact_object(triggerIds=[10000955], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=3, operator='Equal'):
            return SafeGreen7123()
        if user_value(key='Barrier12', value=10):
            return Reset()


class SafeGreen7123(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=3, operator='Equal'):
            return Enable7123()
        if not count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Enable7123(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000939], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000939], arg2=0):
            return Activate7123()
        if not count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Activate7123(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=True)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000939], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7123()


class Delay7123(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000955], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=3, operator='Equal'):
            return Sensor7123()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if object_interacted(interactIds=[10000955], arg2=0):
            return DeActivate7123()


class DeActivate7123(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=False)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7123()
        if user_value(key='Barrier12', value=10):
            return Reset()


#  4명 
class Sensor7124(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8120], visible=False)
        set_interact_object(triggerIds=[10000939], state=0) # On
        set_interact_object(triggerIds=[10000955], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=4, operator='Equal'):
            return SafeGreen7124()
        if user_value(key='Barrier12', value=10):
            return Reset()


class SafeGreen7124(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=4, operator='Equal'):
            return Enable7124()
        if not count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Enable7124(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000939], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000939], arg2=0):
            return Activate7124()
        if not count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Activate7124(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=True)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000939], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7124()


class Delay7124(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000955], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=4, operator='Equal'):
            return Sensor7124()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if object_interacted(interactIds=[10000955], arg2=0):
            return DeActivate7124()


class DeActivate7124(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=False)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7124()
        if user_value(key='Barrier12', value=10):
            return Reset()


#  5명 
class Sensor7125(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=1) # yellow
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8120], visible=False)
        set_interact_object(triggerIds=[10000939], state=0) # On
        set_interact_object(triggerIds=[10000955], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=5, operator='Equal'):
            return SafeGreen7125()
        if user_value(key='Barrier12', value=10):
            return Reset()


class SafeGreen7125(state.State):
    def on_enter(self):
        set_user_value(triggerId=7120, key='Color12', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9120, boxId=5, operator='Equal'):
            return Enable7125()
        if not count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Enable7125(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9120], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000939], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000939], arg2=0):
            return Activate7125()
        if not count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Activate7125(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=True)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000939], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7125()


class Delay7125(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000955], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9120, boxId=5, operator='Equal'):
            return Sensor7125()
        if user_value(key='Barrier12', value=10):
            return Reset()
        if object_interacted(interactIds=[10000955], arg2=0):
            return DeActivate7125()


class DeActivate7125(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8120], visible=False)
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7125()
        if user_value(key='Barrier12', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8121,8122,8123,8124,8125,8126], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8120], visible=False)
        set_interact_object(triggerIds=[10000939], state=0) # On
        set_interact_object(triggerIds=[10000955], state=0) # Off
        set_user_value(key='Barrier12', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


