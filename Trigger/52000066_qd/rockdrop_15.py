""" trigger/52000066_qd/rockdrop_15.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8011], isEnable=False)
        set_skill(triggerIds=[8012], isEnable=False)
        set_effect(triggerIds=[7011], visible=False) # RockDrop
        set_effect(triggerIds=[7012], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if check_user():
            return Delay01()


class Delay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return RockDrop01()


class RockDrop01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7011], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return RockDrop02()


class RockDrop02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8011], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Delay02()


class Delay02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return RockDrop11()


class RockDrop11(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7012], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return RockDrop12()


class RockDrop12(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8012], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return RockDrop21()


class RockDrop21(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7011], visible=True) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return RockDrop22()


class RockDrop22(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8011], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_skill(triggerIds=[8011], isEnable=False)
        set_skill(triggerIds=[8012], isEnable=False)
        set_effect(triggerIds=[7011], visible=False) # RockDrop
        set_effect(triggerIds=[7012], visible=False) # RockDrop

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return RockDrop01()


