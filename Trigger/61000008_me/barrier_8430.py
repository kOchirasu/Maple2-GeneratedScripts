""" trigger/61000008_me/barrier_8430.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_interact_object(triggerIds=[10000952], state=2) # On
        self.set_interact_object(triggerIds=[10000968], state=2) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Barrier43', value=1):
            return Sensor7431(self.ctx)
        if self.user_value(key='Barrier43', value=2):
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43', value=3):
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43', value=4):
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43', value=5):
            return Sensor7435(self.ctx)


# 1명 방어 불가
class Sensor7431(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=1) # yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='1', operator='Equal'):
            return Activate7431(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Activate7431(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='1', operator='Equal'):
            return Sensor7431(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


# 2명
class Sensor7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_interact_object(triggerIds=[10000952], state=0) # On
        self.set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='2', operator='Equal'):
            return SafeGreen7432(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class SafeGreen7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='2', operator='Equal'):
            return Enable7432(self.ctx)
        if not self.count_users(boxId=9430, minUsers='2', operator='Equal'):
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Enable7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000952], stateValue=0):
            # On
            return Activate7432(self.ctx)
        if not self.count_users(boxId=9430, minUsers='2', operator='Equal'):
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Activate7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=True)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='2', operator='Equal'):
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7432(self.ctx)


class Delay7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='2', operator='Equal'):
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000968], stateValue=0):
            # Off
            return DeActivate7432(self.ctx)


class DeActivate7432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7432(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


# 3명
class Sensor7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_interact_object(triggerIds=[10000952], state=0) # On
        self.set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='3', operator='Equal'):
            return SafeGreen7433(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class SafeGreen7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='3', operator='Equal'):
            return Enable7433(self.ctx)
        if not self.count_users(boxId=9430, minUsers='3', operator='Equal'):
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Enable7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000952], stateValue=0):
            # On
            return Activate7433(self.ctx)
        if not self.count_users(boxId=9430, minUsers='3', operator='Equal'):
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Activate7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=True)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='3', operator='Equal'):
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7433(self.ctx)


class Delay7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='3', operator='Equal'):
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000968], stateValue=0):
            # Off
            return DeActivate7433(self.ctx)


class DeActivate7433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7433(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


# 4명
class Sensor7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_interact_object(triggerIds=[10000952], state=0) # On
        self.set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='4', operator='Equal'):
            return SafeGreen7434(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class SafeGreen7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='4', operator='Equal'):
            return Enable7434(self.ctx)
        if not self.count_users(boxId=9430, minUsers='4', operator='Equal'):
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Enable7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000952], stateValue=0):
            # On
            return Activate7434(self.ctx)
        if not self.count_users(boxId=9430, minUsers='4', operator='Equal'):
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Activate7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=True)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='4', operator='Equal'):
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7434(self.ctx)


class Delay7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='4', operator='Equal'):
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000968], stateValue=0):
            # Off
            return DeActivate7434(self.ctx)


class DeActivate7434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7434(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


# 5명
class Sensor7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=1) # yellow
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_interact_object(triggerIds=[10000952], state=0) # On
        self.set_interact_object(triggerIds=[10000968], state=0) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='5', operator='Equal'):
            return SafeGreen7435(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class SafeGreen7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=7430, key='Color43', value=2) # green

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9430, minUsers='5', operator='Equal'):
            return Enable7435(self.ctx)
        if not self.count_users(boxId=9430, minUsers='5', operator='Equal'):
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Enable7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9430], sound='DDStop_Stage_Shiled_01')
        self.set_interact_object(triggerIds=[10000952], state=1) # On

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000952], stateValue=0):
            # On
            return Activate7435(self.ctx)
        if not self.count_users(boxId=9430, minUsers='5', operator='Equal'):
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Activate7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=True)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000952], state=2) # On

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='5', operator='Equal'):
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.wait_tick(waitTick=1000):
            return Delay7435(self.ctx)


class Delay7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000968], state=1) # Off

    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9430, minUsers='5', operator='Equal'):
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)
        if self.object_interacted(interactIds=[10000968], stateValue=0):
            # Off
            return DeActivate7435(self.ctx)


class DeActivate7435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Sensor7435(self.ctx)
        if self.user_value(key='Barrier43', value=10):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8431,8432,8433,8434,8435,8436], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[8430], visible=False)
        self.set_interact_object(triggerIds=[10000952], state=0) # On
        self.set_interact_object(triggerIds=[10000968], state=0) # Off
        self.set_user_value(key='Barrier43', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
