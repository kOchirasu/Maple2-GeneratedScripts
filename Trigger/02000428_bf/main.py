""" trigger/02000428_bf/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6010,6011], visible=True, arg3=1, delay=1) # 맨 오른쪽 지점에서 대포 배치하기 위한 오프젝트 생성하기 , TriggerObjectID: 6010, 6011
        self.set_mesh(triggerIds=[6000,6001,6002,6003], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(triggerIds=[6004,6005], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 던전 나가기 위한 포탈 초기화 설정,   arg1="1" 은 포탈ID, 메인 전투판에 있는 포탈, 참고로 스타팅 포인트에 있는 나가가 포탈인 arg1="1" 은 활성화 상태로 배치함

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작_인페르녹전함(self.ctx)


class 전투시작_인페르녹전함(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True) # 인페르녹 전함 스폰하기, 스폰ID : 101

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 첫번째페이즈_인페르녹전함(self.ctx)


class 첫번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SecondPhase', value=1):
            return 두번째페이즈_인페르녹전함(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 두번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6010,6011,6012,6013,6014,6015,6016], visible=False, arg3=0, delay=0, scale=0.5) # 맨 오른쪽 건너편 막힌 벽 제거하기 ,    오른쪽 지점 대포 배치하기 위한 오프젝트는 TriggerObjectID: 6010, 6011  이거 제거해야 전투가 쾌적함

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ThirdPhase', value=1):
            return 세번째페이즈_인페르녹등장(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 세번째페이즈_인페르녹등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=True) # 인페르녹 보스 스폰하기, 스폰ID : 102
        self.set_sound(triggerId=8410, enable=True) # 보스 등장하면 보스용 BGM으로 교체하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인페르녹전투시작(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 인페르녹전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102]):
            return 인페르녹처치성공(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


# 던전 포기 버튼 눌렸을 때 혹은 시간이 다 되었을때에 실패 일러스트 연출 처리하기 위한 장치 넣기
class 던전실패(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1]) # 던전 포기 버튼 누르면 바로 몬스터 제거하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전멸던전실패연출01(self.ctx)


class 전멸던전실패연출01(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='tristan_normal', duration=4000, script='$02000410_BF__ClearCheck__10$') # 트리스탄의 "이런 시간이 부족한 건가?! 이대로면 버틸 수 없어!" 대사로, NA는 인페르녹 던전이 시간 버티기가 아닌 제한 시간까지 인페르녹 HP 다 까는 것이 목적이기 때문에 여기서의 트리스탄 대사는 NA만 다름

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전멸던전실패연출02(self.ctx)


class 전멸던전실패연출02(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=6200, script='$02000410_BF__ClearCheck__1$', voice='ko/Npc/00002156')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6200):
            return 전멸던전실패(self.ctx)


class 전멸던전실패(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 인페르녹처치성공(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_stop_timer() # 인페르녹 죽이면 제일 먼저 던전 시간 멈추게 하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 성공연출시작(self.ctx)


class 성공연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=3000, script='$02000410_BF__ClearCheck__2$', voice='ko/Npc/00002182')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 성공연출01(self.ctx)


class 성공연출01(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='movie', usm='Common/WorldInvasionScene5.usm', duration=0) # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_talk(npcId=11003536, illust='Bliche_nomal', duration=8000, script='$02000410_BF__ClearCheck__3$', voice='ko/Npc/00002177')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 성공연출02_pre(self.ctx)


class 성공연출02_pre(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 성공연출02(self.ctx)


class 성공연출02(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\WorldInvasionScene6.usm', movieId=1, skipType='needAll')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 최종성공처리(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 최종성공처리(self.ctx)


class 최종성공처리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1]) # 대포하고 12시 방향의 파괴 직전의 인페르녹 전함 제거함
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(triggerId=750, type='trigger', achieve='ClearBalrogMagicBurster') # arg3="ClearBalrogMagicBurster" 는 achieve.xlsx 의 코드 21230095 던전 클리어 조건 트로피 설정에 넣는 데이터임
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.dungeon_clear() # 던전성공

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


initial_state = Ready
