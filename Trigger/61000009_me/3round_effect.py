""" trigger/61000009_me/3round_effect.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='3Round_Effect', value=1):
            return Spawn_Start_Ready()


class Spawn_Start_Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7999], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Skill_01()


class Skill_01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[5021], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Skill_02()


class Skill_02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[5022], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Skill_03()


class Skill_03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[5023], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Skill_04()


class Skill_04(state.State):
    def on_enter(self):
        set_skill(triggerIds=[5024], isEnable=True)


