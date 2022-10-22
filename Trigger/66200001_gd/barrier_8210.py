""" trigger/66200001_gd/barrier_8210.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8210], visible=False)
        set_interact_object(triggerIds=[10001189], state=2) # On
        set_interact_object(triggerIds=[10001205], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier21', value=1):
            return Sensor7211()
        if user_value(key='Barrier21', value=2):
            return Sensor7212()
        if user_value(key='Barrier21', value=3):
            return Sensor7213()
        if user_value(key='Barrier21', value=4):
            return Sensor7214()
        if user_value(key='Barrier21', value=5):
            return Sensor7215()


#  1명 방어 불가 
class Sensor7211(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=1, operator='Equal'):
            return Activate7211()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Activate7211(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=1, operator='Equal'):
            return Sensor7211()
        if user_value(key='Barrier21', value=10):
            return Reset()


#  2명 
class Sensor7212(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8210], visible=False)
        set_interact_object(triggerIds=[10001189], state=0) # On
        set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=2, operator='Equal'):
            return SafeGreen7212()
        if user_value(key='Barrier21', value=10):
            return Reset()


class SafeGreen7212(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=2, operator='Equal'):
            return CheckSameUserTag7212()
        if not count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212()
        if user_value(key='Barrier21', value=10):
            return Reset()


class CheckSameUserTag7212(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7212()
        if not count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212()
        if not check_same_user_tag(boxId=9210):
            return SafeGreen7212()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Enable7212(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001189], arg2=0):
            return Activate7212()
        if not count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Activate7212(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=True)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7212()


class Delay7212(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=2, operator='Equal'):
            return Sensor7212()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if object_interacted(interactIds=[10001205], arg2=0):
            return DeActivate7212()


class DeActivate7212(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=False)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7212()
        if user_value(key='Barrier21', value=10):
            return Reset()


#  3명 
class Sensor7213(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8210], visible=False)
        set_interact_object(triggerIds=[10001189], state=0) # On
        set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=3, operator='Equal'):
            return SafeGreen7213()
        if user_value(key='Barrier21', value=10):
            return Reset()


class SafeGreen7213(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=3, operator='Equal'):
            return CheckSameUserTag7213()
        if not count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213()
        if user_value(key='Barrier21', value=10):
            return Reset()


class CheckSameUserTag7213(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7213()
        if not count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213()
        if not check_same_user_tag(boxId=9210):
            return SafeGreen7213()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Enable7213(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001189], arg2=0):
            return Activate7213()
        if not count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Activate7213(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=True)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7213()


class Delay7213(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=3, operator='Equal'):
            return Sensor7213()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if object_interacted(interactIds=[10001205], arg2=0):
            return DeActivate7213()


class DeActivate7213(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=False)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7213()
        if user_value(key='Barrier21', value=10):
            return Reset()


#  4명 
class Sensor7214(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8210], visible=False)
        set_interact_object(triggerIds=[10001189], state=0) # On
        set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=4, operator='Equal'):
            return SafeGreen7214()
        if user_value(key='Barrier21', value=10):
            return Reset()


class SafeGreen7214(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=4, operator='Equal'):
            return CheckSameUserTag7214()
        if not count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214()
        if user_value(key='Barrier21', value=10):
            return Reset()


class CheckSameUserTag7214(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7214()
        if not count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214()
        if not check_same_user_tag(boxId=9210):
            return SafeGreen7214()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Enable7214(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001189], arg2=0):
            return Activate7214()
        if not count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Activate7214(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=True)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7214()


class Delay7214(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=4, operator='Equal'):
            return Sensor7214()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if object_interacted(interactIds=[10001205], arg2=0):
            return DeActivate7214()


class DeActivate7214(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=False)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7214()
        if user_value(key='Barrier21', value=10):
            return Reset()


#  5명 
class Sensor7215(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=1) # yellow
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8210], visible=False)
        set_interact_object(triggerIds=[10001189], state=0) # On
        set_interact_object(triggerIds=[10001205], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=5, operator='Equal'):
            return SafeGreen7215()
        if user_value(key='Barrier21', value=10):
            return Reset()


class SafeGreen7215(state.State):
    def on_enter(self):
        set_user_value(triggerId=7210, key='Color21', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9210, boxId=5, operator='Equal'):
            return CheckSameUserTag7215()
        if not count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215()
        if user_value(key='Barrier21', value=10):
            return Reset()


class CheckSameUserTag7215(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7215()
        if not count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215()
        if not check_same_user_tag(boxId=9210):
            return SafeGreen7215()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Enable7215(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9210], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001189], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001189], arg2=0):
            return Activate7215()
        if not count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Activate7215(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=True)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001189], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7215()


class Delay7215(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001205], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9210, boxId=5, operator='Equal'):
            return Sensor7215()
        if user_value(key='Barrier21', value=10):
            return Reset()
        if object_interacted(interactIds=[10001205], arg2=0):
            return DeActivate7215()


class DeActivate7215(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8210], visible=False)
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7215()
        if user_value(key='Barrier21', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8211,8212,8213,8214,8215,8216], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8210], visible=False)
        set_interact_object(triggerIds=[10001189], state=0) # On
        set_interact_object(triggerIds=[10001205], state=0) # Off
        set_user_value(key='Barrier21', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


