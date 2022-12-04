""" trigger/02020301_bf/3000053_phase_4_interect_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200025,200026], visible=False)
        self.set_interact_object(triggerIds=[10003113], state=2) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_4_Interect_03', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_4_Interect_03', value=0):
            return 대기(self.ctx)


class 인터렉트_설정(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200025,200026], visible=True)
        self.set_interact_object(triggerIds=[10003113], state=1) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003113], stateValue=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_4_Interect_03', value=0):
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200025,200026], visible=False)
        self.set_ai_extra_data(key='Phase_4_Sub_Bomb_3', value=1, isModify=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_4_Interect_03', value=0):
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='Phase_4_Sub_Bomb_3', value=0, isModify=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_4_Interect_03', value=0):
            return 대기(self.ctx)


initial_state = 대기
