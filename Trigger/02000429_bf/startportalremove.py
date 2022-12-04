""" trigger/02000429_bf/startportalremove.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 시작지점포탈_우선생성(self.ctx)


class 시작지점포탈_우선생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True) # 최초 스타팅 포인트 지점에 배치된 메인 전투판으로 들어서기 위한 포탈 최초에 활성화 시키기,   arg1="3" 은 포탈ID

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=40000):
            return 시작지점포탈제거_직전(self.ctx)


class 시작지점포탈제거_직전(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=770, boxId=1):
            return 시작지점포탈_제거알림메시지생성(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 시작지점포탈제거_실행(self.ctx)


class 시작지점포탈_제거알림메시지생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000428_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 시작지점포탈제거_실행(self.ctx)


class 시작지점포탈제거_실행(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False) # 최초 스타팅 포인트 지점에 배치된 메인 전투판으로 들어서기 위한 포탈을 비활성화 상태로 만들기,   arg1="3" 은 포탈ID

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
