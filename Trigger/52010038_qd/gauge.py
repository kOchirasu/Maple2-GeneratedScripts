""" trigger/52010038_qd/gauge.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GaugeOpen', value=1):
            return 게이지시작(self.ctx)


class 게이지시작(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[700], enable=True)
        self.set_user_value(triggerId=999002, key='GaugeStart', value=1)
        self.set_user_value(triggerId=991001, key='GaugeStart', value=1)
        self.set_user_value(triggerId=991002, key='GaugeStart', value=1)
        self.set_user_value(triggerId=991003, key='GaugeStart', value=1)
        self.set_user_value(triggerId=991004, key='GaugeStart', value=1)
        self.shadow_expedition(type='OpenBossGauge', title='$52010038_QD__gauge__2$', maxGaugePoint=1000)

    def on_tick(self) -> common.Trigger:
        if self.shadow_expedition_reach_point(point=1000):
            return 성공(self.ctx)
        if self.user_value(key='CoreIsDead', value=1):
            return 실패(self.ctx)
        if self.user_value(key='EngineIsDead', value=1):
            return 실패(self.ctx)

    def on_exit(self):
        self.shadow_expedition(type='CloseBossGauge')
        self.set_user_value(triggerId=991001, key='GaugeClosed', value=1)
        self.set_user_value(triggerId=991002, key='GaugeClosed', value=1)
        self.set_user_value(triggerId=991003, key='GaugeClosed', value=1)
        self.set_user_value(triggerId=991004, key='GaugeClosed', value=1)
        self.set_user_value(triggerId=999002, key='GaugeClosed', value=1)


class 성공(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=6000, script='$52010038_QD__gauge__3$', voice='ko/Npc/00002107')
        self.set_achievement(triggerId=199, type='trigger', achieve='skyfortress_takeoff')
        self.set_event_ui(type=7, arg2='$52010038_QD__GAUGE__0$', arg3='2500')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 정리(self.ctx)


class 실패(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=5, arg2='$52010038_QD__GAUGE__1$', arg3='2500')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.move_user(mapId=2000092, portalId=20)
            return 정리(self.ctx)


class 정리(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_user_value(triggerId=992001, key='WaveEnd', value=1)
        self.set_user_value(triggerId=992002, key='WaveEnd', value=1)
        self.set_user_value(triggerId=993001, key='WoundEnd', value=1)
        self.set_user_value(triggerId=999004, key='AllertEnd', value=1)
        self.move_user(mapId=52010039, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
