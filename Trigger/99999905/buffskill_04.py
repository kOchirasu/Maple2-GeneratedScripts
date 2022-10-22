""" trigger/99999905/buffskill_04.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_actor(triggerId=204, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10604]):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_enter(self):
        set_actor(triggerId=204, visible=True, initialSequence='Dead_A')

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[10604]):
            return 초기화()
        if random_condition(rate=33):
            return A스킬작동()
        if random_condition(rate=33):
            return B스킬작동()
        if random_condition(rate=34):
            return C스킬작동()


class A스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7401], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7401], isEnable=False)
            return 시작대기중()


class B스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7402], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7402], isEnable=False)
            return 시작대기중()


class C스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7403], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7403], isEnable=False)
            return 시작대기중()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[7401], isEnable=False)
        set_skill(triggerIds=[7402], isEnable=False)
        set_skill(triggerIds=[7403], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


