""" trigger/61000022_me/barrier_8320.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=2) # On
        set_interact_object(triggerIds=[10000963], state=2) # Off

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
        if user_value(key='Barrier32', value=7):
            return Sensor7327()
        if user_value(key='Barrier32', value=8):
            return Sensor7328()
        if user_value(key='Barrier32', value=9):
            return Sensor7329()
        if user_value(key='Barrier32', value=6):
            return Sensor7326()
        if user_value(key='Barrier32', value=15):
            return Sensor73215()
        if user_value(key='Barrier32', value=20):
            return Sensor73220()
        if user_value(key='Barrier32', value=25):
            return Sensor73225()
        if user_value(key='Barrier32', value=30):
            return Sensor73230()


#  1명 방어 불가 
class Sensor7321(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=1) # yellow
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

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
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

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
            return Enable7322()
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7322(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7322()
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7322(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7322()


class Delay7322(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=2, operator='Equal'):
            return Sensor7322()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
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
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

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
            return Enable7323()
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7323(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7323()
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7323(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7323()


class Delay7323(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=3, operator='Equal'):
            return Sensor7323()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
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
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

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
            return Enable7324()
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7324(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7324()
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7324(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7324()


class Delay7324(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=4, operator='Equal'):
            return Sensor7324()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
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
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

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
            return Enable7325()
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7325(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7325()
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7325(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7325()


class Delay7325(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=5, operator='Equal'):
            return Sensor7325()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
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


#  7명 
class Sensor7327(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=7, operator='Equal'):
            return SafeGreen7327()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7327(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=7, operator='Equal'):
            return Enable7327()
        if not count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7327(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7327()
        if not count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7327(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7327()


class Delay7327(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=7, operator='Equal'):
            return Sensor7327()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate7327()


class DeActivate7327(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7327()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  8명 
class Sensor7328(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=8, operator='Equal'):
            return SafeGreen7328()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7328(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=8, operator='Equal'):
            return Enable7328()
        if not count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7328(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7328()
        if not count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7328(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7328()


class Delay7328(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=8, operator='Equal'):
            return Sensor7328()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate7328()


class DeActivate7328(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7328()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  9명 
class Sensor7329(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=9, operator='Equal'):
            return SafeGreen7329()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7329(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=9, operator='Equal'):
            return Enable7329()
        if not count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7329(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7329()
        if not count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7329(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7329()


class Delay7329(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=9, operator='Equal'):
            return Sensor7329()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate7329()


class DeActivate7329(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7329()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  10명 
class Sensor7326(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=10, operator='Equal'):
            return SafeGreen7326()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen7326(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=10, operator='Equal'):
            return Enable7326()
        if not count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable7326(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate7326()
        if not count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate7326(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7326()


class Delay7326(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=10, operator='Equal'):
            return Sensor7326()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate7326()


class DeActivate7326(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7326()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  15명 
class Sensor73215(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=15, operator='Equal'):
            return SafeGreen73215()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen73215(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=15, operator='Equal'):
            return Enable73215()
        if not count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable73215(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate73215()
        if not count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate73215(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73215()


class Delay73215(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=15, operator='Equal'):
            return Sensor73215()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate73215()


class DeActivate73215(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73215()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  20명 
class Sensor73220(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=20, operator='Equal'):
            return SafeGreen73220()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen73220(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=20, operator='Equal'):
            return Enable73220()
        if not count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable73220(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate73220()
        if not count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate73220(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73220()


class Delay73220(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=20, operator='Equal'):
            return Sensor73220()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate73220()


class DeActivate73220(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73220()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  25명 
class Sensor73225(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=25, operator='Equal'):
            return SafeGreen73225()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen73225(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=25, operator='Equal'):
            return Enable73225()
        if not count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable73225(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate73225()
        if not count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate73225(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73225()


class Delay73225(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=25, operator='Equal'):
            return Sensor73225()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate73225()


class DeActivate73225(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73225()
        if user_value(key='Barrier32', value=10):
            return Reset()


#  30명 
class Sensor73230(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=3) # red
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=30, operator='Equal'):
            return SafeGreen73230()
        if user_value(key='Barrier32', value=10):
            return Reset()


class SafeGreen73230(state.State):
    def on_enter(self):
        set_user_value(triggerId=7320, key='Color32', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9320, boxId=30, operator='Equal'):
            return Enable73230()
        if not count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Enable73230(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9320], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000947], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000947], arg2=0):
            return Activate73230()
        if not count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Activate73230(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=True)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000947], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay73230()


class Delay73230(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000963], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9320, boxId=30, operator='Equal'):
            return Sensor73230()
        if user_value(key='Barrier32', value=10):
            return Reset()
        if object_interacted(interactIds=[10000963], arg2=0):
            return DeActivate73230()


class DeActivate73230(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8320], visible=False)
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor73230()
        if user_value(key='Barrier32', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8321,8322,8323,8324,8325,8326,8327,8328], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8320], visible=False)
        set_interact_object(triggerIds=[10000947], state=0) # On
        set_interact_object(triggerIds=[10000963], state=0) # Off
        set_user_value(key='Barrier32', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


