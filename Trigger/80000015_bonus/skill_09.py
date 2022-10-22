""" trigger/80000015_bonus/skill_09.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_skill(triggerIds=[720], isEnable=False)
        set_skill(triggerIds=[721], isEnable=False)
        set_skill(triggerIds=[722], isEnable=False)
        set_skill(triggerIds=[723], isEnable=False)
        set_skill(triggerIds=[724], isEnable=False)
        set_skill(triggerIds=[725], isEnable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 스킬01()


class 스킬01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[720], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 스킬02()


class 스킬02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[721], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 스킬03()


class 스킬03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[722], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 스킬04()


class 스킬04(state.State):
    def on_enter(self):
        set_skill(triggerIds=[723], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 스킬05()


class 스킬05(state.State):
    def on_enter(self):
        set_skill(triggerIds=[724], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 스킬06()


class 스킬06(state.State):
    def on_enter(self):
        set_skill(triggerIds=[725], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 대기시간()


class 종료(state.State):
    pass


