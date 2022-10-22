""" trigger/52010038_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[6299], visible=False)
        shadow_expedition(type='CloseBossGauge')
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_buff(boxIds=[199], skillId=70000109, level=1, arg4=False, arg5=False)
        create_monster(spawnIds=[1805,1806], arg2=False)
        create_monster(spawnIds=[1201], arg2=False)
        spawn_npc_range(rangeIds=[1001,1002,1003,1004,1005,1006,1007,1008], isAutoTargeting=False)
        spawn_npc_range(rangeIds=[1101,1102,1103,1104,1105,1106], isAutoTargeting=False)
        spawn_npc_range(rangeIds=[1801,1802,1803,1804], isAutoTargeting=False)
        # <action name="SetCinematicIntro" text="&lt;font color='#ffd200' size='90'&gt;Press 'ESC' to Start&lt;/font&gt;\n\n\n\n\n\n\n\n\n\n\n\n"/>
        set_skip(state=시작)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작()

    def on_exit(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 시작(state.State):
    def on_enter(self):
        set_skip()
        set_user_value(triggerId=999001, key='GaugeOpen', value=1)
        set_user_value(triggerId=992001, key='WaveStart', value=1)
        set_user_value(triggerId=999004, key='AllertStart', value=1)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=150):
            return 부상병발생()


class 부상병발생(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=7000, script='$52010038_QD__main__4$', voice='ko/Npc/00002057')
        set_user_value(triggerId=993001, key='WoundStart', value=1)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=300):
            return 차폭탄방어2()


class 차폭탄방어2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=60, clearAtZero=True, display=True, arg5=80)
        set_user_value(triggerId=992003, key='bombStart', value=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=연출02종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 카메라304()


class 카메라304(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=True)
        set_skip(state=연출02종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 부관대사03()


class 부관대사03(state.State):
    def on_enter(self):
        set_skip(state=연출02종료)
        add_cinematic_talk(npcId=11003536, illustId='Neirin_surprise', msg='$52010038_QD__MAIN__0$', duration=7000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출02종료()


class 연출02종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_skip()
        side_npc_talk(npcId=11003537, illust='Mason_closeEye', duration=7000, script='$52010038_QD__main__5$', voice='ko/Npc/00002095')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2008,2009,2010]):
            create_monster(spawnIds=[4020], arg2=False)
            create_monster(spawnIds=[4020], arg2=False)
            reset_timer(timerId='99')
            return 차폭탄방어완료조건2()


class 차폭탄방어완료조건2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2097]):
            return 종료()
        if wait_tick(waitTick=1000):
            side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=6000, script='$52010038_QD__main__6$', voice='ko/Npc/00002106')
            return 층이벤트스킵3()


class 층이벤트스킵3(state.State):
    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=700):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6201,6202,6203,6204], visible=False)
        create_monster(spawnIds=[2098], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=보스연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 카메라302()


class 카메라302(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_skip(state=보스연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 보스대사01()


class 보스대사01(state.State):
    def on_enter(self):
        set_skip(state=보스연출종료)
        add_cinematic_talk(npcId=11003185, illustId='ShadowClaw_normal', msg='$52010038_QD__MAIN__2$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 보스이동()


class 보스이동(state.State):
    def on_enter(self):
        set_skip(state=보스연출종료)
        move_npc(spawnId=2098, patrolName='MS2PatrolData_2098')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 카메라303()


class 카메라303(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003185, illustId='ShadowClaw_normal', msg='$52010038_QD__MAIN__3$', duration=5000, align='left')
        select_camera(triggerId=303, enable=True)
        set_skip(state=보스연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 보스연출종료()


class 보스연출종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6299], visible=True)
        side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=7000, script='$52010038_QD__main__8$', voice='ko/Npc/00002058')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_skip()
        destroy_monster(spawnIds=[2098])
        create_monster(spawnIds=[2099], arg2=True)
        create_monster(spawnIds=[1099], arg2=False)
        set_user_value(triggerId=992001, key='WaveSlowDown', value=1)
        set_user_value(triggerId=992002, key='WaveStart', value=1)

    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=1000):
            return 종료()
        if monster_dead(boxIds=[1099]):
            set_user_value(triggerId=999001, key='EngineIsDead', value=1)
            return 종료()


class 종료(state.State):
    pass


