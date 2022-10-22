""" trigger/52010038_qd/gauge.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GaugeOpen', value=1):
            return 게이지시작()


class 게이지시작(state.State):
    def on_enter(self):
        set_skill(triggerIds=[700], isEnable=True)
        set_user_value(triggerId=999002, key='GaugeStart', value=1)
        set_user_value(triggerId=991001, key='GaugeStart', value=1)
        set_user_value(triggerId=991002, key='GaugeStart', value=1)
        set_user_value(triggerId=991003, key='GaugeStart', value=1)
        set_user_value(triggerId=991004, key='GaugeStart', value=1)
        shadow_expedition(type='OpenBossGauge', title='$52010038_QD__gauge__2$', maxGaugePoint=1000)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=1000):
            return 성공()
        if user_value(key='CoreIsDead', value=1):
            return 실패()
        if user_value(key='EngineIsDead', value=1):
            return 실패()

    def on_exit(self):
        shadow_expedition(type='CloseBossGauge')
        set_user_value(triggerId=991001, key='GaugeClosed', value=1)
        set_user_value(triggerId=991002, key='GaugeClosed', value=1)
        set_user_value(triggerId=991003, key='GaugeClosed', value=1)
        set_user_value(triggerId=991004, key='GaugeClosed', value=1)
        set_user_value(triggerId=999002, key='GaugeClosed', value=1)


class 성공(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=6000, script='$52010038_QD__gauge__3$', voice='ko/Npc/00002107')
        set_achievement(triggerId=199, type='trigger', achieve='skyfortress_takeoff')
        set_event_ui(type=7, arg2='$52010038_QD__GAUGE__0$', arg3='2500')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 정리()


class 실패(state.State):
    def on_enter(self):
        set_event_ui(type=5, arg2='$52010038_QD__GAUGE__1$', arg3='2500')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            move_user(mapId=2000092, portalId=20)
            return 정리()


class 정리(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_user_value(triggerId=992001, key='WaveEnd', value=1)
        set_user_value(triggerId=992002, key='WaveEnd', value=1)
        set_user_value(triggerId=993001, key='WoundEnd', value=1)
        set_user_value(triggerId=999004, key='AllertEnd', value=1)
        move_user(mapId=52010039, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


