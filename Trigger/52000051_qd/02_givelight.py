""" trigger/52000051_qd/02_givelight.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001022], state=0) # Lotus
        set_user_value(key='InnerLight', value=0)
        set_user_value(key='InactivateLotus', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='InnerLight', value=1):
            return Delay01()


class Delay01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001022], state=1) # Lotus

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001022], arg2=0):
            return GiveLight01()
        if user_value(key='InactivateLotus', value=1):
            return Wait()


class GiveLight01(state.State):
    def on_enter(self):
        add_buff(boxIds=[9100], skillId=70000102, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Delay01()
        if user_value(key='InactivateLotus', value=1):
            return Wait()


