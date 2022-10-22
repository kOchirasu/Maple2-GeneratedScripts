""" trigger/02020301_bf/3000031_phase_2_interect_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003131], state=2) # 2페이즈 인터렉트 오브젝트 대기

    def on_tick(self) -> state.State:
        if user_value(key='Phase_2_Interect_01', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__3000031_PHASE_2_INTERECT_01__0$', duration=3176)
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__3000031_PHASE_2_INTERECT_01__1$', duration=3176)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 인터렉트_설정()


class 인터렉트_설정(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020301_BF__3000031_PHASE_2_INTERECT_01__2$', arg3='4000')
        create_monster(spawnIds=[999], arg2=False) # 탑승 아르케온 등장(연출용)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 탈것_등장()


class 탈것_등장(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003131], state=1)
        destroy_monster(spawnIds=[999])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003131], arg2=0):
            return 인터렉트_동작()
        if user_value(key='Phase_2_Interect_01', value=0):
            return 대기()


class 인터렉트_동작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인터렉트_리셋()
        if user_value(key='Phase_2_Interect_01', value=0):
            return 대기()


class 인터렉트_리셋(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=62100152, level=1):
            return 리셋_대기()
        if user_value(key='Phase_2_Interect_01', value=0):
            return 대기()


class 리셋_대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 인터렉트_설정()
        if user_value(key='Phase_2_Interect_01', value=0):
            return 대기()


