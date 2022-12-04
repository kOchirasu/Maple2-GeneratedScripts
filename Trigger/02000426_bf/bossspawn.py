""" trigger/02000426_bf/bossspawn.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
        self.set_user_value(key='ZakumBodyAppearance', value=0) # 이 변수 신호 받아서 자쿰 몸체 등장시키는데 사용함

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 던전코드별보스등장(self.ctx)


class 던전코드별보스등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id(dungeonId=23040003):
            return 어려운난이도보스등장(self.ctx)
        if self.dungeon_id(dungeonId=23041003):
            return 쉬운난이도보스등장(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 어려운난이도보스등장(self.ctx)


class 어려운난이도보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False) # 어려운 난이도의 자쿰 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


class 쉬운난이도보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False) # 쉬운 난이도의 자쿰 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZakumBodyAppearance', value=1):
            return 자쿰몸체등장(self.ctx)
        if self.user_value(key='ZakumDungeonEnd', value=1):
            return 종료딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 자쿰몸체등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='ZakumBodyAppearance', value=0) # 이 변수 0 초기화 하여 무한루프 빠지는거 방지

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id(dungeonId=23040003):
            return 어려운난이도_자쿰몸등장(self.ctx)
        if self.dungeon_id(dungeonId=23041003):
            return 쉬운난이도_자쿰몸등장(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 어려운난이도_자쿰몸등장(self.ctx)


class 어려운난이도_자쿰몸등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2011], animationEffect=False) # 어려운 난이도의 자쿰몸 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


class 쉬운난이도_자쿰몸등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2012], animationEffect=False) # 쉬운 난이도의 자쿰몸 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 시간 기능 종료시킴
        self.dungeon_close_timer()
        self.set_achievement(achieve='ZakumKritiasClear') # arg3="ZakumKritiasClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함
        self.set_user_value(triggerId=999103, key='BattleEnd', value=1)
        self.set_user_value(triggerId=999102, key='BattleEnd2', value=1) # 자쿰 팔 제거때 용암 올라오게 하는 트리거 xml 담당, 999102_Lavaflow.xml
        self.set_user_value(triggerId=999108, key='BattleEnd2', value=1) # 계약의 토템에 의해 왼쪽 용암 올라오게 하는 트리거 xml 담당, 999108_Lavaflow.xm
        self.set_user_value(triggerId=999109, key='BattleEnd2', value=1) # 계약의 토템에 의해 오른쪽 용암 올라오게 하는 트리거 xml 담당, 999109_Lavaflow.xml
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.remove_buff(boxId=199, skillId=50005300)
        self.remove_buff(boxId=199, skillId=50005301)
        self.remove_buff(boxId=199, skillId=50001450) # 죽음의 저주 걸렸을때 자쿰 클리어 하면, 해제함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.set_user_value(triggerId=999103, key='BattleEnd', value=1)
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.remove_buff(boxId=199, skillId=50005300)
        self.remove_buff(boxId=199, skillId=50005301)
        self.remove_buff(boxId=199, skillId=50001450) # 죽음의 저주 걸렸을때 자쿰 클리어 하면, 해제함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


initial_state = 시작
