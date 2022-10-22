""" trigger/61000022_me/barrier_8230.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=2) # On
        set_interact_object(triggerIds=[10000960], state=2) # Off

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
        if user_value(key='Barrier23', value=7):
            return Sensor7237()
        if user_value(key='Barrier23', value=8):
            return Sensor7238()
        if user_value(key='Barrier23', value=9):
            return Sensor7239()
        if user_value(key='Barrier23', value=6):
            return Sensor7236()
        if user_value(key='Barrier23', value=15):
            return Sensor72315()
        if user_value(key='Barrier23', value=20):
            return Sensor72320()
        if user_value(key='Barrier23', value=25):
            return Sensor72325()
        if user_value(key='Barrier23', value=30):
            return Sensor72330()


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
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

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
            return Enable7232()
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7232(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7232()
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7232(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7232()


class Delay7232(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
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
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

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
            return Enable7233()
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7233(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7233()
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7233(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7233()


class Delay7233(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
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
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

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
            return Enable7234()
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7234(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7234()
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7234(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7234()


class Delay7234(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
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
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

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
            return Enable7235()
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7235(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7235()
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7235(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7235()


class Delay7235(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
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


#  7명 
class Sensor7237(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=7, operator='Equal'):
            return SafeGreen7237()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7237(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=7, operator='Equal'):
            return Enable7237()
        if not count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7237(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7237()
        if not count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7237(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7237()


class Delay7237(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate7237()


class DeActivate7237(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7237()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  8명 
class Sensor7238(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=8, operator='Equal'):
            return SafeGreen7238()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7238(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=8, operator='Equal'):
            return Enable7238()
        if not count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7238(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7238()
        if not count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7238(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7238()


class Delay7238(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate7238()


class DeActivate7238(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7238()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  9명 
class Sensor7239(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=9, operator='Equal'):
            return SafeGreen7239()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7239(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=9, operator='Equal'):
            return Enable7239()
        if not count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7239(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7239()
        if not count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7239(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7239()


class Delay7239(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate7239()


class DeActivate7239(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7239()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  10명 
class Sensor7236(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=10, operator='Equal'):
            return SafeGreen7236()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen7236(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=10, operator='Equal'):
            return Enable7236()
        if not count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable7236(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate7236()
        if not count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate7236(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay7236()


class Delay7236(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate7236()


class DeActivate7236(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor7236()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  15명 
class Sensor72315(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=15, operator='Equal'):
            return SafeGreen72315()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen72315(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=15, operator='Equal'):
            return Enable72315()
        if not count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable72315(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate72315()
        if not count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate72315(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72315()


class Delay72315(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate72315()


class DeActivate72315(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72315()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  20명 
class Sensor72320(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=20, operator='Equal'):
            return SafeGreen72320()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen72320(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=20, operator='Equal'):
            return Enable72320()
        if not count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable72320(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate72320()
        if not count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate72320(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72320()


class Delay72320(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate72320()


class DeActivate72320(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72320()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  25명 
class Sensor72325(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=25, operator='Equal'):
            return SafeGreen72325()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen72325(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=25, operator='Equal'):
            return Enable72325()
        if not count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable72325(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate72325()
        if not count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate72325(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72325()


class Delay72325(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate72325()


class DeActivate72325(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72325()
        if user_value(key='Barrier23', value=10):
            return Reset()


#  30명 
class Sensor72330(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=3) # red
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=30, operator='Equal'):
            return SafeGreen72330()
        if user_value(key='Barrier23', value=10):
            return Reset()


class SafeGreen72330(state.State):
    def on_enter(self):
        set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=30, operator='Equal'):
            return Enable72330()
        if not count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Enable72330(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000944], arg2=0):
            return Activate72330()
        if not count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Activate72330(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=True)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if wait_tick(waitTick=1000):
            return Delay72330()


class Delay72330(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> state.State:
        if not count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330()
        if user_value(key='Barrier23', value=10):
            return Reset()
        if object_interacted(interactIds=[10000960], arg2=0):
            return DeActivate72330()


class DeActivate72330(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8230], visible=False)
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Sensor72330()
        if user_value(key='Barrier23', value=10):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[8230], visible=False)
        set_interact_object(triggerIds=[10000944], state=0) # On
        set_interact_object(triggerIds=[10000960], state=0) # Off
        set_user_value(key='Barrier23', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


