""" trigger/02000207_bf/bossspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZakumDungeonEnd', value=1):
            return 종료딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999103, key='BattleEnd', value=1)
        self.set_user_value(triggerId=999102, key='BattleEnd2', value=1) # 자쿰 팔 제거때 용암 올라오게 하는 트리거 xml 담당, 999102_Lavaflow.xml
        self.set_user_value(triggerId=999108, key='BattleEnd2', value=1) # 계약의 토템에 의해 왼쪽 용암 올라오게 하는 트리거 xml 담당, 999108_Lavaflow.xm
        self.set_user_value(triggerId=999109, key='BattleEnd2', value=1) # 계약의 토템에 의해 오른쪽 용암 올라오게 하는 트리거 xml 담당, 999109_Lavaflow.xml
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_user_value(triggerId=999103, key='BattleEnd', value=1)
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0) # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


initial_state = 대기
