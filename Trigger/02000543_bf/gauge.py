""" trigger/02000543_bf/gauge.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GaugeOpen', value=1):
            return 게이지시작(self.ctx)


class 게이지시작(common.Trigger):
    def on_enter(self):
        self.shadow_expedition(type='OpenBossGauge', title='$02000543_BF__GAUGE__0$', maxGaugePoint=1000)

    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=1000):
            return 성공(self.ctx)


class 성공(common.Trigger):
    def on_enter(self):
        self.shadow_expedition(type='CloseBossGauge')
        self.destroy_monster(spawnIds=[-1])
        self.set_user_value(triggerId=2001, key='WaveEnd', value=1)
        self.set_user_value(triggerId=2003, key='WaveEnd', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
