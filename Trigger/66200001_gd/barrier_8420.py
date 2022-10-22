""" trigger/66200001_gd/barrier_8420.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8420], visible=False)
        set_interact_object(triggerIds=[10001198], state=2) # On
        set_interact_object(triggerIds=[10001214], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier42', value=1):
            return Sensor7421()
        if user_value(key='Barrier42', value=2):
            return Sensor7422()
        if user_value(key='Barrier42', value=3):
            return Sensor7423()
        if user_value(key='Barrier42', value=4):
            return Sensor7424()
        if user_value(key='Barrier42', value=5):
            return Sensor7425()


#  1명 방어 불가 
class Sensor7421(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=1, operator='Equal'):
            return Activate7421()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Activate7421(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=1, operator='Equal'):
            return Sensor7421()
        if user_value(key='Barrier42', value=10):
            return Reset()


#  2명 
class Sensor7422(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8420], visible=False)
        set_interact_object(triggerIds=[10001198], state=0) # On
        set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=2, operator='Equal'):
            return SafeGreen7422()
        if user_value(key='Barrier42', value=10):
            return Reset()


class SafeGreen7422(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=2, operator='Equal'):
            return CheckSameUserTag7422()
        if not count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422()
        if user_value(key='Barrier42', value=10):
            return Reset()


class CheckSameUserTag7422(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7422()
        if not count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422()
        if not check_same_user_tag(boxId=9420):
            return SafeGreen7422()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Enable7422(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001198], arg2=0):
            return Activate7422()
        if not count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Activate7422(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=True)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7422()


class Delay7422(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=2, operator='Equal'):
            return Sensor7422()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if object_interacted(interactIds=[10001214], arg2=0):
            return DeActivate7422()


class DeActivate7422(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=False)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7422()
        if user_value(key='Barrier42', value=10):
            return Reset()


#  3명 
class Sensor7423(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8420], visible=False)
        set_interact_object(triggerIds=[10001198], state=0) # On
        set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=3, operator='Equal'):
            return SafeGreen7423()
        if user_value(key='Barrier42', value=10):
            return Reset()


class SafeGreen7423(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=3, operator='Equal'):
            return CheckSameUserTag7423()
        if not count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423()
        if user_value(key='Barrier42', value=10):
            return Reset()


class CheckSameUserTag7423(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7423()
        if not count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423()
        if not check_same_user_tag(boxId=9420):
            return SafeGreen7423()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Enable7423(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001198], arg2=0):
            return Activate7423()
        if not count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Activate7423(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=True)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7423()


class Delay7423(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=3, operator='Equal'):
            return Sensor7423()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if object_interacted(interactIds=[10001214], arg2=0):
            return DeActivate7423()


class DeActivate7423(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=False)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7423()
        if user_value(key='Barrier42', value=10):
            return Reset()


#  4명 
class Sensor7424(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8420], visible=False)
        set_interact_object(triggerIds=[10001198], state=0) # On
        set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=4, operator='Equal'):
            return SafeGreen7424()
        if user_value(key='Barrier42', value=10):
            return Reset()


class SafeGreen7424(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=4, operator='Equal'):
            return CheckSameUserTag7424()
        if not count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424()
        if user_value(key='Barrier42', value=10):
            return Reset()


class CheckSameUserTag7424(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7424()
        if not count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424()
        if not check_same_user_tag(boxId=9420):
            return SafeGreen7424()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Enable7424(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001198], arg2=0):
            return Activate7424()
        if not count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Activate7424(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=True)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7424()


class Delay7424(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=4, operator='Equal'):
            return Sensor7424()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if object_interacted(interactIds=[10001214], arg2=0):
            return DeActivate7424()


class DeActivate7424(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=False)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7424()
        if user_value(key='Barrier42', value=10):
            return Reset()


#  5명 
class Sensor7425(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=1) # yellow
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8420], visible=False)
        set_interact_object(triggerIds=[10001198], state=0) # On
        set_interact_object(triggerIds=[10001214], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=5, operator='Equal'):
            return SafeGreen7425()
        if user_value(key='Barrier42', value=10):
            return Reset()


class SafeGreen7425(state.State):
    def on_enter(self):
        set_user_value(triggerId=7420, key='Color42', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9420, boxId=5, operator='Equal'):
            return CheckSameUserTag7425()
        if not count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425()
        if user_value(key='Barrier42', value=10):
            return Reset()


class CheckSameUserTag7425(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7425()
        if not count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425()
        if not check_same_user_tag(boxId=9420):
            return SafeGreen7425()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Enable7425(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9420], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001198], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001198], arg2=0):
            return Activate7425()
        if not count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Activate7425(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=True)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001198], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7425()


class Delay7425(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001214], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9420, boxId=5, operator='Equal'):
            return Sensor7425()
        if user_value(key='Barrier42', value=10):
            return Reset()
        if object_interacted(interactIds=[10001214], arg2=0):
            return DeActivate7425()


class DeActivate7425(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8420], visible=False)
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7425()
        if user_value(key='Barrier42', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8421,8422,8423,8424,8425,8426], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8420], visible=False)
        set_interact_object(triggerIds=[10001198], state=0) # On
        set_interact_object(triggerIds=[10001214], state=0) # Off
        set_user_value(key='Barrier42', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


