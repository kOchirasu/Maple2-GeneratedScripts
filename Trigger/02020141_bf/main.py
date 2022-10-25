""" trigger/02020141_bf/main.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 나가기 포탈 최초에는 감추기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 보스등장준비(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 보스등장준비(self.ctx)


class 보스등장준비(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[99], animationEffect=False) # EventSpawnPointNPC 의 SpawnPointID가 99 번, 즉   arg1="99"

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1100):
            return 클리어성공유무체크시작(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 클리어성공유무체크시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 연출딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 던전실패(common.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 메인 전투판에 나가기 포탈 생성하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


class 연출딜레이(common.Trigger):
    def on_enter(self):
        self.dungeon_mission_complete(missionId=23090000) # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 던전 클리어 미션 달성임
        self.set_achievement(type='trigger', achieve='TurkaDungeonClear') # achieve.xlsx 트로피 투르카던전클리어 조건 체크, arg1을 넣지 않으면 이 맵 전체에 있는 플레이어를 체크함 , 참고로 arg1을 넣으면 트리거 박스 안에 있는 플레이어만 체크하는 것임

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 보스 죽음과 동시에 자체 60초 늘어나기 때문에,  <state name="연출딜레이"> 단계 끝나고 WaitTick=9초 후에 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.dungeon_clear()
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 메인 전투판에 나가기 포탈 생성하기


initial_state = 시작대기중
