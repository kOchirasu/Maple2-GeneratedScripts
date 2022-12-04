""" trigger/52100301_qd/3000061_phase_5_interect_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200031,200032], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_5_Interect_01', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52100301_QD__3000061_PHASE_5_INTERECT_01__0$', arg3='4000')
        self.create_monster(spawnIds=[999], animationEffect=False) # 탑승 아르케온 등장(연출용)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 탈것_등장(self.ctx)


class 탈것_등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003126], state=1)
        self.destroy_monster(spawnIds=[999])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003126], stateValue=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_5_Interect_01', value=0):
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_5_Interect_01', value=0):
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(boxId=0, additionalEffectId=62100152, level=1):
            return 리셋_대기(self.ctx)
        if self.user_value(key='Phase_5_Interect_01', value=0):
            return 대기(self.ctx)


class 리셋_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작(self.ctx)
        if self.user_value(key='Phase_5_Interect_01', value=0):
            return 대기(self.ctx)


initial_state = 대기
