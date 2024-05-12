""" trigger/02000543_bf/gauge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GaugeOpen', value=1):
            return 게이지시작(self.ctx)


class 게이지시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition(type='OpenBossGauge', title='$02000543_BF__GAUGE__0$', maxGaugePoint=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=1000):
            return 성공(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition(type='CloseBossGauge')
        self.destroy_monster(spawnIds=[-1])
        self.set_user_value(triggerId=2001, key='WaveEnd', value=1)
        self.set_user_value(triggerId=2003, key='WaveEnd', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
