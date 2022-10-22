""" trigger/02010052_bf/torchlight_02.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7010], visible=False) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[110]):
            return burn_state()


class burn_state(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7502], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025,5026], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_02__0$', arg3='3000')
        set_effect(triggerIds=[7010], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return spawn_state()


class spawn_state(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)


