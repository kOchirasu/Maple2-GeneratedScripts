""" trigger/02000290_bf/wind.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_skill(triggerIds=[701], isEnable=False)
        set_effect(triggerIds=[601], visible=False) # 스킬 준비 효과음
        set_effect(triggerIds=[602], visible=False) # 스킬 발동 효과음
        set_effect(triggerIds=[603], visible=False) # 스킬 발동 이펙트
        set_effect(triggerIds=[604], visible=False) # 스킬 발동 이펙트
        set_effect(triggerIds=[605], visible=False) # 스킬 발동 이펙트

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 종료()
        if random_condition(rate=33):
            return A스킬작동()
        if random_condition(rate=33):
            return B스킬작동()
        if random_condition(rate=34):
            return C스킬작동()


class A스킬작동(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 종료()
        if wait_tick(waitTick=4000):
            set_effect(triggerIds=[601], visible=True)
            show_guide_summary(entityId=20002906, textId=20002906)
            return 스킬발동()


class B스킬작동(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 종료()
        if wait_tick(waitTick=6000):
            set_effect(triggerIds=[601], visible=True)
            show_guide_summary(entityId=20002906, textId=20002906)
            return 스킬발동()


class C스킬작동(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 종료()
        if wait_tick(waitTick=8000):
            set_effect(triggerIds=[601], visible=True)
            show_guide_summary(entityId=20002906, textId=20002906)
            return 스킬발동()


class 스킬발동(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 종료()
        if wait_tick(waitTick=4000):
            hide_guide_summary(entityId=20002906)
            set_effect(triggerIds=[602], visible=True)
            set_effect(triggerIds=[603], visible=True)
            set_effect(triggerIds=[604], visible=True)
            set_effect(triggerIds=[605], visible=True)
            set_skill(triggerIds=[701], isEnable=True)
            return 스킬랜덤()


class 종료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002906)


