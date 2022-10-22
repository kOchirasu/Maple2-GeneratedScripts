""" trigger/66200001_gd/barrier_8320.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10001194], state=2) # On
        set_interact_object(triggerIds=[10001210], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier32', value=1):
            return Sensor7321()
        if user_value(key='Barrier32', value=2):
            return Sensor7322()
        if user_value(key='Barrier32', value=3):
            return Sensor7323()
        if user_value(key='Barrier32', value=4):
            return Sensor7324()
        if user_value(key='Barrier32', value=5):
            return Sensor7325()


#  1명 방어 불가 
class Sensor7321(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=1, operator='Equal'):
            return Activate7321()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7321(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=1, operator='Equal'):
            return Sensor7321()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  2명 
class Sensor7322(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10001194], state=0) # On
        set_interact_object(triggerIds=[10001210], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=2, operator='Equal'):
            return SafeGreen7322()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7322(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=2, operator='Equal'):
            return CheckSameUserTag7322()
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()


class CheckSameUserTag7322(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7322()
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if not check_same_user_tag(boxId=9320):
            return SafeGreen7322()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7322(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001194], arg2=0):
            return Activate7322()
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7322(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7322()


class Delay7322(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10001210], arg2=0):
            return DeActivate7322()


class DeActivate7322(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  3명 
class Sensor7323(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10001194], state=0) # On
        set_interact_object(triggerIds=[10001210], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=3, operator='Equal'):
            return SafeGreen7323()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7323(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=3, operator='Equal'):
            return CheckSameUserTag7323()
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()


class CheckSameUserTag7323(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7323()
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if not check_same_user_tag(boxId=9320):
            return SafeGreen7323()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7323(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001194], arg2=0):
            return Activate7323()
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7323(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7323()


class Delay7323(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10001210], arg2=0):
            return DeActivate7323()


class DeActivate7323(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  4명 
class Sensor7324(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10001194], state=0) # On
        set_interact_object(triggerIds=[10001210], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=4, operator='Equal'):
            return SafeGreen7324()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7324(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=4, operator='Equal'):
            return CheckSameUserTag7324()
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()


class CheckSameUserTag7324(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7324()
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if not check_same_user_tag(boxId=9320):
            return SafeGreen7324()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7324(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001194], arg2=0):
            return Activate7324()
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7324(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7324()


class Delay7324(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10001210], arg2=0):
            return DeActivate7324()


class DeActivate7324(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  5명 
class Sensor7325(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10001194], state=0) # On
        set_interact_object(triggerIds=[10001210], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=5, operator='Equal'):
            return SafeGreen7325()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7325(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=5, operator='Equal'):
            return CheckSameUserTag7325()
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()


class CheckSameUserTag7325(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7325()
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if not check_same_user_tag(boxId=9320):
            return SafeGreen7325()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7325(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001194], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001194], arg2=0):
            return Activate7325()
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7325(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001194], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7325()


class Delay7325(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001210], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10001210], arg2=0):
            return DeActivate7325()


class DeActivate7325(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10001194], state=0) # On
        set_interact_object(triggerIds=[10001210], state=0) # Off
        set_user_value(key='Barrier32', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


