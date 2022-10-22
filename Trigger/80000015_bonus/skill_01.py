""" trigger/80000015_bonus/skill_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[701], isEnable=False)
        set_visible_breakable_object(triggerIds=[7101,7102,7103], arg2=False)
        set_breakable(triggerIds=[7101,7102,7103], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[7101,7102,7103], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[7101,7102,7103], enabled=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 스킬발동()


class 스킬발동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[701], isEnable=True)
        set_breakable(triggerIds=[7101,7102,7103], enabled=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시작()


class 종료(state.State):
    pass


