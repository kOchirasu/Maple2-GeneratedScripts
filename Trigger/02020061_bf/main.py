""" trigger/02020061_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawnId=2, isEnable=False)
        self.enable_spawn_point_pc(spawnId=3, isEnable=False)
        self.enable_spawn_point_pc(spawnId=4, isEnable=False)
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.reset_timer(timerId='3')
        self.set_actor(triggerId=1901, visible=True, initialSequence='Idle_A') # <연출용 액터>
        self.set_effect(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=True)
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048], visible=True) # <가두기 트리거 메쉬>
        self.shadow_expedition(type='CloseBossGauge')
        self.set_user_value(triggerId=99990002, key='SpawnStart', value=0)
        self.set_user_value(triggerId=99990003, key='ObjectPhase', value=0)
        self.set_user_value(triggerId=99990008, key='BossPhase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 유저카운트(self.ctx)


class 유저카운트(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FieldGameStart', value=1):
            return 딜레이(self.ctx)
        if self.user_value(key='FieldGameStart', value=2):
            return 방폭(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9002, type='trigger', achieve='corps_battle')
        self.set_event_ui(type=1, arg2='$02020061_BF__MAIN__0$', arg3='5000')
        self.select_camera(triggerId=999, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작(self.ctx)


class 방폭(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020061_BF__MAIN__1$', arg3='10000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 내보내기(self.ctx)


class 내보내기(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)
        self.enable_spawn_point_pc(spawnId=2, isEnable=True)
        self.enable_spawn_point_pc(spawnId=3, isEnable=True)
        self.enable_spawn_point_pc(spawnId=4, isEnable=True)
        self.reset_camera(interpolationTime=1)
        self.set_effect(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=False)
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048], visible=False)
        self.set_event_ui(type=0, arg2='1,3')
        self.set_event_ui(type=1, arg2='$02020061_BF__MAIN__2$', arg3='5000')
        self.set_timer(timerId='1', seconds=180, startDelay=1, interval=1, vOffset=60) # <1라운드 게임 플레이 타임 설정>
        self.shadow_expedition(type='OpenBossGauge', maxGaugePoint=800)
        self.set_user_value(triggerId=99990002, key='SpawnStart', value=1)
        self.set_actor(triggerId=1901, visible=False, initialSequence='Idle_A') # <연출용 액터>
        self.create_monster(spawnIds=[701], animationEffect=False) # <무적 오브젝트 생성>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GaugeClear', value=1):
            return 오브젝트페이즈(self.ctx)
        if self.time_expired(timerId='1'):
            return 실패_세팅(self.ctx)


class 오브젝트페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.give_reward_content(rewardId=31000001)
        self.set_event_ui(type=1, arg2='$02020061_BF__MAIN__3$', arg3='5000')
        self.shadow_expedition(type='CloseBossGauge')
        self.set_event_ui(type=0, arg2='2,3')
        self.reset_timer(timerId='1')
        self.set_user_value(triggerId=99990003, key='ObjectPhase', value=1)
        self.set_timer(timerId='2', seconds=180, startDelay=1, interval=1, vOffset=60) # <2라운드 게임 플레이 타임 설정>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectClear', value=1):
            return 보스페이즈(self.ctx)
        if self.time_expired(timerId='2'):
            return 실패_세팅(self.ctx)


class 보스페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.give_reward_content(rewardId=31000002)
        self.destroy_monster(spawnIds=[-1])
        self.set_event_ui(type=1, arg2='$02020061_BF__MAIN__4$', arg3='5000')
        self.reset_timer(timerId='2')
        self.set_event_ui(type=0, arg2='3,3')
        self.set_user_value(triggerId=99990008, key='BossPhase', value=1)
        self.set_timer(timerId='3', seconds=180, startDelay=1, interval=1, vOffset=60) # <3라운드 게임 플레이 타임 설정>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossClear', value=1):
            return 성공_세팅(self.ctx)
        if self.time_expired(timerId='3'):
            return 실패_세팅(self.ctx)


class 성공_세팅(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__MAIN__5$')
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.reset_timer(timerId='3')
        self.set_user_value(triggerId=99990002, key='SpawnStart', value=2)
        self.set_user_value(triggerId=99990003, key='ObjectPhase', value=2)
        self.set_user_value(triggerId=99990004, key='BossPhase', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 성공_대사용(self.ctx)


class 성공_대사용(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003533, illust='Bliche_smile', duration=5000, script='$02020061_BF__MAIN__6$')
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 성공(self.ctx)


class 실패_세팅(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__MAIN__7$')
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.reset_timer(timerId='3')
        self.set_user_value(triggerId=99990002, key='SpawnStart', value=2)
        self.set_user_value(triggerId=99990003, key='ObjectPhase', value=2)
        self.set_user_value(triggerId=99990004, key='BossPhase', value=2)
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 실패_대사용(self.ctx)


class 실패_대사용(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020061_BF__MAIN__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 실패(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self):
        self.field_war_end(isClear=True)
        self.set_achievement(type='trigger', achieve='FieldwarAchieve_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self):
        self.field_war_end(isClear=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
