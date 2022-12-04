""" trigger/61000022_me/barrier_8130.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_interact_object(triggerIds=[10000940], state=2) # On
        self.set_interact_object(triggerIds=[10000956], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier13', value=1):
            return Sensor7131(self.ctx)
        if self.user_value(key='Barrier13', value=2):
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13', value=3):
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13', value=4):
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13', value=5):
            return Sensor7135(self.ctx)


# 1명 방어 불가
class Sensor7131(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=1, operator='Equal'):
            return Activate7131(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Activate7131(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=1, operator='Equal'):
            return Sensor7131(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7132(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_interact_object(triggerIds=[10000940], state=0) # On
        self.set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=2, operator='Equal'):
            return SafeGreen7132(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class SafeGreen7132(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=2, operator='Equal'):
            return Enable7132(self.ctx)
        if not self.count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Enable7132(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000940], stateValue=0):
            return Activate7132(self.ctx)
        if not self.count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Activate7132(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=True)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7132(self.ctx)


class Delay7132(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=2, operator='Equal'):
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000956], stateValue=0):
            return DeActivate7132(self.ctx)


class DeActivate7132(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7132(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7133(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_interact_object(triggerIds=[10000940], state=0) # On
        self.set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=3, operator='Equal'):
            return SafeGreen7133(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class SafeGreen7133(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=3, operator='Equal'):
            return Enable7133(self.ctx)
        if not self.count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Enable7133(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000940], stateValue=0):
            return Activate7133(self.ctx)
        if not self.count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Activate7133(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=True)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7133(self.ctx)


class Delay7133(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=3, operator='Equal'):
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000956], stateValue=0):
            return DeActivate7133(self.ctx)


class DeActivate7133(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7133(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7134(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_interact_object(triggerIds=[10000940], state=0) # On
        self.set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=4, operator='Equal'):
            return SafeGreen7134(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class SafeGreen7134(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=4, operator='Equal'):
            return Enable7134(self.ctx)
        if not self.count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Enable7134(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000940], stateValue=0):
            return Activate7134(self.ctx)
        if not self.count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Activate7134(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=True)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7134(self.ctx)


class Delay7134(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=4, operator='Equal'):
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000956], stateValue=0):
            return DeActivate7134(self.ctx)


class DeActivate7134(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7134(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7135(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=1) # yellow
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_interact_object(triggerIds=[10000940], state=0) # On
        self.set_interact_object(triggerIds=[10000956], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=5, operator='Equal'):
            return SafeGreen7135(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class SafeGreen7135(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7130, key='Color13', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9130, boxId=5, operator='Equal'):
            return Enable7135(self.ctx)
        if not self.count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Enable7135(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9130], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000940], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000940], stateValue=0):
            return Activate7135(self.ctx)
        if not self.count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Activate7135(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=True)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000940], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7135(self.ctx)


class Delay7135(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000956], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9130, boxId=5, operator='Equal'):
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000956], stateValue=0):
            return DeActivate7135(self.ctx)


class DeActivate7135(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7135(self.ctx)
        if self.user_value(key='Barrier13', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8131,8132,8133,8134,8135,8136], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8130], visible=False)
        self.set_interact_object(triggerIds=[10000940], state=0) # On
        self.set_interact_object(triggerIds=[10000956], state=0) # Off
        self.set_user_value(key='Barrier13', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
