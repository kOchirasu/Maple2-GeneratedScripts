""" trigger/02020097_bf/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False) # 첫번째 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 두번째 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False) # 마지막 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portalId=28, visible=False, enable=False, minimapVisible=False) # 스타팅 부활 지점에서 바로 3페이지 전투판 입구로 가는 순간이동 포탈 최초에는 감추기
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121], visible=False, arg3=0, delay=0, scale=0) # 몬스터는 밟고 플레이어는 밟지 못하는 트리거메쉬 설정하기
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207], visible=False, arg3=0, delay=0, scale=0) # 계단 트리거메쉬 초기화 감추기
        self.set_mesh(triggerIds=[211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239], visible=False, arg3=0, delay=0, scale=0) # 계단 트리거메쉬 초기화 감추기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10]):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[99], animationEffect=False) # 발록 보스 스폰시키기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기상태(self.ctx)


class 대기상태(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StairsOk', value=1): # 2페이즈 전투 다 끝나고 , AI_Balrog_Kritias.xml 발록에게   StairsOk2nd = 1 신호를 받으면 이 부분 실행
            return 계단생성시작중(self.ctx)
        if self.user_value(key='StairsOk2nd', value=1): # 3페이지로 들어서면 보스는 하늘높이 날아가는데, 플레이어가 3페이지 전투판으로 들어서면 즉 이 트기러 영역 안으로 들어오면 보스에게 신호를 보내서 3페이지 전투판으로
            return 계단생성시작중2nd(self.ctx)
        if self.user_detected(boxIds=[11]): # 보스가 죽을 경우
            return 플레이어3페이지전투판으로오기(self.ctx)
        if self.monster_dead(boxIds=[99]):
            return 연출딜레이(self.ctx)


class 계단생성시작중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 계단생성(self.ctx)


class 계단생성(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0, scale=0) # 1페이지 끝내고 2페이지 진입하는 투명벽 제거하기
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207], visible=True, arg3=1, delay=120, scale=0.5) # 계단 트리거메쉬 생성
        self.set_user_value(key='StairsOk', value=0) # 무한 루프 빠지는 것을 막기 위해 이 변수 0 초기화 하기, 이후 이 변수 다시 사용할 일 없음

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기상태(self.ctx)


class 계단생성시작중2nd(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 계단생성2nd(self.ctx)


class 계단생성2nd(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239], visible=True, arg3=1, delay=50, scale=0.5) # 계단 트리거메쉬 생성
        self.set_user_value(key='StairsOk2nd', value=0) # 무한 루프 빠지는 것을 막기 위해 이 변수 0 초기화 하기, 이후 이 변수 다시 사용할 일 없음

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 칸막이제거2nd(self.ctx)


class 칸막이제거2nd(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[302], visible=False, arg3=0, delay=0, scale=0) # 2페이지 끝내고 3페이지 진입하는 투명벽 제거하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기상태(self.ctx)


class 플레이어3페이지전투판으로오기(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='3PhaseSetOk', value=1) # 플레이어가 3페이지 전투판에 들어서면 발록AI에게 3PhaseSetOk=1 신호를 보내서 , 3페이지 전투판으로 점프 내려오도록 함
        self.set_portal(portalId=28, visible=True, enable=True, minimapVisible=True) # 스타팅 부활 지점에서 바로 3페이지 전투판 입구로 가는 순간이동 포탈 생성하도록 하기

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]): # 혹시 몰라서 이부분 다시 설정,          1페이즈 전투 다 끝나고 , AI_Balrog_Kritias.xml 발록에게   StairsOk = 1 신호를 받으면 이 부분 실행
            return 연출딜레이(self.ctx)
        if self.user_value(key='StairsOk', value=1):
            return None # Missing State: 사다리생성


class 연출딜레이(common.Trigger):
    def on_enter(self):
        self.set_achievement(achieve='BalrogKritiasClear') # arg3="BalrogKritiasClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 첫번째 전투판에서 생성
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 두번째 전투판에서 생성
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 마지막 전투판에서 생성
        self.dungeon_clear()


initial_state = 시작대기중
