""" trigger/02020301_bf/3000051_phase_4_interect_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200021,200022], visible=False)
        self.set_interact_object(triggerIds=[10003111], state=2) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Phase_4_Interect_01', value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_4_Interect_01', value=0):
            return 대기(self.ctx)


class 인터렉트_설정(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200021,200022], visible=True)
        self.set_interact_object(triggerIds=[10003111], state=1) # 4페이즈 인터렉트 오브젝트 생성

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10003111], stateValue=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_4_Interect_01', value=0):
            return 대기(self.ctx)


class 인터렉트_동작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200021,200022], visible=False)
        self.set_ai_extra_data(key='Phase_4_Sub_Bomb_1', value=1, isModify=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_4_Interect_01', value=0):
            return 대기(self.ctx)


class 인터렉트_리셋(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='Phase_4_Sub_Bomb_1', value=0, isModify=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_4_Interect_01', value=0):
            return 대기(self.ctx)


initial_state = 대기
