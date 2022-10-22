""" trigger/52100301_qd/300002_phase_1.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='AI_Phase', value=1):
            return 텍스트_대기()


class 텍스트_대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 패이즈_1_시작()


class 패이즈_1_시작(state.State):
    def on_enter(self):
        set_user_value(key='AI_Phase', value=0)
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300002_PHASE_1__0$', duration=4176)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


