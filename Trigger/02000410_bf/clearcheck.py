""" trigger/02000410_bf/clearcheck.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작(self.ctx)


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_check_play_time(playSeconds=420):
            return 지금부터파티전멸체크(self.ctx)
        if self.user_value(key='ThirdPhase', value=1):
            return 지금부터파티전멸체크(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전포기(self.ctx)


class 지금부터파티전멸체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[700]):
            return 전멸던전실패연출01(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전포기(self.ctx)
        if self.dungeon_check_play_time(playSeconds=900):
            return 분완료15(self.ctx)


class 던전포기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1]) # 던전 포기 버튼 누르면 바로 몬스터 제거하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전멸던전실패연출01(self.ctx)


class 전멸던전실패연출01(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11000144, illust='tristan_normal', duration=4000, script='$02000410_BF__ClearCheck__0$', voice='ko/Npc/00002171')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전멸던전실패연출02(self.ctx)


class 전멸던전실패연출02(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=4000, script='$02000410_BF__ClearCheck__1$', voice='ko/Npc/00002156')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전멸던전실패(self.ctx)


class 전멸던전실패(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 분완료15(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(feature='DungeonRankBalance_01', missionId=24090003) # ## 한국용 던전랭크 코드: 15분 경과시 던전랭크 체크하기 위한 신호
        self.dungeon_mission_complete(feature='DungeonRankBalance_02', missionId=24090013) # ## 중국용 던전랭크 코드: 15분 경과시 던전랭크 체크하기 위한 신호

    def on_tick(self) -> common.Trigger:
        if self.check_npc_damage(spawnId=102, damageRate=1, operator='GreaterEqual'): # 인페르녹 보스 스폰ID : 102 의 몬스터가 지금까지 받은 대미지가 HP 기준 대비 100%보다 적으면 던전 실패 처리
            return 성공연출시작(self.ctx)
        if self.check_npc_damage(spawnId=102, damageRate=1, operator='Less'):
            return 실패연출시작(self.ctx)
        """
        condition name="CheckNpcDamage"   파라미터 기능 설명

                    spawnPointID: 체크할 NPC스폰포인트ID 스포너 안에 여러 NPC가 있을 경우 맨 첫 NPC를 체크합니다.
                    damageRate: 누적 대미지 기준 값 1.0 일경우 해당 npc의 maxHP 0.5의 경우 50%
                    operator: 연산자 기준 입니다 생략시 해당 값 이상 (GreaterEqual 이며) 다음 옵션을 사용 가능합니다.
                    Greater, GreaterEqual, Equal, LessEqual, Less,
        """


class 성공연출시작(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='EventClear', value=1) # 여기서는 인페르녹 보스 소멸 시키지 말고, AI쪽으로 EventClear = 1 신호 보내서 던전성공 이벤트 연출용도 NPC로 교체하고 본인 자신은 퇴장하도록 설정함
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=3000, script='$02000410_BF__ClearCheck__2$', voice='ko/Npc/00002182')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 성공연출01(self.ctx)


class 성공연출01(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='movie', usm='Common/WorldInvasionScene5.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=8000, script='$02000410_BF__ClearCheck__3$', voice='ko/Npc/00002177')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 성공연출02_pre(self.ctx)


class 성공연출02_pre(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 성공연출02(self.ctx)


class 성공연출02(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\WorldInvasionScene6.usm', movieId=1, skipType='needAll')

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 최종성공처리(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 최종성공처리(self.ctx)


class 실패연출시작(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='EventLeave', value=1) # 여기서는 인페르녹 보스 소멸 시키지 말고, AI쪽으로 EventLeave = 1 신호 보내서 던전실패 이벤트 연출용도 NPC로 교체하고 본인 자신은 퇴장하도록 설정함
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=3000, script='$02000410_BF__ClearCheck__4$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 실패연출01(self.ctx)


class 실패연출01(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='movie', usm='Common/WorldInvasionScene5.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_talk(npcId=11003533, illust='Bliche_nomal', duration=8000, script='$02000410_BF__ClearCheck__5$')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 실패연출02(self.ctx)


class 실패연출02(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003795, illust='infernog_nomal', duration=4000, script='$02000410_BF__ClearCheck__6$', voice='ko/Monster/60000722')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 실패연출03(self.ctx)


class 실패연출03(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003795, illust='infernog_nomal', duration=4000, script='$02000410_BF__ClearCheck__7$', voice='ko/Monster/60000723')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 실패연출05(self.ctx)


class 실패연출05(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_surprise', duration=4000, script='$02000410_BF__ClearCheck__8$', voice='ko/Npc/00002165')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 실패연출06(self.ctx)


class 실패연출06(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003533, illust='Bliche_closeEye', duration=4000, script='$02000410_BF__ClearCheck__9$', voice='ko/Npc/00002155')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 최종실패처리(self.ctx)


class 최종성공처리(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1]) # 대포하고 12시 방향의 파괴 직전의 인페르녹 전함 제거함
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # arg3="ClearBalrogMagicBurster" 는 achieve.xlsx 의 코드 21230095 던전 클리어 조건 트로피 설정에 넣는 데이터임
        self.set_achievement(triggerId=750, type='trigger', achieve='infernogout')
        self.set_achievement(triggerId=750, type='trigger', achieve='ClearBalrogMagicBurster') # arg1="750"는 MS2TriggerBox   TriggerObjectID = 750  이것으로 02000410 맵에 트리거 박스가 2개 있는데(700, 750)  750이 안전부활 장소까지 포함되는 범위라서 이거 사용함
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 던전 나가기 위한 포탈 생성,   arg1="2" 은 포탈ID, 안전 부활 지점에 있는 포탈
        self.dungeon_clear() # 던전성공

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 최종실패처리(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1]) # 대포하고 12시 방향의 파괴 직전의 인페르녹 전함 제거함
        self.set_achievement(triggerId=750, type='trigger', achieve='infernogout')
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 던전 나가기 위한 포탈 생성,   arg1="2" 은 포탈ID, 안전 부활 지점에 있는 포탈
        self.dungeon_fail() # 던전실패

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


initial_state = Ready
