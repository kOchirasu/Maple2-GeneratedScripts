""" trigger/02020147_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 던전맵 나가는 포탈, 시작 지점에 위치
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 던전맵 나가는 포탈, 전투판에 위치
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False) # 시작지점에서 전투판으로 가기위한 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[601]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[701,702,703], animationEffect=False) # 이슈라 렌듀비아 유페리아  등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 클리어체크시작(self.ctx)


class 클리어체크시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True) # 시작지점에서 전투판으로 가기위한 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[701,702,703]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_achievement(achieve='IshuraFinalDungeonClear_Quest')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 던전맵 나가는 포탈, 시작 지점에 위치
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 던전맵 나가는 포탈, 전투판에 위치


initial_state = 시작대기중
