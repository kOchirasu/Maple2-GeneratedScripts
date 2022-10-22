""" trigger/66200001_gd/barrier_8330.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10001195], state=2) # On
        set_interact_object(triggerIds=[10001211], state=2) # Off

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
        set_interact_object(triggerIds=[10001195], state=0) # On
        set_interact_object(triggerIds=[10001211], state=0) # Off

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
            return CheckSameUserTag7332()
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()


class CheckSameUserTag7332(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7332()
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if not check_same_user_tag(boxId=9330):
            return SafeGreen7332()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7332(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001195], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001195], arg2=0):
            return Activate7332()
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7332(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001195], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7332()


class Delay7332(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001211], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=2, operator='Equal'):
            return Sensor7332()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10001211], arg2=0):
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
        set_interact_object(triggerIds=[10001195], state=0) # On
        set_interact_object(triggerIds=[10001211], state=0) # Off

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
            return CheckSameUserTag7333()
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()


class CheckSameUserTag7333(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7333()
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if not check_same_user_tag(boxId=9330):
            return SafeGreen7333()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7333(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001195], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001195], arg2=0):
            return Activate7333()
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7333(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001195], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7333()


class Delay7333(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001211], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=3, operator='Equal'):
            return Sensor7333()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10001211], arg2=0):
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
        set_interact_object(triggerIds=[10001195], state=0) # On
        set_interact_object(triggerIds=[10001211], state=0) # Off

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
            return CheckSameUserTag7334()
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()


class CheckSameUserTag7334(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7334()
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if not check_same_user_tag(boxId=9330):
            return SafeGreen7334()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7334(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001195], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001195], arg2=0):
            return Activate7334()
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7334(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001195], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7334()


class Delay7334(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001211], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=4, operator='Equal'):
            return Sensor7334()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10001211], arg2=0):
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
        set_interact_object(triggerIds=[10001195], state=0) # On
        set_interact_object(triggerIds=[10001211], state=0) # Off

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
            return CheckSameUserTag7335()
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()


class CheckSameUserTag7335(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7335()
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if not check_same_user_tag(boxId=9330):
            return SafeGreen7335()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Enable7335(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001195], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001195], arg2=0):
            return Activate7335()
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()


class Activate7335(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8330], visible=True)
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001195], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7335()


class Delay7335(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001211], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9330, boxId=5, operator='Equal'):
            return Sensor7335()
        if user_value(key='Barrier33', value=10):
            return Reset()
        if object_interacted(interactIds=[10001211], arg2=0):
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


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8331,8332,8333,8334,8335,8336,8337,8338], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8330], visible=False)
        set_interact_object(triggerIds=[10001195], state=0) # On
        set_interact_object(triggerIds=[10001211], state=0) # Off
        set_user_value(key='Barrier33', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


