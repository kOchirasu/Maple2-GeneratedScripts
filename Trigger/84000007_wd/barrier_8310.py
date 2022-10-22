""" trigger/84000007_wd/barrier_8310.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8310], visible=False)
        set_interact_object(triggerIds=[10000946], state=2) # On
        set_interact_object(triggerIds=[10000962], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier31', value=1):
            return Sensor7311()
        if user_value(key='Barrier31', value=2):
            return Sensor7312()
        if user_value(key='Barrier31', value=3):
            return Sensor7313()
        if user_value(key='Barrier31', value=4):
            return Sensor7314()
        if user_value(key='Barrier31', value=5):
            return Sensor7315()


#  1명 방어 불가 
class Sensor7311(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=1, operator='Equal'):
            return Activate7311()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Activate7311(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=1, operator='Equal'):
            return Sensor7311()
        if user_value(key='Barrier31', value=10):
            return Reset()


#  2명 
class Sensor7312(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=1) # yellow
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8310], visible=False)
        set_interact_object(triggerIds=[10000946], state=0) # On
        set_interact_object(triggerIds=[10000962], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=2, operator='Equal'):
            return SafeGreen7312()
        if user_value(key='Barrier31', value=10):
            return Reset()


class SafeGreen7312(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=2, operator='Equal'):
            return Enable7312()
        if not count_users(boxId=9310, boxId=2, operator='Equal'):
            return Sensor7312()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Enable7312(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9310], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000946], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000946], arg2=0):
            return Activate7312()
        if not count_users(boxId=9310, boxId=2, operator='Equal'):
            return Sensor7312()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Activate7312(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=True)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000946], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=2, operator='Equal'):
            return Sensor7312()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7312()


class Delay7312(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000962], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=2, operator='Equal'):
            return Sensor7312()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if object_interacted(interactIds=[10000962], arg2=0):
            return DeActivate7312()


class DeActivate7312(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=False)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7312()
        if user_value(key='Barrier31', value=10):
            return Reset()


#  3명 
class Sensor7313(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=1) # yellow
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8310], visible=False)
        set_interact_object(triggerIds=[10000946], state=0) # On
        set_interact_object(triggerIds=[10000962], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=3, operator='Equal'):
            return SafeGreen7313()
        if user_value(key='Barrier31', value=10):
            return Reset()


class SafeGreen7313(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=3, operator='Equal'):
            return Enable7313()
        if not count_users(boxId=9310, boxId=3, operator='Equal'):
            return Sensor7313()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Enable7313(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9310], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000946], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000946], arg2=0):
            return Activate7313()
        if not count_users(boxId=9310, boxId=3, operator='Equal'):
            return Sensor7313()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Activate7313(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=True)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000946], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=3, operator='Equal'):
            return Sensor7313()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7313()


class Delay7313(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000962], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=3, operator='Equal'):
            return Sensor7313()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if object_interacted(interactIds=[10000962], arg2=0):
            return DeActivate7313()


class DeActivate7313(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=False)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7313()
        if user_value(key='Barrier31', value=10):
            return Reset()


#  4명 
class Sensor7314(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=1) # yellow
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8310], visible=False)
        set_interact_object(triggerIds=[10000946], state=0) # On
        set_interact_object(triggerIds=[10000962], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=4, operator='Equal'):
            return SafeGreen7314()
        if user_value(key='Barrier31', value=10):
            return Reset()


class SafeGreen7314(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=4, operator='Equal'):
            return Enable7314()
        if not count_users(boxId=9310, boxId=4, operator='Equal'):
            return Sensor7314()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Enable7314(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9310], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000946], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000946], arg2=0):
            return Activate7314()
        if not count_users(boxId=9310, boxId=4, operator='Equal'):
            return Sensor7314()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Activate7314(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=True)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000946], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=4, operator='Equal'):
            return Sensor7314()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7314()


class Delay7314(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000962], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=4, operator='Equal'):
            return Sensor7314()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if object_interacted(interactIds=[10000962], arg2=0):
            return DeActivate7314()


class DeActivate7314(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=False)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7314()
        if user_value(key='Barrier31', value=10):
            return Reset()


#  5명 
class Sensor7315(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=1) # yellow
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8310], visible=False)
        set_interact_object(triggerIds=[10000946], state=0) # On
        set_interact_object(triggerIds=[10000962], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=5, operator='Equal'):
            return SafeGreen7315()
        if user_value(key='Barrier31', value=10):
            return Reset()


class SafeGreen7315(state.State):
    def on_enter(self):
        set_user_value(triggerId=7310, key='Color31', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=5, operator='Equal'):
            return Enable7315()
        if not count_users(boxId=9310, boxId=5, operator='Equal'):
            return Sensor7315()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Enable7315(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9310], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000946], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000946], arg2=0):
            return Activate7315()
        if not count_users(boxId=9310, boxId=5, operator='Equal'):
            return Sensor7315()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Activate7315(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=True)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000946], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=5, operator='Equal'):
            return Sensor7315()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7315()


class Delay7315(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000962], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9310, boxId=5, operator='Equal'):
            return Sensor7315()
        if user_value(key='Barrier31', value=10):
            return Reset()
        if object_interacted(interactIds=[10000962], arg2=0):
            return DeActivate7315()


class DeActivate7315(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8310], visible=False)
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7315()
        if user_value(key='Barrier31', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8311,8312,8313,8314,8315,8316], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8310], visible=False)
        set_interact_object(triggerIds=[10000946], state=0) # On
        set_interact_object(triggerIds=[10000962], state=0) # Off
        set_user_value(key='Barrier31', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


