""" trigger/02020301_bf/3000031_phase_2_interect_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003131], state=2) # 2페이즈 인터렉트 오브젝트 대기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_2_Interect_01', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__3000031_PHASE_2_INTERECT_01__0$', duration=3176)
        self.side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__3000031_PHASE_2_INTERECT_01__1$', duration=3176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 인터렉트_설정(self.ctx)


class 인터렉트_설정(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020301_BF__3000031_PHASE_2_INTERECT_01__2$', arg3='4000')
        self.create_monster(spawnIds=[999], animationEffect=False) # 탑승 아르케온 등장(연출용)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 탈것_등장(self.ctx)


class 탈것_등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003131], state=1)
        self.destroy_monster(spawnIds=[999])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003131], stateValue=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_2_Interect_01', value=0):
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_2_Interect_01', value=0):
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawnId=101, additionalEffectId=62100152, level=1):
            return 리셋_대기(self.ctx)
        if self.user_value(key='Phase_2_Interect_01', value=0):
            return 대기(self.ctx)


class 리셋_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_2_Interect_01', value=0):
            return 대기(self.ctx)


initial_state = 대기
