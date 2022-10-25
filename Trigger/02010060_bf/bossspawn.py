""" trigger/02010060_bf/bossspawn.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 포탈ID 1: 던전 입구에 있는 나가기 포탈 셋팅 초기화
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 포탈ID 2: 3페이즈 전투 장소에 나가기 포탈 셋팅 초기화
        self.set_portal(portalId=8, visible=False, enable=False, minimapVisible=False) # 포탈ID 8: 1페이즈 전투 장소에 나가기 포탈 셋팅 초기화, 보스가 1페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함
        self.set_portal(portalId=9, visible=False, enable=False, minimapVisible=False) # 포탈ID 9: 2페이즈 전투 장소에 나가기 포탈 셋팅 초기화, 보스가 2페이즈에서 순삭 당할 수 있기 때문에 1페이즈 전투 장소에도 나가기 포탈 생성함

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 몬스터등장(self.ctx)


class 몬스터등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2099], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 종료딜레이(self.ctx)


class 종료딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=9, visible=True, enable=True, minimapVisible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작대기중
