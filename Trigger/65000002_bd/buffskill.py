""" trigger/65000002_bd/buffskill.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 초대기2()


class 초대기2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        play_system_sound_in_box(sound='BD_Buffskill_00')
        show_guide_summary(entityId=26500202, textId=26500202, duration=3000)

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
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7001], isEnable=False)
            return 스킬랜덤()


class B스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7002], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7002], isEnable=False)
            return 스킬랜덤()


class C스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7003], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7003], isEnable=False)
            return 스킬랜덤()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[7001], isEnable=False)
        set_skill(triggerIds=[7002], isEnable=False)
        set_skill(triggerIds=[7003], isEnable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작대기중()


