""" trigger/52010038_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[6299], visible=False)
        self.shadow_expedition(type='CloseBossGauge')
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(boxIds=[199], skillId=70000109, level=1, isPlayer=False, isSkillSet=False)
        self.create_monster(spawnIds=[1805,1806], animationEffect=False)
        self.create_monster(spawnIds=[1201], animationEffect=False)
        self.spawn_npc_range(rangeIds=[1001,1002,1003,1004,1005,1006,1007,1008], isAutoTargeting=False)
        self.spawn_npc_range(rangeIds=[1101,1102,1103,1104,1105,1106], isAutoTargeting=False)
        self.spawn_npc_range(rangeIds=[1801,1802,1803,1804], isAutoTargeting=False)
        # <action name="SetCinematicIntro" text="&lt;font color='#ffd200' size='90'&gt;Press 'ESC' to Start&lt;/font&gt;\n\n\n\n\n\n\n\n\n\n\n\n"/>
        self.set_skip(state=시작)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_user_value(triggerId=999001, key='GaugeOpen', value=1)
        self.set_user_value(triggerId=992001, key='WaveStart', value=1)
        self.set_user_value(triggerId=999004, key='AllertStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=150):
            return 부상병발생(self.ctx)


class 부상병발생(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=7000, script='$52010038_QD__main__4$', voice='ko/Npc/00002057')
        self.set_user_value(triggerId=993001, key='WoundStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=300):
            return 차폭탄방어2(self.ctx)


class 차폭탄방어2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='99', seconds=60, startDelay=1, interval=1, vOffset=80)
        self.set_user_value(triggerId=992003, key='bombStart', value=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=연출02종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 카메라304(self.ctx)


class 카메라304(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=304, enable=True)
        self.set_skip(state=연출02종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부관대사03(self.ctx)


class 부관대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=연출02종료)
        self.add_cinematic_talk(npcId=11003536, illustId='Neirin_surprise', msg='$52010038_QD__MAIN__0$', duration=7000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출02종료(self.ctx)


class 연출02종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_skip()
        self.side_npc_talk(npcId=11003537, illust='Mason_closeEye', duration=7000, script='$52010038_QD__main__5$', voice='ko/Npc/00002095')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2008,2009,2010]):
            self.create_monster(spawnIds=[4020], animationEffect=False)
            self.create_monster(spawnIds=[4020], animationEffect=False)
            self.reset_timer(timerId='99')
            return 차폭탄방어완료조건2(self.ctx)


class 차폭탄방어완료조건2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2097]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=1000):
            self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=6000, script='$52010038_QD__main__6$', voice='ko/Npc/00002106')
            return 층이벤트스킵3(self.ctx)


class 층이벤트스킵3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=700):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6201,6202,6203,6204], visible=False)
        self.create_monster(spawnIds=[2098], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=보스연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 카메라302(self.ctx)


class 카메라302(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.set_skip(state=보스연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 보스대사01(self.ctx)


class 보스대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=보스연출종료)
        self.add_cinematic_talk(npcId=11003185, illustId='ShadowClaw_normal', msg='$52010038_QD__MAIN__2$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 보스이동(self.ctx)


class 보스이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=보스연출종료)
        self.move_npc(spawnId=2098, patrolName='MS2PatrolData_2098')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 카메라303(self.ctx)


class 카메라303(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003185, illustId='ShadowClaw_normal', msg='$52010038_QD__MAIN__3$', duration=5000, align='left')
        self.select_camera(triggerId=303, enable=True)
        self.set_skip(state=보스연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 보스연출종료(self.ctx)


class 보스연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6299], visible=True)
        self.side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=7000, script='$52010038_QD__main__8$', voice='ko/Npc/00002058')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_skip()
        self.destroy_monster(spawnIds=[2098])
        self.create_monster(spawnIds=[2099], animationEffect=True)
        self.create_monster(spawnIds=[1099], animationEffect=False)
        self.set_user_value(triggerId=992001, key='WaveSlowDown', value=1)
        self.set_user_value(triggerId=992002, key='WaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=1000):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            self.set_user_value(triggerId=999001, key='EngineIsDead', value=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
