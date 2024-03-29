""" trigger/84000007_wd/barrier_8230.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=2) # On
        self.set_interact_object(triggerIds=[10000960], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier23', value=1):
            return Sensor7231(self.ctx)
        if self.user_value(key='Barrier23', value=2):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=3):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=4):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=5):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=7):
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23', value=8):
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23', value=9):
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23', value=6):
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23', value=15):
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23', value=20):
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23', value=25):
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23', value=30):
            return Sensor72330(self.ctx)


# 1명 방어 불가
class Sensor7231(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=1, operator='Equal'):
            return Activate7231(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7231(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=1, operator='Equal'):
            return Sensor7231(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7232(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return SafeGreen7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7232(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Enable7232(self.ctx)
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7232(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7232(self.ctx)
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7232(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7232(self.ctx)


class Delay7232(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=2, operator='Equal'):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7232(self.ctx)


class DeActivate7232(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7232(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7233(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return SafeGreen7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7233(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Enable7233(self.ctx)
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7233(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7233(self.ctx)
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7233(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7233(self.ctx)


class Delay7233(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=3, operator='Equal'):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7233(self.ctx)


class DeActivate7233(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7233(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7234(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return SafeGreen7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7234(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Enable7234(self.ctx)
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7234(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7234(self.ctx)
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7234(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7234(self.ctx)


class Delay7234(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=4, operator='Equal'):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7234(self.ctx)


class DeActivate7234(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7234(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7235(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=1) # yellow
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return SafeGreen7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7235(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Enable7235(self.ctx)
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7235(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7235(self.ctx)
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7235(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7235(self.ctx)


class Delay7235(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=5, operator='Equal'):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7235(self.ctx)


class DeActivate7235(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7235(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 7명
class Sensor7237(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=7, operator='Equal'):
            return SafeGreen7237(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7237(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=7, operator='Equal'):
            return Enable7237(self.ctx)
        if not self.count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7237(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7237(self.ctx)
        if not self.count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7237(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7237(self.ctx)


class Delay7237(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=7, operator='Equal'):
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7237(self.ctx)


class DeActivate7237(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7237(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 8명
class Sensor7238(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=8, operator='Equal'):
            return SafeGreen7238(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7238(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=8, operator='Equal'):
            return Enable7238(self.ctx)
        if not self.count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7238(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7238(self.ctx)
        if not self.count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7238(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7238(self.ctx)


class Delay7238(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=8, operator='Equal'):
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7238(self.ctx)


class DeActivate7238(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7238(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 9명
class Sensor7239(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=9, operator='Equal'):
            return SafeGreen7239(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7239(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=9, operator='Equal'):
            return Enable7239(self.ctx)
        if not self.count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7239(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7239(self.ctx)
        if not self.count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7239(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7239(self.ctx)


class Delay7239(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=9, operator='Equal'):
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7239(self.ctx)


class DeActivate7239(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7239(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 10명
class Sensor7236(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=10, operator='Equal'):
            return SafeGreen7236(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen7236(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=10, operator='Equal'):
            return Enable7236(self.ctx)
        if not self.count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable7236(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate7236(self.ctx)
        if not self.count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate7236(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7236(self.ctx)


class Delay7236(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=10, operator='Equal'):
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate7236(self.ctx)


class DeActivate7236(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7236(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 15명
class Sensor72315(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=15, operator='Equal'):
            return SafeGreen72315(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen72315(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=15, operator='Equal'):
            return Enable72315(self.ctx)
        if not self.count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable72315(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate72315(self.ctx)
        if not self.count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate72315(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72315(self.ctx)


class Delay72315(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=15, operator='Equal'):
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate72315(self.ctx)


class DeActivate72315(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72315(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 20명
class Sensor72320(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=20, operator='Equal'):
            return SafeGreen72320(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen72320(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=20, operator='Equal'):
            return Enable72320(self.ctx)
        if not self.count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable72320(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate72320(self.ctx)
        if not self.count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate72320(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72320(self.ctx)


class Delay72320(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=20, operator='Equal'):
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate72320(self.ctx)


class DeActivate72320(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72320(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 25명
class Sensor72325(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=25, operator='Equal'):
            return SafeGreen72325(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen72325(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=25, operator='Equal'):
            return Enable72325(self.ctx)
        if not self.count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable72325(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate72325(self.ctx)
        if not self.count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate72325(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72325(self.ctx)


class Delay72325(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=25, operator='Equal'):
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate72325(self.ctx)


class DeActivate72325(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72325(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


# 30명
class Sensor72330(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=3) # red
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=30, operator='Equal'):
            return SafeGreen72330(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class SafeGreen72330(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7230, key='Color23', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9230, boxId=30, operator='Equal'):
            return Enable72330(self.ctx)
        if not self.count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Enable72330(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000944], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000944], stateValue=0):
            return Activate72330(self.ctx)
        if not self.count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Activate72330(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=True)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000944], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay72330(self.ctx)


class Delay72330(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000960], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9230, boxId=30, operator='Equal'):
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000960], stateValue=0):
            return DeActivate72330(self.ctx)


class DeActivate72330(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor72330(self.ctx)
        if self.user_value(key='Barrier23', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8231,8232,8233,8234,8235,8236,8237,8238], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8230], visible=False)
        self.set_interact_object(triggerIds=[10000944], state=0) # On
        self.set_interact_object(triggerIds=[10000960], state=0) # Off
        self.set_user_value(key='Barrier23', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
