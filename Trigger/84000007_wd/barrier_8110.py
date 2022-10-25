""" trigger/84000007_wd/barrier_8110.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_interact_object(triggerIds=[10000938], state=2) # On
        self.set_interact_object(triggerIds=[10000954], state=2) # Off

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Barrier11', value=1):
            return Sensor7111(self.ctx)
        if self.user_value(key='Barrier11', value=2):
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11', value=3):
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11', value=4):
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11', value=5):
            return Sensor7115(self.ctx)


# 1명 방어 불가
class Sensor7111(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=1) # yellow

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=1, operator='Equal'):
            return Activate7111(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Activate7111(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=1, operator='Equal'):
            return Sensor7111(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7112(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_interact_object(triggerIds=[10000938], state=0) # On
        self.set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=2, operator='Equal'):
            return SafeGreen7112(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class SafeGreen7112(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=2, operator='Equal'):
            return Enable7112(self.ctx)
        if not self.count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Enable7112(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000938], stateValue=0):
            return Activate7112(self.ctx)
        if not self.count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Activate7112(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=True)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7112(self.ctx)


class Delay7112(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=2, operator='Equal'):
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000954], stateValue=0):
            return DeActivate7112(self.ctx)


class DeActivate7112(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7112(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7113(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_interact_object(triggerIds=[10000938], state=0) # On
        self.set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=3, operator='Equal'):
            return SafeGreen7113(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class SafeGreen7113(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=3, operator='Equal'):
            return Enable7113(self.ctx)
        if not self.count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Enable7113(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000938], stateValue=0):
            return Activate7113(self.ctx)
        if not self.count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Activate7113(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=True)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7113(self.ctx)


class Delay7113(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=3, operator='Equal'):
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000954], stateValue=0):
            return DeActivate7113(self.ctx)


class DeActivate7113(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7113(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7114(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_interact_object(triggerIds=[10000938], state=0) # On
        self.set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=4, operator='Equal'):
            return SafeGreen7114(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class SafeGreen7114(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=4, operator='Equal'):
            return Enable7114(self.ctx)
        if not self.count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Enable7114(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000938], stateValue=0):
            return Activate7114(self.ctx)
        if not self.count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Activate7114(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=True)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7114(self.ctx)


class Delay7114(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=4, operator='Equal'):
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000954], stateValue=0):
            return DeActivate7114(self.ctx)


class DeActivate7114(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7114(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7115(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=1) # yellow
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_interact_object(triggerIds=[10000938], state=0) # On
        self.set_interact_object(triggerIds=[10000954], state=0) # Off

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=5, operator='Equal'):
            return SafeGreen7115(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class SafeGreen7115(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7110, key='Color11', value=2) # green

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9110, boxId=5, operator='Equal'):
            return Enable7115(self.ctx)
        if not self.count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Enable7115(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9110], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000938], state=1) # On

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000938], stateValue=0):
            return Activate7115(self.ctx)
        if not self.count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Activate7115(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=True)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000938], state=2) # On

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7115(self.ctx)


class Delay7115(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000954], state=1) # Off

    def on_tick(self) -> common.Trigger:
        if not self.count_users(boxId=9110, boxId=5, operator='Equal'):
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000954], stateValue=0):
            return DeActivate7115(self.ctx)


class DeActivate7115(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7115(self.ctx)
        if self.user_value(key='Barrier11', value=10):
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8111,8112,8113,8114], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8110], visible=False)
        self.set_interact_object(triggerIds=[10000938], state=0) # On
        self.set_interact_object(triggerIds=[10000954], state=0) # Off
        self.set_user_value(key='Barrier11', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
