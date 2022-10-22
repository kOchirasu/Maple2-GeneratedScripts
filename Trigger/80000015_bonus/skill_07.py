""" trigger/80000015_bonus/skill_07.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[712], isEnable=False)
        set_skill(triggerIds=[726], isEnable=False)
        set_visible_breakable_object(triggerIds=[7701,7702,7703,7704], arg2=False)
        set_breakable(triggerIds=[7701,7702,7703,7704], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[7701,7702,7703,7704], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[7701,7702,7703,7704], enabled=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 스킬발동()


class 스킬발동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[712], isEnable=True)
        set_skill(triggerIds=[726], isEnable=True)
        set_breakable(triggerIds=[7701,7702,7703,7704], enabled=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시작()


class 종료(state.State):
    pass


