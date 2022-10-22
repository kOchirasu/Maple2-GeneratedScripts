""" trigger/66200001_gd/barrier_8230.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10001191], state=2) # On
        set_interact_object(triggerIds=[10001207], state=2) # Off

    def on_tick(self) -> state.State:
        if user_value(key='Barrier23', value=1):
            return Sensor7231()
        if user_value(key='Barrier23', value=2):
            return Sensor7232()
        if user_value(key='Barrier23', value=3):
            return Sensor7233()
        if user_value(key='Barrier23', value=4):
            return Sensor7234()
        if user_value(key='Barrier23', value=5):
            return Sensor7235()


#  1명 방어 불가 
class Sensor7231(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=1) # yellow

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=1, operator='Equal'):
            return Activate7231()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7231(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=1, operator='Equal'):
            return Sensor7231()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  2명 
class Sensor7232(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10001191], state=0) # On
        set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=2, operator='Equal'):
            return SafeGreen7232()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7232(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=2, operator='Equal'):
            return CheckSameUserTag7232()
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()


class CheckSameUserTag7232(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7232()
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if not check_same_user_tag(boxId=9230):
            return SafeGreen7232()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7232(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001191], arg2=0):
            return Activate7232()
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7232(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7232()


class Delay7232(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10001207], arg2=0):
            return DeActivate7232()


class DeActivate7232(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  3명 
class Sensor7233(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10001191], state=0) # On
        set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=3, operator='Equal'):
            return SafeGreen7233()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7233(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=3, operator='Equal'):
            return CheckSameUserTag7233()
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()


class CheckSameUserTag7233(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7233()
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if not check_same_user_tag(boxId=9230):
            return SafeGreen7233()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7233(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001191], arg2=0):
            return Activate7233()
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7233(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7233()


class Delay7233(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10001207], arg2=0):
            return DeActivate7233()


class DeActivate7233(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  4명 
class Sensor7234(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10001191], state=0) # On
        set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=4, operator='Equal'):
            return SafeGreen7234()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7234(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=4, operator='Equal'):
            return CheckSameUserTag7234()
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()


class CheckSameUserTag7234(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7234()
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if not check_same_user_tag(boxId=9230):
            return SafeGreen7234()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7234(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001191], arg2=0):
            return Activate7234()
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7234(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7234()


class Delay7234(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10001207], arg2=0):
            return DeActivate7234()


class DeActivate7234(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  5명 
class Sensor7235(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10001191], state=0) # On
        set_interact_object(triggerIds=[10001207], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=5, operator='Equal'):
            return SafeGreen7235()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7235(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=5, operator='Equal'):
            return CheckSameUserTag7235()
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()


class CheckSameUserTag7235(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return Enable7235()
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if not check_same_user_tag(boxId=9230):
            return SafeGreen7235()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7235(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10001191], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001191], arg2=0):
            return Activate7235()
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7235(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10001191], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7235()


class Delay7235(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001207], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10001207], arg2=0):
            return DeActivate7235()


class DeActivate7235(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10001191], state=0) # On
        set_interact_object(triggerIds=[10001207], state=0) # Off
        set_user_value(key='Barrier23', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()

