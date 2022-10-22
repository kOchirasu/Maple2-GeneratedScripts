""" trigger/84000007_wd/barrier_8130.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8130], visible=False)
        set_interact_object(triggerIds=[10000940], state=2) # On
        set_interact_object(triggerIds=[10000956], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier13', value=1):
            return Sensor7131()
        if user_value(key='Barrier13', value=2):
            return Sensor7132()
        if user_value(key='Barrier13', value=3):
            return Sensor7133()
        if user_value(key='Barrier13', value=4):
            return Sensor7134()
        if user_value(key='Barrier13', value=5):
            return Sensor7135()


#  1명 방어 불가 
class Sensor7131(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=1, operator='Equal'):
            return Activate7131()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Activate7131(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=1, operator='Equal'):
            return Sensor7131()
        if user_value(key='Barrier13', value=10):
            return Reset()


#  2명 
class Sensor7132(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8130], visible=False)
        set_interact_object(triggerIds=[10000940], state=0) # On
        set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=2, operator='Equal'):
            return SafeGreen7132()
        if user_value(key='Barrier13', value=10):
            return Reset()


class SafeGreen7132(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=2, operator='Equal'):
            return Enable7132()
        if not count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Enable7132(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000940], arg2=0):
            return Activate7132()
        if not count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Activate7132(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=True)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7132()


class Delay7132(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if object_interacted(interactIds=[10000956], arg2=0):
            return DeActivate7132()


class DeActivate7132(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=False)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7132()
        if user_value(key='Barrier13', value=10):
            return Reset()


#  3명 
class Sensor7133(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8130], visible=False)
        set_interact_object(triggerIds=[10000940], state=0) # On
        set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=3, operator='Equal'):
            return SafeGreen7133()
        if user_value(key='Barrier13', value=10):
            return Reset()


class SafeGreen7133(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=3, operator='Equal'):
            return Enable7133()
        if not count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Enable7133(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000940], arg2=0):
            return Activate7133()
        if not count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Activate7133(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=True)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7133()


class Delay7133(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if object_interacted(interactIds=[10000956], arg2=0):
            return DeActivate7133()


class DeActivate7133(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=False)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7133()
        if user_value(key='Barrier13', value=10):
            return Reset()


#  4명 
class Sensor7134(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8130], visible=False)
        set_interact_object(triggerIds=[10000940], state=0) # On
        set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=4, operator='Equal'):
            return SafeGreen7134()
        if user_value(key='Barrier13', value=10):
            return Reset()


class SafeGreen7134(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=4, operator='Equal'):
            return Enable7134()
        if not count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Enable7134(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000940], arg2=0):
            return Activate7134()
        if not count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Activate7134(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=True)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7134()


class Delay7134(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if object_interacted(interactIds=[10000956], arg2=0):
            return DeActivate7134()


class DeActivate7134(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=False)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7134()
        if user_value(key='Barrier13', value=10):
            return Reset()


#  5명 
class Sensor7135(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8130], visible=False)
        set_interact_object(triggerIds=[10000940], state=0) # On
        set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=5, operator='Equal'):
            return SafeGreen7135()
        if user_value(key='Barrier13', value=10):
            return Reset()


class SafeGreen7135(state.State):
    def on_enter(self):
        set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9130, boxId=5, operator='Equal'):
            return Enable7135()
        if not count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Enable7135(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000940], arg2=0):
            return Activate7135()
        if not count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Activate7135(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=True)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7135()


class Delay7135(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135()
        if user_value(key='Barrier13', value=10):
            return Reset()
        if object_interacted(interactIds=[10000956], arg2=0):
            return DeActivate7135()


class DeActivate7135(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8130], visible=False)
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7135()
        if user_value(key='Barrier13', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8130], visible=False)
        set_interact_object(triggerIds=[10000940], state=0) # On
        set_interact_object(triggerIds=[10000956], state=0) # Off
        set_user_value(key='Barrier13', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


