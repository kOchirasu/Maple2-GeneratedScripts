""" trigger/02020301_bf/3000063_phase_5_interect_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200035,200036], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_5_Interect_03', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인터렉트_설정(self.ctx)


class 인터렉트_설정(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200035,200036], visible=True)
        self.set_interact_object(triggerIds=[10003103], state=1) # 4페이즈 인터렉트 오브젝트 생성
        self.set_visible_breakable_object(triggerIds=[5530], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003103], stateValue=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_5_Interect_03', value=0):
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200035,200036], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_5_Interect_03', value=0):
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_5_Interect_03', value=0):
            return 대기(self.ctx)


initial_state = 대기
