""" trigger/02000419_bf/1122330_bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 보스 Kill하고 맵에 나가기 포탈 초기화 설정
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False) # 보스 Kill하고 맵에 나가기 포탈 초기화설정
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False) # 스타팅 포인트에서 다리가 사라지면 맵으로 바로 순간이동하는 맵 내부 포탈 설정

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 몬스터등장(self.ctx)


class 몬스터등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2000], animationEffect=False)
        self.set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], visible=False, arg3=0, delay=200, scale=0.5) # BridgeSeconds 지점의 다리 순차적으로 제거하기
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True) # 시작지점에서 전투판으로 순간이도 시켜주는 포탈 생성
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025], visible=False, arg3=0, delay=200, scale=0.5) # BridgeStart  지점의 다리 순차적으로 제거하기

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='NextMove', value=1): # 보스가 죽을 경우
            return 두번째전투판이동다리생성(self.ctx)
        if self.monster_dead(boxIds=[2000]):
            return 연출딜레이(self.ctx)


class 두번째전투판이동다리생성(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], visible=True, arg3=1, delay=120, scale=0.5) # BridgeSeconds, 두번째 전투판으로 이동하기 위한 다리가 순차적으로 생성
        self.set_mesh(triggerIds=[5001,5002], visible=False, arg3=0, delay=0, scale=0) # 두번째 전투판으로 이동하기 위한 다리가 생성되면 5001 : 투명 벽 제거하기, 5002 : 지란트 소환몹이 등장하는 곳에 설치된 투명벽도 제거하기

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000]):
            return 연출딜레이(self.ctx)


class 연출딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 두번째 전투판에서 생성
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True) # 보스 죽이면 나가기 포탈 생성하기, 첫번째 전투판에서 생성
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False) # 스타팅 포인트에서 다리가 사라지면 맵으로 바로 순간이동하는 맵 내부 포탈 설정
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025], visible=True, arg3=1, delay=1, scale=1) # BridgeStart
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=False, arg3=0, delay=0, scale=0) # 시작지점 철창벽
        self.set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], visible=True, arg3=1, delay=120, scale=0.5) # BridgeSeconds, 두번째 전투판으로 이동하기 위한 다리가 순차적으로 생성
        self.set_mesh(triggerIds=[5001,5002], visible=False, arg3=0, delay=0, scale=0) # 두번째 전투판으로 이동하기 위한 다리가 생성되면 5001 : 투명 벽 제거하기, 5002 : 지란트 소환몹이 등장하는 곳에 설치된 투명벽도 제거하기
        self.dungeon_clear()


initial_state = 시작대기중
