""" trigger/52100301_qd/3000042_phase_3_interect_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[200011,200012,200013,200014], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_3_Interect_02', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[1003], skillId=62100168, level=1) # 포탑 기절 이뮨

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인터렉트_설정(self.ctx)


class 인터렉트_설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[200011,200012,200013,200014], visible=True)
        self.set_interact_object(triggerIds=[10003121], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003121], stateValue=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_3_Interect_02', value=0):
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[200011,200012,200013,200014], visible=False)
        self.set_ai_extra_data(key='Shoot_Cannon_2', value=1, isModify=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_3_Interect_02', value=0):
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='Shoot_Cannon_2', value=0, isModify=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_3_Interect_02', value=0):
            return 대기(self.ctx)


initial_state = 대기
