""" trigger/61000022_me/barrier_8240.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8240], visible=False)
        set_interact_object(triggerIds=[10000945], state=2) # On
        set_interact_object(triggerIds=[10000961], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier24', value=1):
            return Sensor7241()
        if user_value(key='Barrier24', value=2):
            return Sensor7242()
        if user_value(key='Barrier24', value=3):
            return Sensor7243()
        if user_value(key='Barrier24', value=4):
            return Sensor7244()
        if user_value(key='Barrier24', value=5):
            return Sensor7245()


#  1명 방어 불가 
class Sensor7241(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=1, operator='Equal'):
            return Activate7241()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Activate7241(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=1, operator='Equal'):
            return Sensor7241()
        if user_value(key='Barrier24', value=10):
            return Reset()


#  2명 
class Sensor7242(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=1) # yellow
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8240], visible=False)
        set_interact_object(triggerIds=[10000945], state=0) # On
        set_interact_object(triggerIds=[10000961], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=2, operator='Equal'):
            return SafeGreen7242()
        if user_value(key='Barrier24', value=10):
            return Reset()


class SafeGreen7242(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=2, operator='Equal'):
            return Enable7242()
        if not count_users(boxId=9240, boxId=2, operator='Equal'):
            return Sensor7242()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Enable7242(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9240], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000945], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000945], arg2=0):
            return Activate7242()
        if not count_users(boxId=9240, boxId=2, operator='Equal'):
            return Sensor7242()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Activate7242(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=True)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000945], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=2, operator='Equal'):
            return Sensor7242()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7242()


class Delay7242(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000961], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=2, operator='Equal'):
            return Sensor7242()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if object_interacted(interactIds=[10000961], arg2=0):
            return DeActivate7242()


class DeActivate7242(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=False)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7242()
        if user_value(key='Barrier24', value=10):
            return Reset()


#  3명 
class Sensor7243(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=1) # yellow
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8240], visible=False)
        set_interact_object(triggerIds=[10000945], state=0) # On
        set_interact_object(triggerIds=[10000961], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=3, operator='Equal'):
            return SafeGreen7243()
        if user_value(key='Barrier24', value=10):
            return Reset()


class SafeGreen7243(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=3, operator='Equal'):
            return Enable7243()
        if not count_users(boxId=9240, boxId=3, operator='Equal'):
            return Sensor7243()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Enable7243(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9240], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000945], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000945], arg2=0):
            return Activate7243()
        if not count_users(boxId=9240, boxId=3, operator='Equal'):
            return Sensor7243()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Activate7243(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=True)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000945], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=3, operator='Equal'):
            return Sensor7243()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7243()


class Delay7243(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000961], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=3, operator='Equal'):
            return Sensor7243()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if object_interacted(interactIds=[10000961], arg2=0):
            return DeActivate7243()


class DeActivate7243(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=False)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7243()
        if user_value(key='Barrier24', value=10):
            return Reset()


#  4명 
class Sensor7244(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=1) # yellow
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8240], visible=False)
        set_interact_object(triggerIds=[10000945], state=0) # On
        set_interact_object(triggerIds=[10000961], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=4, operator='Equal'):
            return SafeGreen7244()
        if user_value(key='Barrier24', value=10):
            return Reset()


class SafeGreen7244(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=4, operator='Equal'):
            return Enable7244()
        if not count_users(boxId=9240, boxId=4, operator='Equal'):
            return Sensor7244()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Enable7244(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9240], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000945], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000945], arg2=0):
            return Activate7244()
        if not count_users(boxId=9240, boxId=4, operator='Equal'):
            return Sensor7244()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Activate7244(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=True)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000945], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=4, operator='Equal'):
            return Sensor7244()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7244()


class Delay7244(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000961], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=4, operator='Equal'):
            return Sensor7244()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if object_interacted(interactIds=[10000961], arg2=0):
            return DeActivate7244()


class DeActivate7244(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=False)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7244()
        if user_value(key='Barrier24', value=10):
            return Reset()


#  5명 
class Sensor7245(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=1) # yellow
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8240], visible=False)
        set_interact_object(triggerIds=[10000945], state=0) # On
        set_interact_object(triggerIds=[10000961], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=5, operator='Equal'):
            return SafeGreen7245()
        if user_value(key='Barrier24', value=10):
            return Reset()


class SafeGreen7245(state.State):
    def on_enter(self):
        set_user_value(triggerId=7240, key='Color24', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9240, boxId=5, operator='Equal'):
            return Enable7245()
        if not count_users(boxId=9240, boxId=5, operator='Equal'):
            return Sensor7245()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Enable7245(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9240], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000945], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000945], arg2=0):
            return Activate7245()
        if not count_users(boxId=9240, boxId=5, operator='Equal'):
            return Sensor7245()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Activate7245(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=True)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000945], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=5, operator='Equal'):
            return Sensor7245()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7245()


class Delay7245(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000961], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9240, boxId=5, operator='Equal'):
            return Sensor7245()
        if user_value(key='Barrier24', value=10):
            return Reset()
        if object_interacted(interactIds=[10000961], arg2=0):
            return DeActivate7245()


class DeActivate7245(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8240], visible=False)
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7245()
        if user_value(key='Barrier24', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8241,8242,8243,8244,8245,8246], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8240], visible=False)
        set_interact_object(triggerIds=[10000945], state=0) # On
        set_interact_object(triggerIds=[10000961], state=0) # Off
        set_user_value(key='Barrier24', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


