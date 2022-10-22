""" trigger/02000543_bf/gauge.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GaugeOpen', value=1):
            return 게이지시작()


class 게이지시작(state.State):
    def on_enter(self):
        shadow_expedition(type='OpenBossGauge', title='$02000543_BF__GAUGE__0$', maxGaugePoint=1000)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=1000):
            return 성공()


class 성공(state.State):
    def on_enter(self):
        shadow_expedition(type='CloseBossGauge')
        destroy_monster(spawnIds=[-1])
        set_user_value(triggerId=2001, key='WaveEnd', value=1)
        set_user_value(triggerId=2003, key='WaveEnd', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


