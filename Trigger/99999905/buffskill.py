""" trigger/99999905/buffskill.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_event_ui(type=1, arg2='$99999905__BUFFSKILL__0$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[103]):
            return 초기화()
        if random_condition(rate=33):
            return A스킬작동()
        if random_condition(rate=33):
            return B스킬작동()
        if random_condition(rate=34):
            return C스킬작동()


class A스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7001], isEnable=True)
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            set_skill(triggerIds=[7001], isEnable=False)
            return 스킬랜덤()


class B스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7002], isEnable=True)
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            set_skill(triggerIds=[7002], isEnable=False)
            return 스킬랜덤()


class C스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7003], isEnable=True)
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            set_skill(triggerIds=[7003], isEnable=False)
            return 스킬랜덤()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[7001], isEnable=False)
        set_skill(triggerIds=[7002], isEnable=False)
        set_skill(triggerIds=[7003], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


