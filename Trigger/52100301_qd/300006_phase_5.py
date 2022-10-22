""" trigger/52100301_qd/300006_phase_5.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='AI_Phase', value=5):
            return 패이즈_5_시작()


class 패이즈_5_시작(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300006_PHASE_5__0$', duration=3176)
        set_effect(triggerIds=[200021,200022,200023,200024,200025,200026,200027,200028], visible=False)
        set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_user_value(triggerId=3000051, key='Phase_4_Interect_01', value=0) # 페이즈4 장치 삭제
        set_user_value(triggerId=3000052, key='Phase_4_Interect_02', value=0)
        set_user_value(triggerId=3000053, key='Phase_4_Interect_03', value=0)
        set_user_value(triggerId=3000054, key='Phase_4_Interect_04', value=0)
        set_effect(triggerIds=[200001,200002,200003,200004,200005,200006,200007,200008], visible=False)
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300006_PHASE_5__1$', duration=3176)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아르케온_등장()


class 아르케온_등장(state.State):
    def on_enter(self):
        set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아르케온_탈것_생성()


class 아르케온_탈것_생성(state.State):
    def on_enter(self):
        set_user_value(triggerId=3000061, key='Phase_5_Interect_01', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return None # Missing State: 게임종료


