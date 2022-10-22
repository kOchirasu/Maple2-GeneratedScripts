""" trigger/66000004_gd/buffskill_03.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_actor(triggerId=203, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10603]):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_enter(self):
        set_actor(triggerId=203, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[10603]):
            return 초기화()
        if random_condition(rate=33):
            return A스킬작동()
        if random_condition(rate=33):
            return B스킬작동()
        if random_condition(rate=34):
            return C스킬작동()


class A스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7301], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7301], isEnable=False)
            return 시작대기중()


class B스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7302], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7302], isEnable=False)
            return 시작대기중()


class C스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7303], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7303], isEnable=False)
            return 시작대기중()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[7301], isEnable=False)
        set_skill(triggerIds=[7302], isEnable=False)
        set_skill(triggerIds=[7303], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


