""" trigger/02000290_bf/wind.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[701], enable=False)
        self.set_effect(triggerIds=[601], visible=False) # 스킬 준비 효과음
        self.set_effect(triggerIds=[602], visible=False) # 스킬 발동 효과음
        self.set_effect(triggerIds=[603], visible=False) # 스킬 발동 이펙트
        self.set_effect(triggerIds=[604], visible=False) # 스킬 발동 이펙트
        self.set_effect(triggerIds=[605], visible=False) # 스킬 발동 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 종료(self.ctx)
        if self.random_condition(rate=33):
            return A스킬작동(self.ctx)
        if self.random_condition(rate=33):
            return B스킬작동(self.ctx)
        if self.random_condition(rate=34):
            return C스킬작동(self.ctx)


class A스킬작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=4000):
            self.set_effect(triggerIds=[601], visible=True)
            self.show_guide_summary(entityId=20002906, textId=20002906)
            return 스킬발동(self.ctx)


class B스킬작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=6000):
            self.set_effect(triggerIds=[601], visible=True)
            self.show_guide_summary(entityId=20002906, textId=20002906)
            return 스킬발동(self.ctx)


class C스킬작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=8000):
            self.set_effect(triggerIds=[601], visible=True)
            self.show_guide_summary(entityId=20002906, textId=20002906)
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=4000):
            self.hide_guide_summary(entityId=20002906)
            self.set_effect(triggerIds=[602], visible=True)
            self.set_effect(triggerIds=[603], visible=True)
            self.set_effect(triggerIds=[604], visible=True)
            self.set_effect(triggerIds=[605], visible=True)
            self.set_skill(triggerIds=[701], enable=True)
            return 스킬랜덤(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002906)


initial_state = 시작대기중
