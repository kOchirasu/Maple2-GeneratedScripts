""" trigger/02020147_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 던전맵 나가는 포탈, 시작 지점에 위치
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 던전맵 나가는 포탈, 전투판에 위치
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False) # 시작지점에서 전투판으로 가기위한 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[601]):
            # ID 601 인 트리거 박스 안에 플레어가 들어서면 보스 생성시키기
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701,702,703], animationEffect=False) # 이슈라 렌듀비아 유페리아  등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 클리어체크시작(self.ctx)


class 클리어체크시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True) # 시작지점에서 전투판으로 가기위한 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[701,702,703]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # 보스 죽음 동작 연출이 끝날때까지 6~8초 정도 기다림
            # arg1 = "특정트리거 박스 안에 있는 유저만 체크하고자 할때"   arg2 = "trigger"    즉 trigger 이거만 쓸수 있음  특정 트리거 박스 안의 유저만 체크 방식을 사용하고자 할때 이 2개 넣어야 함
            self.set_achievement(achieve='IshuraFinalDungeonClear_Quest')
            # arg1 , arg2  넣지 않으면 맵 안에 있는 모든 유저에게 이 업적이 반영됨
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 던전맵 나가는 포탈, 시작 지점에 위치
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 던전맵 나가는 포탈, 전투판에 위치


initial_state = 시작대기중
