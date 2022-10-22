""" trigger/61000008_me/barrier_8140.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8140], visible=False)
        set_interact_object(triggerIds=[10000941], state=2) # On
        set_interact_object(triggerIds=[10000957], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier14', value=1):
            return Sensor7141()
        if user_value(key='Barrier14', value=2):
            return Sensor7142()
        if user_value(key='Barrier14', value=3):
            return Sensor7143()
        if user_value(key='Barrier14', value=4):
            return Sensor7144()
        if user_value(key='Barrier14', value=5):
            return Sensor7145()


#  1명 방어 불가 
class Sensor7141(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=1, operator='Equal'):
            return Activate7141()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Activate7141(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=1, operator='Equal'):
            return Sensor7141()
        if user_value(key='Barrier14', value=10):
            return Reset()


#  2명 
class Sensor7142(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8140], visible=False)
        set_interact_object(triggerIds=[10000941], state=0) # On
        set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=2, operator='Equal'):
            return SafeGreen7142()
        if user_value(key='Barrier14', value=10):
            return Reset()


class SafeGreen7142(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=2, operator='Equal'):
            return Enable7142()
        if not count_users(boxId=9140, boxId=2, operator='Equal'):
            return Sensor7142()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Enable7142(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000941], arg2=0):
            return Activate7142()
        if not count_users(boxId=9140, boxId=2, operator='Equal'):
            return Sensor7142()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Activate7142(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=True)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=2, operator='Equal'):
            return Sensor7142()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7142()


class Delay7142(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=2, operator='Equal'):
            return Sensor7142()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if object_interacted(interactIds=[10000957], arg2=0):
            return DeActivate7142()


class DeActivate7142(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=False)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7142()
        if user_value(key='Barrier14', value=10):
            return Reset()


#  3명 
class Sensor7143(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8140], visible=False)
        set_interact_object(triggerIds=[10000941], state=0) # On
        set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=3, operator='Equal'):
            return SafeGreen7143()
        if user_value(key='Barrier14', value=10):
            return Reset()


class SafeGreen7143(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=3, operator='Equal'):
            return Enable7143()
        if not count_users(boxId=9140, boxId=3, operator='Equal'):
            return Sensor7143()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Enable7143(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000941], arg2=0):
            return Activate7143()
        if not count_users(boxId=9140, boxId=3, operator='Equal'):
            return Sensor7143()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Activate7143(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=True)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=3, operator='Equal'):
            return Sensor7143()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7143()


class Delay7143(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=3, operator='Equal'):
            return Sensor7143()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if object_interacted(interactIds=[10000957], arg2=0):
            return DeActivate7143()


class DeActivate7143(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=False)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7143()
        if user_value(key='Barrier14', value=10):
            return Reset()


#  4명 
class Sensor7144(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8140], visible=False)
        set_interact_object(triggerIds=[10000941], state=0) # On
        set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=4, operator='Equal'):
            return SafeGreen7144()
        if user_value(key='Barrier14', value=10):
            return Reset()


class SafeGreen7144(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=4, operator='Equal'):
            return Enable7144()
        if not count_users(boxId=9140, boxId=4, operator='Equal'):
            return Sensor7144()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Enable7144(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000941], arg2=0):
            return Activate7144()
        if not count_users(boxId=9140, boxId=4, operator='Equal'):
            return Sensor7144()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Activate7144(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=True)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=4, operator='Equal'):
            return Sensor7144()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7144()


class Delay7144(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=4, operator='Equal'):
            return Sensor7144()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if object_interacted(interactIds=[10000957], arg2=0):
            return DeActivate7144()


class DeActivate7144(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=False)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7144()
        if user_value(key='Barrier14', value=10):
            return Reset()


#  5명 
class Sensor7145(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=1) # yellow
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8140], visible=False)
        set_interact_object(triggerIds=[10000941], state=0) # On
        set_interact_object(triggerIds=[10000957], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=5, operator='Equal'):
            return SafeGreen7145()
        if user_value(key='Barrier14', value=10):
            return Reset()


class SafeGreen7145(state.State):
    def on_enter(self):
        set_user_value(triggerId=7140, key='Color14', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9140, boxId=5, operator='Equal'):
            return Enable7145()
        if not count_users(boxId=9140, boxId=5, operator='Equal'):
            return Sensor7145()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Enable7145(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9140], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000941], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000941], arg2=0):
            return Activate7145()
        if not count_users(boxId=9140, boxId=5, operator='Equal'):
            return Sensor7145()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Activate7145(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=True)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000941], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=5, operator='Equal'):
            return Sensor7145()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7145()


class Delay7145(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000957], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9140, boxId=5, operator='Equal'):
            return Sensor7145()
        if user_value(key='Barrier14', value=10):
            return Reset()
        if object_interacted(interactIds=[10000957], arg2=0):
            return DeActivate7145()


class DeActivate7145(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8140], visible=False)
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7145()
        if user_value(key='Barrier14', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8141,8142,8143,8144], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8140], visible=False)
        set_interact_object(triggerIds=[10000941], state=0) # On
        set_interact_object(triggerIds=[10000957], state=0) # Off
        set_user_value(key='Barrier14', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


