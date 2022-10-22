""" trigger/63000006_cs/shake02.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 다리흔들기준비()


class 다리흔들기준비(state.State):
    def on_enter(self):
        set_skill(triggerIds=[910], isEnable=False)
        set_skill(triggerIds=[911], isEnable=False)
        set_skill(triggerIds=[912], isEnable=False)
        set_skill(triggerIds=[913], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬발동01()


class 스킬발동01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=42)
        set_skill(triggerIds=[910], isEnable=True)
        set_skill(triggerIds=[911], isEnable=True)
        set_skill(triggerIds=[912], isEnable=True)
        set_skill(triggerIds=[913], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 다리흔들기준비()
        if user_detected(boxIds=[9002]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_skill(triggerIds=[910], isEnable=False)
        set_skill(triggerIds=[911], isEnable=False)
        set_skill(triggerIds=[912], isEnable=False)
        set_skill(triggerIds=[913], isEnable=False)


