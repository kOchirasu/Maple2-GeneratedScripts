""" trigger/84000007_wd/barrier_8410.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8410], visible=False)
        set_interact_object(triggerIds=[10000950], state=2) # On
        set_interact_object(triggerIds=[10000966], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier41', value=1):
            return Sensor7411()
        if user_value(key='Barrier41', value=2):
            return Sensor7412()
        if user_value(key='Barrier41', value=3):
            return Sensor7413()
        if user_value(key='Barrier41', value=4):
            return Sensor7414()
        if user_value(key='Barrier41', value=5):
            return Sensor7415()


#  1명 방어 불가 
class Sensor7411(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=1, operator='Equal'):
            return Activate7411()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Activate7411(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=1, operator='Equal'):
            return Sensor7411()
        if user_value(key='Barrier41', value=10):
            return Reset()


#  2명 
class Sensor7412(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8410], visible=False)
        set_interact_object(triggerIds=[10000950], state=0) # On
        set_interact_object(triggerIds=[10000966], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=2, operator='Equal'):
            return SafeGreen7412()
        if user_value(key='Barrier41', value=10):
            return Reset()


class SafeGreen7412(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=2, operator='Equal'):
            return Enable7412()
        if not count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Enable7412(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000950], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000950], arg2=0):
            return Activate7412()
        if not count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Activate7412(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=True)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000950], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7412()


class Delay7412(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000966], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=2, operator='Equal'):
            return Sensor7412()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if object_interacted(interactIds=[10000966], arg2=0):
            return DeActivate7412()


class DeActivate7412(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=False)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7412()
        if user_value(key='Barrier41', value=10):
            return Reset()


#  3명 
class Sensor7413(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8410], visible=False)
        set_interact_object(triggerIds=[10000950], state=0) # On
        set_interact_object(triggerIds=[10000966], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=3, operator='Equal'):
            return SafeGreen7413()
        if user_value(key='Barrier41', value=10):
            return Reset()


class SafeGreen7413(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=3, operator='Equal'):
            return Enable7413()
        if not count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Enable7413(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000950], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000950], arg2=0):
            return Activate7413()
        if not count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Activate7413(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=True)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000950], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7413()


class Delay7413(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000966], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=3, operator='Equal'):
            return Sensor7413()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if object_interacted(interactIds=[10000966], arg2=0):
            return DeActivate7413()


class DeActivate7413(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=False)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7413()
        if user_value(key='Barrier41', value=10):
            return Reset()


#  4명 
class Sensor7414(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8410], visible=False)
        set_interact_object(triggerIds=[10000950], state=0) # On
        set_interact_object(triggerIds=[10000966], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=4, operator='Equal'):
            return SafeGreen7414()
        if user_value(key='Barrier41', value=10):
            return Reset()


class SafeGreen7414(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=4, operator='Equal'):
            return Enable7414()
        if not count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Enable7414(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000950], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000950], arg2=0):
            return Activate7414()
        if not count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Activate7414(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=True)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000950], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7414()


class Delay7414(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000966], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=4, operator='Equal'):
            return Sensor7414()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if object_interacted(interactIds=[10000966], arg2=0):
            return DeActivate7414()


class DeActivate7414(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=False)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7414()
        if user_value(key='Barrier41', value=10):
            return Reset()


#  5명 
class Sensor7415(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=1) # yellow
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8410], visible=False)
        set_interact_object(triggerIds=[10000950], state=0) # On
        set_interact_object(triggerIds=[10000966], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=5, operator='Equal'):
            return SafeGreen7415()
        if user_value(key='Barrier41', value=10):
            return Reset()


class SafeGreen7415(state.State):
    def on_enter(self):
        set_user_value(triggerId=7410, key='Color41', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9410, boxId=5, operator='Equal'):
            return Enable7415()
        if not count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Enable7415(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9410], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000950], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000950], arg2=0):
            return Activate7415()
        if not count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Activate7415(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=True)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000950], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7415()


class Delay7415(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000966], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9410, boxId=5, operator='Equal'):
            return Sensor7415()
        if user_value(key='Barrier41', value=10):
            return Reset()
        if object_interacted(interactIds=[10000966], arg2=0):
            return DeActivate7415()


class DeActivate7415(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8410], visible=False)
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7415()
        if user_value(key='Barrier41', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8411,8412,8413,8414], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8410], visible=False)
        set_interact_object(triggerIds=[10000950], state=0) # On
        set_interact_object(triggerIds=[10000966], state=0) # Off
        set_user_value(key='Barrier41', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


